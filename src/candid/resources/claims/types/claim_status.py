# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClaimStatus(str, enum.Enum):
    BILLER_RECEIVED = "biller_received"
    CODED = "coded"
    SUBMITTED_TO_PAYER = "submitted_to_payer"
    MISSING_INFORMATION = "missing_information"
    NOT_BILLABLE = "not_billable"
    WAITING_FOR_PROVIDER = "waiting_for_provider"
    ERA_RECEIVED = "era_received"
    REJECTED = "rejected"
    DENIED = "denied"
    PAID = "paid"
    PAID_INCORRECTLY = "paid_incorrectly"
    FINALIZED_PAID = "finalized_paid"
    FINALIZED_DENIED = "finalized_denied"
    HELD_BY_CUSTOMER = "held_by_customer"

    def visit(
        self,
        biller_received: typing.Callable[[], T_Result],
        coded: typing.Callable[[], T_Result],
        submitted_to_payer: typing.Callable[[], T_Result],
        missing_information: typing.Callable[[], T_Result],
        not_billable: typing.Callable[[], T_Result],
        waiting_for_provider: typing.Callable[[], T_Result],
        era_received: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        denied: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        paid_incorrectly: typing.Callable[[], T_Result],
        finalized_paid: typing.Callable[[], T_Result],
        finalized_denied: typing.Callable[[], T_Result],
        held_by_customer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ClaimStatus.BILLER_RECEIVED:
            return biller_received()
        if self is ClaimStatus.CODED:
            return coded()
        if self is ClaimStatus.SUBMITTED_TO_PAYER:
            return submitted_to_payer()
        if self is ClaimStatus.MISSING_INFORMATION:
            return missing_information()
        if self is ClaimStatus.NOT_BILLABLE:
            return not_billable()
        if self is ClaimStatus.WAITING_FOR_PROVIDER:
            return waiting_for_provider()
        if self is ClaimStatus.ERA_RECEIVED:
            return era_received()
        if self is ClaimStatus.REJECTED:
            return rejected()
        if self is ClaimStatus.DENIED:
            return denied()
        if self is ClaimStatus.PAID:
            return paid()
        if self is ClaimStatus.PAID_INCORRECTLY:
            return paid_incorrectly()
        if self is ClaimStatus.FINALIZED_PAID:
            return finalized_paid()
        if self is ClaimStatus.FINALIZED_DENIED:
            return finalized_denied()
        if self is ClaimStatus.HELD_BY_CUSTOMER:
            return held_by_customer()