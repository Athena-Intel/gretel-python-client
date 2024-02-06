# coding: utf-8

"""
    

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import re  # noqa: F401
import warnings

from typing import Optional

from pydantic import conlist, StrictBool, StrictStr, validate_arguments, ValidationError
from typing_extensions import Annotated

from gretel_client.rest_v1.api_client import ApiClient
from gretel_client.rest_v1.api_response import ApiResponse
from gretel_client.rest_v1.exceptions import ApiTypeError, ApiValueError  # noqa: F401
from gretel_client.rest_v1.models.get_cluster_response import GetClusterResponse
from gretel_client.rest_v1.models.list_clusters_response import ListClustersResponse


class ClustersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_cluster(
        self, cluster_id: StrictStr, **kwargs
    ) -> GetClusterResponse:  # noqa: E501
        """get_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cluster(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetClusterResponse
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the get_cluster_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.get_cluster_with_http_info(cluster_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cluster_with_http_info(
        self, cluster_id: StrictStr, **kwargs
    ) -> ApiResponse:  # noqa: E501
        """get_cluster  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cluster_with_http_info(cluster_id, async_req=True)
        >>> result = thread.get()

        :param cluster_id: (required)
        :type cluster_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetClusterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["cluster_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cluster" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["cluster_id"]:
            _path_params["cluster_id"] = _params["cluster_id"]

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            "200": "GetClusterResponse",
        }

        return self.api_client.call_api(
            "/v1/clusters/{cluster_id}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def list_clusters(
        self,
        owned_only: Optional[StrictBool] = None,
        expand: Optional[conlist(StrictStr)] = None,
        **kwargs,
    ) -> ListClustersResponse:  # noqa: E501
        """list_clusters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_clusters(owned_only, expand, async_req=True)
        >>> result = thread.get()

        :param owned_only:
        :type owned_only: bool
        :param expand:
        :type expand: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListClustersResponse
        """
        kwargs["_return_http_data_only"] = True
        if "_preload_content" in kwargs:
            raise ValueError(
                "Error! Please call the list_clusters_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"
            )
        return self.list_clusters_with_http_info(
            owned_only, expand, **kwargs
        )  # noqa: E501

    @validate_arguments
    def list_clusters_with_http_info(
        self,
        owned_only: Optional[StrictBool] = None,
        expand: Optional[conlist(StrictStr)] = None,
        **kwargs,
    ) -> ApiResponse:  # noqa: E501
        """list_clusters  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_clusters_with_http_info(owned_only, expand, async_req=True)
        >>> result = thread.get()

        :param owned_only:
        :type owned_only: bool
        :param expand:
        :type expand: List[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListClustersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["owned_only", "expand"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_clusters" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("owned_only") is not None:  # noqa: E501
            _query_params.append(("owned_only", _params["owned_only"]))

        if _params.get("expand") is not None:  # noqa: E501
            _query_params.append(("expand", _params["expand"]))
            _collection_formats["expand"] = "multi"

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            "200": "ListClustersResponse",
        }

        return self.api_client.call_api(
            "/v1/clusters",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
