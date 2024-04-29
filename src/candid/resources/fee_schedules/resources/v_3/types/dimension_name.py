# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DimensionName(str, enum.Enum):
    """
    The name of a dimension.
    """

    PAYER_UUID = "payer_uuid"
    ORGANIZATION_BILLING_PROVIDER_ID = "organization_billing_provider_id"
    CPT_CODE = "cpt_code"

    def visit(
        self,
        payer_uuid: typing.Callable[[], T_Result],
        organization_billing_provider_id: typing.Callable[[], T_Result],
        cpt_code: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DimensionName.PAYER_UUID:
            return payer_uuid()
        if self is DimensionName.ORGANIZATION_BILLING_PROVIDER_ID:
            return organization_billing_provider_id()
        if self is DimensionName.CPT_CODE:
            return cpt_code()