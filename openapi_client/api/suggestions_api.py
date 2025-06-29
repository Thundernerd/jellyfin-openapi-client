# coding: utf-8

"""
    Jellyfin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 10.11.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from openapi_client.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_client.models.base_item_kind import BaseItemKind
from openapi_client.models.media_type import MediaType

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class SuggestionsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_suggestions(
        self,
        user_id: Annotated[Optional[StrictStr], Field(description="The user id.")] = None,
        media_type: Annotated[Optional[List[MediaType]], Field(description="The media types.")] = None,
        type: Annotated[Optional[List[BaseItemKind]], Field(description="The type.")] = None,
        start_index: Annotated[Optional[StrictInt], Field(description="Optional. The start index.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Optional. The limit.")] = None,
        enable_total_record_count: Annotated[Optional[StrictBool], Field(description="Whether to enable the total record count.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BaseItemDtoQueryResult:
        """Gets suggestions.


        :param user_id: The user id.
        :type user_id: str
        :param media_type: The media types.
        :type media_type: List[MediaType]
        :param type: The type.
        :type type: List[BaseItemKind]
        :param start_index: Optional. The start index.
        :type start_index: int
        :param limit: Optional. The limit.
        :type limit: int
        :param enable_total_record_count: Whether to enable the total record count.
        :type enable_total_record_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_suggestions_serialize(
            user_id=user_id,
            media_type=media_type,
            type=type,
            start_index=start_index,
            limit=limit,
            enable_total_record_count=enable_total_record_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BaseItemDtoQueryResult",
            '503': None,
            '401': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_suggestions_with_http_info(
        self,
        user_id: Annotated[Optional[StrictStr], Field(description="The user id.")] = None,
        media_type: Annotated[Optional[List[MediaType]], Field(description="The media types.")] = None,
        type: Annotated[Optional[List[BaseItemKind]], Field(description="The type.")] = None,
        start_index: Annotated[Optional[StrictInt], Field(description="Optional. The start index.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Optional. The limit.")] = None,
        enable_total_record_count: Annotated[Optional[StrictBool], Field(description="Whether to enable the total record count.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[BaseItemDtoQueryResult]:
        """Gets suggestions.


        :param user_id: The user id.
        :type user_id: str
        :param media_type: The media types.
        :type media_type: List[MediaType]
        :param type: The type.
        :type type: List[BaseItemKind]
        :param start_index: Optional. The start index.
        :type start_index: int
        :param limit: Optional. The limit.
        :type limit: int
        :param enable_total_record_count: Whether to enable the total record count.
        :type enable_total_record_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_suggestions_serialize(
            user_id=user_id,
            media_type=media_type,
            type=type,
            start_index=start_index,
            limit=limit,
            enable_total_record_count=enable_total_record_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BaseItemDtoQueryResult",
            '503': None,
            '401': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_suggestions_without_preload_content(
        self,
        user_id: Annotated[Optional[StrictStr], Field(description="The user id.")] = None,
        media_type: Annotated[Optional[List[MediaType]], Field(description="The media types.")] = None,
        type: Annotated[Optional[List[BaseItemKind]], Field(description="The type.")] = None,
        start_index: Annotated[Optional[StrictInt], Field(description="Optional. The start index.")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="Optional. The limit.")] = None,
        enable_total_record_count: Annotated[Optional[StrictBool], Field(description="Whether to enable the total record count.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Gets suggestions.


        :param user_id: The user id.
        :type user_id: str
        :param media_type: The media types.
        :type media_type: List[MediaType]
        :param type: The type.
        :type type: List[BaseItemKind]
        :param start_index: Optional. The start index.
        :type start_index: int
        :param limit: Optional. The limit.
        :type limit: int
        :param enable_total_record_count: Whether to enable the total record count.
        :type enable_total_record_count: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_suggestions_serialize(
            user_id=user_id,
            media_type=media_type,
            type=type,
            start_index=start_index,
            limit=limit,
            enable_total_record_count=enable_total_record_count,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BaseItemDtoQueryResult",
            '503': None,
            '401': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_suggestions_serialize(
        self,
        user_id,
        media_type,
        type,
        start_index,
        limit,
        enable_total_record_count,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'mediaType': 'multi',
            'type': 'multi',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if user_id is not None:
            
            _query_params.append(('userId', user_id))
            
        if media_type is not None:
            
            _query_params.append(('mediaType', media_type))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if start_index is not None:
            
            _query_params.append(('startIndex', start_index))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if enable_total_record_count is not None:
            
            _query_params.append(('enableTotalRecordCount', enable_total_record_count))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json', 
                    'application/json; profile="CamelCase"', 
                    'application/json; profile="PascalCase"', 
                    'text/html'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'CustomAuthentication'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/Items/Suggestions',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


