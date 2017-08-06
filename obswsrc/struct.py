# =============================================================================
# >> CONSTANTS
# =============================================================================
SKIP_OPTIONAL_CHECK = False


# =============================================================================
# >> CLASSES
# =============================================================================
class BaseStruct(dict):
    pass


class StructField:
    def __init__(self, attr_name, field_name, value_type, optional=False):
        self.attr_name = attr_name
        self.field_name = field_name
        self.value_type = value_type
        self.optional = optional


class StructMeta(type):
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)

        cls._fields_by_attr_name = {}
        cls._fields_by_field_name = {}

        for field in cls._fields:
            cls._fields_by_attr_name[field.attr_name] = field
            cls._fields_by_field_name[field.field_name] = field


class Struct(BaseStruct, metaclass=StructMeta):
    _fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__()

        if len(args) == 1 and not kwargs:

            # Initialization from a unJSONed dict with OBS naming
            for field_name, raw_value in args[0].items():
                try:
                    field = self._fields_by_field_name[field_name]
                except KeyError:
                    raise TypeError(
                        "Struct '{class_name}': '{field_name}' is an invalid "
                        "field name for this struct".format(
                            class_name=self.__class__.__name__,
                            field_name=field_name))

                value = field.value_type(raw_value)
                self[field_name] = value

        elif not args:

            # Initialization from Python-friendly attributes
            for attr_name, value in kwargs.items():
                try:
                    field = self._fields_by_attr_name[attr_name]
                except KeyError:
                    raise TypeError(
                        "Struct '{class_name}': '{attr_name}' is an invalid "
                        "keyword argument for this struct".format(
                            class_name=self.__class__.__name__,
                            attr_name=attr_name))

                if not isinstance(value, field.value_type):
                    raise TypeError(
                        "Struct '{class_name}': '{attr_name}' value should be "
                        "of type '{type_name}'".format(
                            class_name=self.__class__.__name__,
                            attr_name=attr_name,
                            type_name=field.value_type.__name__))

                self[field.field_name] = value

        else:
            raise TypeError(
                "{class_name} can initialized only either with 1 positional "
                "argument (dictionary of fields) or with keyword "
                "arguments".format(class_name=self.__class__.__name__))

        # Make sure that all required fields are set
        for field in self._fields:
            if SKIP_OPTIONAL_CHECK or field.optional:
                continue

            if field.field_name not in self:
                raise TypeError(
                    "Struct '{class_name}': Missing required {field_name} "
                    "field".format(
                        class_name=self.__class__.__name__,
                        field_name=field.field_name))

    def __getattr__(self, attr_name):
        try:
            field = self._fields_by_attr_name[attr_name]
        except KeyError:
            raise AttributeError(
                "'{class_name}' object has no attribute '{attr_name}'".format(
                    class_name=self.__class__.__name__, attr_name=attr_name))

        return self[field.field_name]

    def __setattr__(self, attr_name, value):
        try:
            field = self._fields_by_attr_name[attr_name]
        except KeyError:
            raise AttributeError(
                "'{class_name}' object has no attribute '{attr_name}'".format(
                    class_name=self.__class__.__name__, attr_name=attr_name))

        if not isinstance(value, field.value_type):
            raise TypeError(
                "Struct '{class_name}': '{attr_name}' value should be of type "
                "'{type_name}'".format(
                    class_name=self.__class__.__name__,
                    attr_name=attr_name,
                    type_name=field.value_type.__name__))

        self[field.field_name] = value


class VariableStruct(BaseStruct):
    _allowed_types = ()

    def __init__(self, **kwargs):
        super().__init__()

        # Initialization from OBS-named kwargs
        for field_name, value in kwargs.items():
            if type(value) not in self._allowed_types:
                raise TypeError(
                    "VariableStruct '{class_name}': '{field_name}' value "
                    "should be one of these types: {types}".format(
                        class_name=self.__class__.__name__,
                        field_name=field_name,
                        types=', '.join(
                            type_.__name__ for type_ in self._allowed_types
                        )
                    )
                )

            self[field_name] = value

        return

    def __getattr__(self, field_name):
        return self[field_name]

    def __setattr__(self, field_name, value):
        if type(value) not in self._allowed_types:
            raise TypeError(
                "VariableStruct '{class_name}': '{field_name}' value should "
                "be one of these types: {types}".format(
                    class_name=self.__class__.__name__,
                    field_name=field_name,
                    types=', '.join(
                        type_.__name__ for type_ in self._allowed_types
                    )
                )
            )

        self[field_name] = value
