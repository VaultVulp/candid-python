# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.claim_id import ClaimId
from ...commons.types.date_range_optional_end import DateRangeOptionalEnd
from ...commons.types.decimal import Decimal
from ...commons.types.service_line_id import ServiceLineId
from ...commons.types.service_line_units import ServiceLineUnits
from .service_line_base_with_optionals import ServiceLineBaseWithOptionals


class ServiceLine(ServiceLineBaseWithOptionals):
    service_line_id: ServiceLineId
    procedure_code: str
    quantity: Decimal = pydantic.Field(
        description=(
            "String representation of a Decimal that can be parsed by most libraries.\n"
            "A ServiceLine quantity cannot contain more than one digit of precision.\n"
            "Example: 1.1 is valid, 1.11 is not.\n"
        )
    )
    units: ServiceLineUnits
    claim_id: ClaimId
    date_of_service_range: DateRangeOptionalEnd = pydantic.Field(
        description=(
            "A range of dates of service for this service line. If the service line is for a single date, the end date\n"
            "will be empty.\n"
        )
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