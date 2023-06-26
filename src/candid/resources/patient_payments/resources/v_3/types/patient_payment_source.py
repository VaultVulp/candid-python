# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatientPaymentSource(str, enum.Enum):
    MANUAL_ENTRY = "MANUAL_ENTRY"
    CHARGEBEE_PAYMENTS = "CHARGEBEE_PAYMENTS"
    CHARGEBEE_MANUALLY_VOIDED_BY_CANDID = "CHARGEBEE MANUALLY VOIDED BY CANDID"
    CHARGEBEE_REFUNDS = "CHARGEBEE_REFUNDS"
    SQUARE_REFUNDS = "SQUARE_REFUNDS"
    SQUARE_PAYMENTS = "SQUARE_PAYMENTS"
    STRIPE_CHARGES = "STRIPE_CHARGES"
    STRIPE_REFUNDS = "STRIPE_REFUNDS"
    ELATION_PAYMENTS = "ELATION_PAYMENTS"

    def visit(
        self,
        manual_entry: typing.Callable[[], T_Result],
        chargebee_payments: typing.Callable[[], T_Result],
        chargebee_manually_voided_by_candid: typing.Callable[[], T_Result],
        chargebee_refunds: typing.Callable[[], T_Result],
        square_refunds: typing.Callable[[], T_Result],
        square_payments: typing.Callable[[], T_Result],
        stripe_charges: typing.Callable[[], T_Result],
        stripe_refunds: typing.Callable[[], T_Result],
        elation_payments: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatientPaymentSource.MANUAL_ENTRY:
            return manual_entry()
        if self is PatientPaymentSource.CHARGEBEE_PAYMENTS:
            return chargebee_payments()
        if self is PatientPaymentSource.CHARGEBEE_MANUALLY_VOIDED_BY_CANDID:
            return chargebee_manually_voided_by_candid()
        if self is PatientPaymentSource.CHARGEBEE_REFUNDS:
            return chargebee_refunds()
        if self is PatientPaymentSource.SQUARE_REFUNDS:
            return square_refunds()
        if self is PatientPaymentSource.SQUARE_PAYMENTS:
            return square_payments()
        if self is PatientPaymentSource.STRIPE_CHARGES:
            return stripe_charges()
        if self is PatientPaymentSource.STRIPE_REFUNDS:
            return stripe_refunds()
        if self is PatientPaymentSource.ELATION_PAYMENTS:
            return elation_payments()