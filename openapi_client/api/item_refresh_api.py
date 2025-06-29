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

from pydantic import Field, StrictBool, StrictStr
from typing import Optional
from typing_extensions import Annotated

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class ItemRefreshApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def refresh_item(
        self,
        item_id: Annotated[StrictStr, Field(description="Item id.")],
        metadata_refresh_mode: Annotated[Optional[StrictStr], Field(description="(Optional) Specifies the metadata refresh mode.")] = None,
        image_refresh_mode: Annotated[Optional[StrictStr], Field(description="(Optional) Specifies the image refresh mode.")] = None,
        replace_all_metadata: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.")] = None,
        replace_all_images: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.")] = None,
        regenerate_trickplay: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh.")] = None,
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
    ) -> None:
        """Refreshes metadata for an item.


        :param item_id: Item id. (required)
        :type item_id: str
        :param metadata_refresh_mode: (Optional) Specifies the metadata refresh mode.
        :type metadata_refresh_mode: MetadataRefreshMode
        :param image_refresh_mode: (Optional) Specifies the image refresh mode.
        :type image_refresh_mode: MetadataRefreshMode
        :param replace_all_metadata: (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.
        :type replace_all_metadata: bool
        :param replace_all_images: (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.
        :type replace_all_images: bool
        :param regenerate_trickplay: (Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh.
        :type regenerate_trickplay: bool
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

        _param = self._refresh_item_serialize(
            item_id=item_id,
            metadata_refresh_mode=metadata_refresh_mode,
            image_refresh_mode=image_refresh_mode,
            replace_all_metadata=replace_all_metadata,
            replace_all_images=replace_all_images,
            regenerate_trickplay=regenerate_trickplay,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '404': "ProblemDetails",
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
    def refresh_item_with_http_info(
        self,
        item_id: Annotated[StrictStr, Field(description="Item id.")],
        metadata_refresh_mode: Annotated[Optional[StrictStr], Field(description="(Optional) Specifies the metadata refresh mode.")] = None,
        image_refresh_mode: Annotated[Optional[StrictStr], Field(description="(Optional) Specifies the image refresh mode.")] = None,
        replace_all_metadata: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.")] = None,
        replace_all_images: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.")] = None,
        regenerate_trickplay: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh.")] = None,
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
    ) -> ApiResponse[None]:
        """Refreshes metadata for an item.


        :param item_id: Item id. (required)
        :type item_id: str
        :param metadata_refresh_mode: (Optional) Specifies the metadata refresh mode.
        :type metadata_refresh_mode: MetadataRefreshMode
        :param image_refresh_mode: (Optional) Specifies the image refresh mode.
        :type image_refresh_mode: MetadataRefreshMode
        :param replace_all_metadata: (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.
        :type replace_all_metadata: bool
        :param replace_all_images: (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.
        :type replace_all_images: bool
        :param regenerate_trickplay: (Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh.
        :type regenerate_trickplay: bool
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

        _param = self._refresh_item_serialize(
            item_id=item_id,
            metadata_refresh_mode=metadata_refresh_mode,
            image_refresh_mode=image_refresh_mode,
            replace_all_metadata=replace_all_metadata,
            replace_all_images=replace_all_images,
            regenerate_trickplay=regenerate_trickplay,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '404': "ProblemDetails",
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
    def refresh_item_without_preload_content(
        self,
        item_id: Annotated[StrictStr, Field(description="Item id.")],
        metadata_refresh_mode: Annotated[Optional[StrictStr], Field(description="(Optional) Specifies the metadata refresh mode.")] = None,
        image_refresh_mode: Annotated[Optional[StrictStr], Field(description="(Optional) Specifies the image refresh mode.")] = None,
        replace_all_metadata: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.")] = None,
        replace_all_images: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.")] = None,
        regenerate_trickplay: Annotated[Optional[StrictBool], Field(description="(Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh.")] = None,
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
        """Refreshes metadata for an item.


        :param item_id: Item id. (required)
        :type item_id: str
        :param metadata_refresh_mode: (Optional) Specifies the metadata refresh mode.
        :type metadata_refresh_mode: MetadataRefreshMode
        :param image_refresh_mode: (Optional) Specifies the image refresh mode.
        :type image_refresh_mode: MetadataRefreshMode
        :param replace_all_metadata: (Optional) Determines if metadata should be replaced. Only applicable if mode is FullRefresh.
        :type replace_all_metadata: bool
        :param replace_all_images: (Optional) Determines if images should be replaced. Only applicable if mode is FullRefresh.
        :type replace_all_images: bool
        :param regenerate_trickplay: (Optional) Determines if trickplay images should be replaced. Only applicable if mode is FullRefresh.
        :type regenerate_trickplay: bool
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

        _param = self._refresh_item_serialize(
            item_id=item_id,
            metadata_refresh_mode=metadata_refresh_mode,
            image_refresh_mode=image_refresh_mode,
            replace_all_metadata=replace_all_metadata,
            replace_all_images=replace_all_images,
            regenerate_trickplay=regenerate_trickplay,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '404': "ProblemDetails",
            '503': None,
            '401': None,
            '403': None,
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _refresh_item_serialize(
        self,
        item_id,
        metadata_refresh_mode,
        image_refresh_mode,
        replace_all_metadata,
        replace_all_images,
        regenerate_trickplay,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
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
        if item_id is not None:
            _path_params['itemId'] = item_id
        # process the query parameters
        if metadata_refresh_mode is not None:
            
            _query_params.append(('metadataRefreshMode', metadata_refresh_mode.value))
            
        if image_refresh_mode is not None:
            
            _query_params.append(('imageRefreshMode', image_refresh_mode.value))
            
        if replace_all_metadata is not None:
            
            _query_params.append(('replaceAllMetadata', replace_all_metadata))
            
        if replace_all_images is not None:
            
            _query_params.append(('replaceAllImages', replace_all_images))
            
        if regenerate_trickplay is not None:
            
            _query_params.append(('regenerateTrickplay', regenerate_trickplay))
            
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
            method='POST',
            resource_path='/Items/{itemId}/Refresh',
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


