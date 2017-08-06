"""
This module holds dynamically generated classes.
For more info see protocol.py and protocol.json.
"""

# =============================================================================
# >> IMPORTS
# =============================================================================
# obs-ws-rc
from .struct import Struct, StructField, StructMeta


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# All classes that inherit from BaseEvent will be available by their names
# in this dictionary
events = {}


# =============================================================================
# >> BASE CLASSES
# =============================================================================
class BaseEventMeta(StructMeta):
    def __init__(cls, name, bases, namespace):
        cls._fields = cls._fields[:] + (
            StructField('update_type', "update-type", str),
            StructField('stream_timecode', "stream-timecode", str, True),
            StructField('rec_timecode', "rec-timecode", str, True),
        )

        super().__init__(name, bases, namespace)

        try:
            type_name = cls.type_name
        except NotImplementedError:
            return

        if type_name in events:
            raise ValueError(
                "Class for event '{type_name}' already exists".format(
                    type_name=type_name))

        events[type_name] = cls


class BaseEvent(Struct, metaclass=BaseEventMeta):
    @property
    def type_name(self):
        raise NotImplementedError
