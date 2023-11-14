# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.datetime_utils import serialize_datetime
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from ....commons.errors.entity_not_found_error import EntityNotFoundError
from ....commons.errors.unauthorized_error import UnauthorizedError
from ....commons.errors.unprocessable_entity_error import UnprocessableEntityError
from ....commons.types.encounter_id import EncounterId
from ....commons.types.entity_not_found_error_message import EntityNotFoundErrorMessage
from ....commons.types.page_token import PageToken
from ....commons.types.task_id import TaskId
from ....commons.types.unauthorized_error_message import UnauthorizedErrorMessage
from ....commons.types.unprocessable_entity_error_message import UnprocessableEntityErrorMessage
from ....commons.types.user_id import UserId
from ..commons.types.task_status import TaskStatus
from ..commons.types.task_type import TaskType
from .errors.task_updated_to_deprecated_status_error import TaskUpdatedToDeprecatedStatusError
from .types.task import Task
from .types.task_actions import TaskActions
from .types.task_create_v_3 import TaskCreateV3
from .types.task_page import TaskPage
from .types.task_sort_options import TaskSortOptions
from .types.task_update_v_3 import TaskUpdateV3
from .types.task_updated_to_deprecated_status_error_type import TaskUpdatedToDeprecatedStatusErrorType

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_actions(self, task_id: TaskId) -> TaskActions:
        """
        **This endpoint is incubating.**

        Parameters:
            - task_id: TaskId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/v3/{task_id}/actions"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TaskActions, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        status: typing.Optional[TaskStatus] = None,
        task_type: typing.Optional[TaskType] = None,
        categories: typing.Optional[str] = None,
        updated_since: typing.Optional[dt.datetime] = None,
        encounter_id: typing.Optional[EncounterId] = None,
        search_term: typing.Optional[str] = None,
        assigned_to_id: typing.Optional[UserId] = None,
        date_of_service_min: typing.Optional[dt.date] = None,
        date_of_service_max: typing.Optional[dt.date] = None,
        billing_provider_npi: typing.Optional[str] = None,
        sort: typing.Optional[TaskSortOptions] = None,
    ) -> TaskPage:
        """
        **This endpoint is incubating.**

        Parameters:
            - limit: typing.Optional[int]. Defaults to 100

            - page_token: typing.Optional[PageToken].

            - status: typing.Optional[TaskStatus].

            - task_type: typing.Optional[TaskType].

            - categories: typing.Optional[str]. Only return tasks with categories that match one in this comma-separated list.

            - updated_since: typing.Optional[dt.datetime]. Only return tasks updated on or after this date-time

            - encounter_id: typing.Optional[EncounterId]. Only return tasks associated with this encounter

            - search_term: typing.Optional[str]. Query tasks by encounter_id, claim_id, task_id, or external_id

            - assigned_to_id: typing.Optional[UserId]. Only return tasks assigned to this user

            - date_of_service_min: typing.Optional[dt.date]. The minimum date of service for the linked encounter

            - date_of_service_max: typing.Optional[dt.date]. The maximum date of service for the linked encounter

            - billing_provider_npi: typing.Optional[str]. The NPI of the billing provider associated with the task's claim

            - sort: typing.Optional[TaskSortOptions]. Defaults to updated_at:desc
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/tasks/v3"),
            params=remove_none_from_dict(
                {
                    "limit": limit,
                    "page_token": page_token,
                    "status": status,
                    "task_type": task_type,
                    "categories": categories,
                    "updated_since": serialize_datetime(updated_since) if updated_since is not None else None,
                    "encounter_id": jsonable_encoder(encounter_id),
                    "search_term": search_term,
                    "assigned_to_id": jsonable_encoder(assigned_to_id),
                    "date_of_service_min": str(date_of_service_min) if date_of_service_min is not None else None,
                    "date_of_service_max": str(date_of_service_max) if date_of_service_max is not None else None,
                    "billing_provider_npi": billing_provider_npi,
                    "sort": sort,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TaskPage, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, task_id: TaskId) -> Task:
        """
        **This endpoint is incubating.**

        Parameters:
            - task_id: TaskId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/v3/{task_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Task, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: TaskCreateV3) -> Task:
        """
        **This endpoint is incubating.**

        Parameters:
            - request: TaskCreateV3.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/tasks/v3"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Task, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, task_id: TaskId, *, request: TaskUpdateV3) -> Task:
        """
        **This endpoint is incubating.**

        Parameters:
            - task_id: TaskId.

            - request: TaskUpdateV3.
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/v3/{task_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Task, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "TaskUpdatedToDeprecatedStatusError":
                raise TaskUpdatedToDeprecatedStatusError(
                    pydantic.parse_obj_as(TaskUpdatedToDeprecatedStatusErrorType, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_actions(self, task_id: TaskId) -> TaskActions:
        """
        **This endpoint is incubating.**

        Parameters:
            - task_id: TaskId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/v3/{task_id}/actions"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TaskActions, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        status: typing.Optional[TaskStatus] = None,
        task_type: typing.Optional[TaskType] = None,
        categories: typing.Optional[str] = None,
        updated_since: typing.Optional[dt.datetime] = None,
        encounter_id: typing.Optional[EncounterId] = None,
        search_term: typing.Optional[str] = None,
        assigned_to_id: typing.Optional[UserId] = None,
        date_of_service_min: typing.Optional[dt.date] = None,
        date_of_service_max: typing.Optional[dt.date] = None,
        billing_provider_npi: typing.Optional[str] = None,
        sort: typing.Optional[TaskSortOptions] = None,
    ) -> TaskPage:
        """
        **This endpoint is incubating.**

        Parameters:
            - limit: typing.Optional[int]. Defaults to 100

            - page_token: typing.Optional[PageToken].

            - status: typing.Optional[TaskStatus].

            - task_type: typing.Optional[TaskType].

            - categories: typing.Optional[str]. Only return tasks with categories that match one in this comma-separated list.

            - updated_since: typing.Optional[dt.datetime]. Only return tasks updated on or after this date-time

            - encounter_id: typing.Optional[EncounterId]. Only return tasks associated with this encounter

            - search_term: typing.Optional[str]. Query tasks by encounter_id, claim_id, task_id, or external_id

            - assigned_to_id: typing.Optional[UserId]. Only return tasks assigned to this user

            - date_of_service_min: typing.Optional[dt.date]. The minimum date of service for the linked encounter

            - date_of_service_max: typing.Optional[dt.date]. The maximum date of service for the linked encounter

            - billing_provider_npi: typing.Optional[str]. The NPI of the billing provider associated with the task's claim

            - sort: typing.Optional[TaskSortOptions]. Defaults to updated_at:desc
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/tasks/v3"),
            params=remove_none_from_dict(
                {
                    "limit": limit,
                    "page_token": page_token,
                    "status": status,
                    "task_type": task_type,
                    "categories": categories,
                    "updated_since": serialize_datetime(updated_since) if updated_since is not None else None,
                    "encounter_id": jsonable_encoder(encounter_id),
                    "search_term": search_term,
                    "assigned_to_id": jsonable_encoder(assigned_to_id),
                    "date_of_service_min": str(date_of_service_min) if date_of_service_min is not None else None,
                    "date_of_service_max": str(date_of_service_max) if date_of_service_max is not None else None,
                    "billing_provider_npi": billing_provider_npi,
                    "sort": sort,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(TaskPage, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "UnprocessableEntityError":
                raise UnprocessableEntityError(
                    pydantic.parse_obj_as(UnprocessableEntityErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, task_id: TaskId) -> Task:
        """
        **This endpoint is incubating.**

        Parameters:
            - task_id: TaskId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/v3/{task_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Task, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: TaskCreateV3) -> Task:
        """
        **This endpoint is incubating.**

        Parameters:
            - request: TaskCreateV3.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/tasks/v3"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Task, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, task_id: TaskId, *, request: TaskUpdateV3) -> Task:
        """
        **This endpoint is incubating.**

        Parameters:
            - task_id: TaskId.

            - request: TaskUpdateV3.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"api/tasks/v3/{task_id}"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Task, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "EntityNotFoundError":
                raise EntityNotFoundError(
                    pydantic.parse_obj_as(EntityNotFoundErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "UnauthorizedError":
                raise UnauthorizedError(
                    pydantic.parse_obj_as(UnauthorizedErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "TaskUpdatedToDeprecatedStatusError":
                raise TaskUpdatedToDeprecatedStatusError(
                    pydantic.parse_obj_as(TaskUpdatedToDeprecatedStatusErrorType, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)