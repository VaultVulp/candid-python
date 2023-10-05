# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ......core.datetime_utils import serialize_datetime
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from .encounter_provider_base import EncounterProviderBase
from .provider_id import ProviderId


class EncounterProvider(EncounterProviderBase):
    provider_id: ProviderId
    address: StreetAddressLongZip
    tax_id: typing.Optional[str]
    npi: str
    taxonomy_code: typing.Optional[str]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
