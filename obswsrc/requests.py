"""
This module holds dynamically generated classes.
For more info see protocol.py and protocol.json.
"""

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python
from enum import Enum

# obs-ws-rc
from .struct import Struct, StructField, StructMeta


# =============================================================================
# >> BASE CLASSES
# =============================================================================
class ResponseStatus(Enum):
    OK = 'OK'
    ERROR = 'ERROR'


class BaseResponseMeta(StructMeta):
    def __init__(cls, name, bases, namespace):
        cls._fields = cls._fields[:] + (
            StructField('message_id', "message-id", str),
            StructField(
                'status',
                "status",
                lambda status: ResponseStatus(status.upper())
            ),
            StructField('error', "error", str, True),
        )

        super().__init__(name, bases, namespace)


class BaseResponse(Struct, metaclass=BaseResponseMeta):
    pass


class BaseRequest(Struct):
    @property
    def type_name(self):
        raise NotImplementedError

    class response_class(BaseResponse):
        pass

    def get_request_data(self, message_id):
        dict_ = self.copy()
        dict_['request-type'] = self.type_name
        dict_['message-id'] = message_id
        return dict_


def dummy_request(**kwargs):
    raise NotImplementedError("protocol.json doesn't implement this request")

AuthenticateRequest = dummy_request
GetAuthRequiredRequest = dummy_request
