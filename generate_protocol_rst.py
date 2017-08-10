"""Generate protocol.rst using protocol.json."""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
import json
from pathlib import Path


# =============================================================================
# >> CONSTANTS
# =============================================================================
PARA_LINE_LENGTH = 80


# =============================================================================
# >> PATHS
# =============================================================================
ROOT = Path(__name__).absolute().parent
PROTOCOL_RST = ROOT / "docs" / "protocol.rst"
PROTOCOL_JSON = ROOT / "obswsrc" / "protocol.json"


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def link(name):
    return ("`view PROTOCOL.md entry on '{}' <https://github.com/"
            "Palakis/obs-websocket/blob/master/"
            "PROTOCOL.md#{}>`_".format(name, name.lower()))


def render_title(text, char):
    return text + "\n" + (char * len(text)) + "\n\n"


def render_def(def_, text):
    max_line_len = PARA_LINE_LENGTH - 3

    result = "\n"
    result += def_ + "\n"

    words = text.split()
    line_len = 0
    for word in words:
        if line_len + len(word) + 1 > max_line_len:
            result += "\n"
        else:
            result += " "

        result += word
        line_len = 0

    result += "\n\n"
    return result


def render_list(items, indent=0):
    result = "\n\n"
    for item in items:
        result += " " * 2 * indent + "- " + item + "\n"
    result += "\n\n"
    return result


def render_fields(fields, indent=0):
    result = ""
    for field_obj in fields:
        result += render_list(
            [field_obj['attr_name'].replace('_', " ").upper()], indent=indent)

        result += render_list([
            "**type:** `" + field_obj['type'] + "`_",
            "**pythonic name:** ``" + field_obj['attr_name'] + "``",
            "**internal name:** *" + field_obj['field_name'] + "*",
            "**is optional?** " + ["No", "Yes"][field_obj.get(
                'optional', False)],
        ], indent=indent+1)

    return result


def render_type(type_name, type_obj):
    result = ""
    result += render_title(type_name, "+")

    if type_obj['type'] == 'builtin':
        result += render_list(["**Style:** This type is native to Python"])

    elif type_obj['type'] == 'struct':
        result += render_list([
            "**Style:** This type contains statically typed fields"])

        result += render_list(["**Fields:**"])
        result += render_fields(type_obj.get('fields', []), indent=1)

    elif type_obj['type'] == 'var_struct':
        result += render_list([
            "**Style:** The number and types of the fields can vary"])

        line = "**Allowed types:**"
        for type_name_ in type_obj['allowed_types']:
            line += " `" + type_name_ + "`_"

        result += render_list([line])

    elif type_obj['type'] == 'collection':
        result += render_list(["**Style:** This type represents a list of "
                               "objects of other type"])

        result += render_list([
            "**Item type:** `" + type_obj['item_type'] + "`_"])

    else:
        raise ValueError("Unknown type: {}".format(type_obj['type']))

    return result


def render_request(request_name, request_obj):
    result = ""
    result += render_title(request_name, "+")

    result += render_list(["**Description:** " + link(request_name)])

    result += render_list(["**Request Fields:**"])
    result += render_fields(request_obj.get('fields', []), indent=1)

    result += render_list(["**Response Fields:**"])
    result += render_fields(
        request_obj.get('response', {}).get('fields', []), indent=1)

    return result


def render_event(event_name, event_obj):
    result = ""
    result += render_title(event_name, "+")

    result += render_list(["**Description:** " + link(event_name)])
    result += render_list(["**Fields:**"])
    result += render_fields(event_obj.get('fields', []), indent=1)

    return result


def main():
    if not PROTOCOL_JSON.is_file():
        raise FileNotFoundError(
            "Couldn't locate {}".format(str(PROTOCOL_JSON)))

    with open(str(PROTOCOL_JSON)) as f_json,\
            open(str(PROTOCOL_RST), 'w') as f_rst:

        protocol = json.load(f_json)

        f_rst.write(render_title("Protocol Reference", "="))

        # Types
        f_rst.write(render_title("Types", "-"))

        for native_type in (bool, float, int, str):
            f_rst.write(render_type(native_type.__name__, {'type': 'builtin'}))

        for type_name, type_obj in sorted(
                protocol['types'].items(), key=lambda item: item[0].lower()):

            f_rst.write(render_type(type_name, type_obj))

        # Requests
        f_rst.write(render_title("Requests", "-"))

        for request_name, request_obj in sorted(
                protocol['requests'].items(),
                key=lambda item: item[0].lower()):

            f_rst.write(render_request(request_name, request_obj))

        # Events
        f_rst.write(render_title("Events", "-"))

        for event_name, event_obj in sorted(
                protocol['events'].items(), key=lambda item: item[0].lower()):

            f_rst.write(render_request(event_name, event_obj))

if __name__ == "__main__":
    main()
