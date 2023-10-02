# This file was auto-generated by Fern from our API Definition.

import typing

from ...environment import CandidApiEnvironment
from .resources.v_2.client import AsyncV2Client, V2Client


class EligibilityClient:
    def __init__(
        self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token
        self.v_2 = V2Client(environment=self._environment, token=self._token)


class AsyncEligibilityClient:
    def __init__(
        self, *, environment: CandidApiEnvironment = CandidApiEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token
        self.v_2 = AsyncV2Client(environment=self._environment, token=self._token)
