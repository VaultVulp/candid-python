# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from .....identifiers.types.identifier_create import IdentifierCreate
from ...v_2.types.license_type import LicenseType
from ...v_2.types.organization_provider_address import OrganizationProviderAddress
from ...v_2.types.provider_type import ProviderType


class OrganizationProviderCreateV2(pydantic.BaseModel):
    npi: str = pydantic.Field(
        description="The NPI of the provider. This must be all digits [0-9] and exactly 10 characters long."
    )
    is_rendering: bool = pydantic.Field(description="Whether the provider can be used to render services.")
    is_billing: bool = pydantic.Field(description="Whether the provider can be used to bill services.")
    first_name: typing.Optional[str] = pydantic.Field(
        description="The first name of the provider, if the provider is an individual."
    )
    last_name: typing.Optional[str] = pydantic.Field(
        description="The last name of the provider, if the provider is an individual."
    )
    organization_name: typing.Optional[str] = pydantic.Field(
        description="The name of the provider, if the provider is an organization."
    )
    provider_type: ProviderType = pydantic.Field(
        description=("Whether the provider is an individual (NPPES Type 1) or organization (NPPES Type 2) provider.\n")
    )
    tax_id: typing.Optional[str] = pydantic.Field(
        description=(
            "If the provider has a contract with insurance, this must be the same tax ID given to the payer on an IRS W-9 form completed during contracting.\n"
        )
    )
    taxonomy_code: typing.Optional[str] = pydantic.Field(
        description="A code designating classification and specialization."
    )
    license_type: LicenseType = pydantic.Field(description="The type of license that the provider holds.")
    addresses: typing.Optional[typing.List[OrganizationProviderAddress]] = pydantic.Field(
        description="The addresses associated with this provider."
    )
    employment_start_date: typing.Optional[dt.date] = pydantic.Field(
        description="The employment start date for the provider."
    )
    employment_termination_date: typing.Optional[dt.date] = pydantic.Field(
        description="The employment termination date for the provider."
    )
    qualifications: typing.List[IdentifierCreate] = pydantic.Field(
        description="A provider's qualifications such as PTAN, Medicaid Provider Id, etc."
    )

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
