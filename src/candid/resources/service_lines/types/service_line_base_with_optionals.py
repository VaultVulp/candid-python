# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.facility_type_code import FacilityTypeCode
from ...diagnoses.types.diagnosis_id import DiagnosisId
from ...invoices.types.invoice import Invoice
from .service_line_adjustment import ServiceLineAdjustment
from .service_line_base import ServiceLineBase
from .service_line_denial_reason import ServiceLineDenialReason
from .service_line_era_data import ServiceLineEraData


class ServiceLineBaseWithOptionals(ServiceLineBase):
    charge_amount_cents: typing.Optional[int]
    allowed_amount_cents: typing.Optional[int]
    insurance_balance_cents: typing.Optional[int]
    patient_balance_cents: typing.Optional[int]
    paid_amount_cents: typing.Optional[int]
    patient_responsibility_cents: typing.Optional[int]
    diagnosis_id_zero: typing.Optional[DiagnosisId]
    diagnosis_id_one: typing.Optional[DiagnosisId]
    diagnosis_id_two: typing.Optional[DiagnosisId]
    diagnosis_id_three: typing.Optional[DiagnosisId]
    service_line_era_data: typing.Optional[ServiceLineEraData]
    service_line_manual_adjustments: typing.Optional[typing.List[ServiceLineAdjustment]]
    related_invoices: typing.Optional[typing.List[Invoice]]
    denial_reason: typing.Optional[ServiceLineDenialReason]
    place_of_service_code: typing.Optional[FacilityTypeCode]

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
