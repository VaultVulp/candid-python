# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.remove_none_from_dict import remove_none_from_dict
from ....commons.errors.http_request_validations_error import HttpRequestValidationsError
from ....commons.types.error_message import ErrorMessage
from ....commons.types.request_validation_error import RequestValidationError
from .errors.export_date_too_early_error import ExportDateTooEarlyError
from .errors.export_files_unavailable_error import ExportFilesUnavailableError
from .errors.export_not_yet_available_error import ExportNotYetAvailableError
from .errors.missing_daily_incremental_export_file_error import MissingDailyIncrementalExportFileError
from .types.get_exports_response import GetExportsResponse


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_exports(self, *, start_date: dt.date, end_date: dt.date) -> GetExportsResponse:
        """
        Retrieve CSV-formatted reports on claim submissions and outcomes. This endpoint returns Export objects that contain an
        authenticated URL to a customer's reports with a 2min TTL. The schema for the CSV export can be found [here](https://app.joincandidhealth.com/files/exports_schema.csv).

        **Schema changes:** Changing column order, removing columns, or changing the name of a column is considered a
        [Breaking Change](../../../api-principles/breaking-changes). Adding new columns to the end of the Exports file is not considered a
        Breaking Change and happens periodically. For this reason, it is important that any downstream automation or processes built on top
        of Candid Health's export files be resilient to the addition of new columns at the end of the file.

        **SLA guarantees:** Files for a given date are guaranteed to be available after 3 business days. For example, Friday's file will be
        available by Wednesday at the latest. If file generation is still in progress upon request before 3 business days have passed, the
        caller will receive a 422 response. If the file has already been generated, it will be served. Please email
        support@joincandidhealth.com with any data requests outside of these stated guarantees.

        Parameters:
            - start_date: dt.date. Beginning date of claim versions returned in the export, ISO 8601 date e.g. 2019-08-24.
                                   Must be at least 1 calendar day in the past. Cannot be earlier than 2022-10-07.

            - end_date: dt.date. Ending date of claim versions returned in the export, ISO 8601 date; e.g. 2019-08-24.
                                 Must be within 30 days of start_date.

        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/exports/v3"),
            params=remove_none_from_dict({"start_date": str(start_date), "end_date": str(end_date)}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExportsResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationsError":
                raise HttpRequestValidationsError(
                    pydantic.parse_obj_as(typing.List[RequestValidationError], _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "ExportFilesUnavailableError":
                raise ExportFilesUnavailableError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "MissingDailyIncrementalExportFileError":
                raise MissingDailyIncrementalExportFileError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "ExportNotYetAvailableError":
                raise ExportNotYetAvailableError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "ExportDateTooEarlyError":
                raise ExportDateTooEarlyError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_exports(self, *, start_date: dt.date, end_date: dt.date) -> GetExportsResponse:
        """
        Retrieve CSV-formatted reports on claim submissions and outcomes. This endpoint returns Export objects that contain an
        authenticated URL to a customer's reports with a 2min TTL. The schema for the CSV export can be found [here](https://app.joincandidhealth.com/files/exports_schema.csv).

        **Schema changes:** Changing column order, removing columns, or changing the name of a column is considered a
        [Breaking Change](../../../api-principles/breaking-changes). Adding new columns to the end of the Exports file is not considered a
        Breaking Change and happens periodically. For this reason, it is important that any downstream automation or processes built on top
        of Candid Health's export files be resilient to the addition of new columns at the end of the file.

        **SLA guarantees:** Files for a given date are guaranteed to be available after 3 business days. For example, Friday's file will be
        available by Wednesday at the latest. If file generation is still in progress upon request before 3 business days have passed, the
        caller will receive a 422 response. If the file has already been generated, it will be served. Please email
        support@joincandidhealth.com with any data requests outside of these stated guarantees.

        Parameters:
            - start_date: dt.date. Beginning date of claim versions returned in the export, ISO 8601 date e.g. 2019-08-24.
                                   Must be at least 1 calendar day in the past. Cannot be earlier than 2022-10-07.

            - end_date: dt.date. Ending date of claim versions returned in the export, ISO 8601 date; e.g. 2019-08-24.
                                 Must be within 30 days of start_date.

        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/exports/v3"),
            params=remove_none_from_dict({"start_date": str(start_date), "end_date": str(end_date)}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetExportsResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "HttpRequestValidationsError":
                raise HttpRequestValidationsError(
                    pydantic.parse_obj_as(typing.List[RequestValidationError], _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "ExportFilesUnavailableError":
                raise ExportFilesUnavailableError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "MissingDailyIncrementalExportFileError":
                raise MissingDailyIncrementalExportFileError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "ExportNotYetAvailableError":
                raise ExportNotYetAvailableError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
            if _response_json["errorName"] == "ExportDateTooEarlyError":
                raise ExportDateTooEarlyError(
                    pydantic.parse_obj_as(ErrorMessage, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)
