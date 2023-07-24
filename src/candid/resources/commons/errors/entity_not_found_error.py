# This file was auto-generated by Fern from our API Definition.

from ....core.api_error import ApiError
from ..types.entity_not_found_error_message import EntityNotFoundErrorMessage


class EntityNotFoundError(ApiError):
    def __init__(self, body: EntityNotFoundErrorMessage):
        super().__init__(status_code=404, body=body)