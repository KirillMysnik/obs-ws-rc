# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
import json
from pathlib import Path

# obs-ws-rc
from . import (
    events as events_module,
    requests as requests_module,
    types as types_module
)
from .protocol import build_events, build_requests, build_types


# =============================================================================
# >> ALL DECLARATION
# =============================================================================
__all__ = ('OBSWS', )


# =============================================================================
# >> PROTOCOL INITIALIZATION
# =============================================================================
_PROTOCOL_PATH = Path(__file__).parent / "protocol.json"

if _PROTOCOL_PATH.is_file():
    with open(str(_PROTOCOL_PATH)) as f:
        protocol = json.load(f)

        types = build_types(protocol)
        for type_name, type_ in types.items():
            setattr(types_module, type_name, type_)

        requests = build_requests(protocol, types)
        for request_name, request in requests.items():
            setattr(requests_module, request_name, request)

        events = build_events(protocol, types)
        for event_name, event in events.items():
            setattr(events_module, event_name, event)


# =============================================================================
# >> FORWARD IMPORTS
# =============================================================================
from .client import OBSWS
