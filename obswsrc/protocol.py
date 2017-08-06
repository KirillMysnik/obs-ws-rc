# =============================================================================
# >> IMPORTS
# =============================================================================
# obs-ws-rc
from .events import BaseEvent
from .requests import BaseRequest, BaseResponse
from .struct import Struct, StructField, VariableStruct


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def _get_fields(obj, known_types):
    fields = []
    for field_obj in obj.get('fields', []):
        attr_name = field_obj['attr_name']
        field_name = field_obj['field_name']
        value_type_str = field_obj['type']
        try:
            value_type = known_types[value_type_str]
        except KeyError:
            raise UnknownType(value_type_str)

        optional = field_obj.get('optional', False)

        fields.append(StructField(
            attr_name, field_name, value_type, optional))

    return tuple(fields)


def _get_allowed_types(obj, known_types):
    allowed_types = []

    for allowed_type_str in obj['allowed_types']:
        try:
            allowed_types.append(known_types[allowed_type_str])
        except KeyError:
            raise UnknownType(allowed_type_str)

    return tuple(allowed_types)


def _get_item_type(obj, known_types):
    item_type_str = obj['item_type']
    try:
        return known_types[item_type_str]
    except KeyError:
        raise UnknownType(item_type_str)


def build_types(protocol):
    struct_meta = type(Struct)
    var_struct_meta = type(VariableStruct)

    known_types = {
        'str': str,
        'int': int,
        'float': float,
        'bool': bool
    }

    types_to_build = list(protocol['types'].items())
    progress = True
    while types_to_build and progress:
        progress = False

        for type_name, type_obj in tuple(types_to_build):
            if type_obj['type'] == "struct":
                try:
                    type_fields = _get_fields(type_obj, known_types)
                except UnknownType:
                    continue

                type_class = struct_meta(
                    type_name,
                    (Struct, ),
                    {'_fields': type_fields}
                )

            elif type_obj['type'] == "var_struct":
                try:
                    allowed_types = _get_allowed_types(type_obj, known_types)
                except UnknownType:
                    continue

                type_class = var_struct_meta(
                    type_name,
                    (VariableStruct, ),
                    {'_allowed_types': allowed_types}
                )

            elif type_obj['type'] == "collection":
                try:
                    item_type = _get_item_type(type_obj, known_types)
                except UnknownType:
                    continue

                def get_type_class(item_type):
                    return lambda data: list(map(item_type, data))

                type_class = get_type_class(item_type)

            else:
                raise ValueError("Unknown type type '{type_name}'".format(
                    type_name=type_name))

            known_types[type_name] = type_class
            types_to_build.remove((type_name, type_obj))
            progress = True

    if types_to_build:
        raise ValueError(
            "The following types have unresolved dependencies: {types}".format(
                types=', '.join(
                    type_name for type_name, type_obj in types_to_build)))

    return known_types


def build_requests(protocol, known_types):
    response_meta = type(BaseResponse)
    request_meta = type(BaseRequest)

    result = {}

    for request_name, request_obj in protocol['requests'].items():
        request_class_name = request_name + "Request"
        response_obj = request_obj.get('response', {})

        request_fields = _get_fields(request_obj, known_types)
        response_fields = _get_fields(response_obj, known_types)

        response_class = response_meta(
            'response_class',
            (BaseResponse, ),
            {'_fields': response_fields}
        )

        request_class = request_meta(
            request_class_name,
            (BaseRequest, ),
            {
                '_fields': request_fields,
                'response_class': response_class,
                'type_name': request_name
            }
        )

        result[request_class_name] = request_class

    return result


def build_events(protocol, known_types):
    event_meta = type(BaseEvent)

    result = {}

    for event_name, event_obj in protocol['events'].items():
        event_class_name = event_name + "Event"

        event_fields = _get_fields(event_obj, known_types)

        event_class = event_meta(
            event_class_name,
            (BaseEvent, ),
            {'_fields': event_fields, 'type_name': event_name}
        )

        result[event_class_name] = event_class

    return result


# =============================================================================
# >> CLASSES
# =============================================================================
class UnknownType(Exception):
    pass
