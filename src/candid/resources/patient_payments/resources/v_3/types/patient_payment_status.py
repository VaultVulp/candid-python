# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PatientPaymentStatus(str, enum.Enum):
    PENDING = "PENDING"
    PAID = "paid"
    CANCELED = "CANCELED"
    VOIDED = "voided"
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    STRIPE_SUCCEEDED = "succeeded"
    STRIPE_PENDING = "pending"
    STRIPE_FAILED = "failed"
    STRIPE_REQUIRES_ACTION = "requires_action"
    STRIPE_CANCELED = "canceled"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        stripe_succeeded: typing.Callable[[], T_Result],
        stripe_pending: typing.Callable[[], T_Result],
        stripe_failed: typing.Callable[[], T_Result],
        stripe_requires_action: typing.Callable[[], T_Result],
        stripe_canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatientPaymentStatus.PENDING:
            return pending()
        if self is PatientPaymentStatus.PAID:
            return paid()
        if self is PatientPaymentStatus.CANCELED:
            return canceled()
        if self is PatientPaymentStatus.VOIDED:
            return voided()
        if self is PatientPaymentStatus.FAILED:
            return failed()
        if self is PatientPaymentStatus.COMPLETED:
            return completed()
        if self is PatientPaymentStatus.STRIPE_SUCCEEDED:
            return stripe_succeeded()
        if self is PatientPaymentStatus.STRIPE_PENDING:
            return stripe_pending()
        if self is PatientPaymentStatus.STRIPE_FAILED:
            return stripe_failed()
        if self is PatientPaymentStatus.STRIPE_REQUIRES_ACTION:
            return stripe_requires_action()
        if self is PatientPaymentStatus.STRIPE_CANCELED:
            return stripe_canceled()