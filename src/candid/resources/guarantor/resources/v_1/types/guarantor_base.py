# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .....commons.types.contact_info import ContactInfo
from .....commons.types.street_address_long_zip import StreetAddressLongZip


class GuarantorBase(pydantic.BaseModel):
    first_name: str
    last_name: str
    external_id: str
    date_of_birth: dt.date
    address: StreetAddressLongZip
    contact_info: ContactInfo

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
