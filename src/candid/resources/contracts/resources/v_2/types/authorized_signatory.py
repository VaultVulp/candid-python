# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AuthorizedSignatory(pydantic.BaseModel):
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    title: typing.Optional[str] = None
    email: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    fax: typing.Optional[str] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}