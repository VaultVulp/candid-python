# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.remove_none_from_dict import remove_none_from_dict
from ....commons.types.page_token import PageToken
from .types.payer import Payer
from .types.payer_page import PayerPage
from .types.payer_uuid import PayerUuid


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, payer_uuid: PayerUuid) -> Payer:
        """
        Parameters:
            - payer_uuid: PayerUuid.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/payers/v3/{payer_uuid}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> PayerPage:
        """
        Parameters:
            - limit: typing.Optional[int]. Defaults to 100

            - search_term: typing.Optional[str].

            - page_token: typing.Optional[PageToken].
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/payers/v3"),
            params=remove_none_from_dict({"limit": limit, "search_term": search_term, "page_token": page_token}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, payer_uuid: PayerUuid) -> Payer:
        """
        Parameters:
            - payer_uuid: PayerUuid.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/payers/v3/{payer_uuid}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Payer, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        search_term: typing.Optional[str] = None,
        page_token: typing.Optional[PageToken] = None,
    ) -> PayerPage:
        """
        Parameters:
            - limit: typing.Optional[int]. Defaults to 100

            - search_term: typing.Optional[str].

            - page_token: typing.Optional[PageToken].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/payers/v3"),
            params=remove_none_from_dict({"limit": limit, "search_term": search_term, "page_token": page_token}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PayerPage, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
