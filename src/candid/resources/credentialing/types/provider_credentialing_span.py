# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.date import Date
from ...organization_providers.resources.v_2.types.organization_provider import OrganizationProvider
from ...payers.types.payer import Payer
from .credentialing_span_dates import CredentialingSpanDates
from .credentialing_span_status import CredentialingSpanStatus
from .provider_credentialing_span_base import ProviderCredentialingSpanBase
from .provider_credentialing_span_id import ProviderCredentialingSpanId


class ProviderCredentialingSpan(ProviderCredentialingSpanBase):
    provider_credentialing_span_id: ProviderCredentialingSpanId
    rendering_provider: OrganizationProvider = pydantic.Field(
        description=("The rendering provider covered by the credentialing span.\n")
    )
    contracting_provider: OrganizationProvider = pydantic.Field(
        description=("The practice location at which the rendering provider is covered by the credentialing span.\n")
    )
    payer: Payer = pydantic.Field(description=("The payer doing the credentialing.\n"))
    dates: CredentialingSpanDates
    submitted_date: typing.Optional[Date] = pydantic.Field(
        description=("Date that the credential paperwork was submitted.\n")
    )
    credentialing_status: CredentialingSpanStatus = pydantic.Field(description=("Status of the credentialing span.\n"))
    payer_loaded_date: typing.Optional[Date] = pydantic.Field(
        description=("Date that the payer loaded the credentialing span into their system.\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}