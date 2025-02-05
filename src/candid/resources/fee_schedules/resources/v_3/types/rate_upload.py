# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .new_rate import NewRate
from .new_rate_version import NewRateVersion


class RateUpload_NewRate(NewRate):
    type: typing_extensions.Literal["new_rate"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class RateUpload_NewVersion(NewRateVersion):
    type: typing_extensions.Literal["new_version"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


RateUpload = typing.Union[RateUpload_NewRate, RateUpload_NewVersion]
