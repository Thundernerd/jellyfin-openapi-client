# openapi_client.PluginsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_plugin**](PluginsApi.md#disable_plugin) | **POST** /Plugins/{pluginId}/{version}/Disable | Disable a plugin.
[**enable_plugin**](PluginsApi.md#enable_plugin) | **POST** /Plugins/{pluginId}/{version}/Enable | Enables a disabled plugin.
[**get_plugin_configuration**](PluginsApi.md#get_plugin_configuration) | **GET** /Plugins/{pluginId}/Configuration | Gets plugin configuration.
[**get_plugin_image**](PluginsApi.md#get_plugin_image) | **GET** /Plugins/{pluginId}/{version}/Image | Gets a plugin&#39;s image.
[**get_plugin_manifest**](PluginsApi.md#get_plugin_manifest) | **POST** /Plugins/{pluginId}/Manifest | Gets a plugin&#39;s manifest.
[**get_plugins**](PluginsApi.md#get_plugins) | **GET** /Plugins | Gets a list of currently installed plugins.
[**uninstall_plugin**](PluginsApi.md#uninstall_plugin) | **DELETE** /Plugins/{pluginId} | Uninstalls a plugin.
[**uninstall_plugin_by_version**](PluginsApi.md#uninstall_plugin_by_version) | **DELETE** /Plugins/{pluginId}/{version} | Uninstalls a plugin by version.
[**update_plugin_configuration**](PluginsApi.md#update_plugin_configuration) | **POST** /Plugins/{pluginId}/Configuration | Updates plugin configuration.


# **disable_plugin**
> disable_plugin(plugin_id, version)

Disable a plugin.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.
    version = 'version_example' # str | Plugin version.

    try:
        # Disable a plugin.
        api_instance.disable_plugin(plugin_id, version)
    except Exception as e:
        print("Exception when calling PluginsApi->disable_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 
 **version** | **str**| Plugin version. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Plugin disabled. |  -  |
**404** | Plugin not found. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_plugin**
> enable_plugin(plugin_id, version)

Enables a disabled plugin.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.
    version = 'version_example' # str | Plugin version.

    try:
        # Enables a disabled plugin.
        api_instance.enable_plugin(plugin_id, version)
    except Exception as e:
        print("Exception when calling PluginsApi->enable_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 
 **version** | **str**| Plugin version. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Plugin enabled. |  -  |
**404** | Plugin not found. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_configuration**
> object get_plugin_configuration(plugin_id)

Gets plugin configuration.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.

    try:
        # Gets plugin configuration.
        api_response = api_instance.get_plugin_configuration(plugin_id)
        print("The response of PluginsApi->get_plugin_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 

### Return type

**object**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin configuration returned. |  -  |
**404** | Plugin not found or plugin configuration not found. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_image**
> bytearray get_plugin_image(plugin_id, version)

Gets a plugin's image.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.
    version = 'version_example' # str | Plugin version.

    try:
        # Gets a plugin's image.
        api_response = api_instance.get_plugin_image(plugin_id, version)
        print("The response of PluginsApi->get_plugin_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 
 **version** | **str**| Plugin version. | 

### Return type

**bytearray**

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*, application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plugin image returned. |  -  |
**404** | Not Found |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugin_manifest**
> get_plugin_manifest(plugin_id)

Gets a plugin's manifest.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.

    try:
        # Gets a plugin's manifest.
        api_instance.get_plugin_manifest(plugin_id)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugin_manifest: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Plugin manifest returned. |  -  |
**404** | Plugin not found. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins**
> List[PluginInfo] get_plugins()

Gets a list of currently installed plugins.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.models.plugin_info import PluginInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)

    try:
        # Gets a list of currently installed plugins.
        api_response = api_instance.get_plugins()
        print("The response of PluginsApi->get_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PluginsApi->get_plugins: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PluginInfo]**](PluginInfo.md)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installed plugins returned. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_plugin**
> uninstall_plugin(plugin_id)

Uninstalls a plugin.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.

    try:
        # Uninstalls a plugin.
        api_instance.uninstall_plugin(plugin_id)
    except Exception as e:
        print("Exception when calling PluginsApi->uninstall_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Plugin uninstalled. |  -  |
**404** | Plugin not found. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uninstall_plugin_by_version**
> uninstall_plugin_by_version(plugin_id, version)

Uninstalls a plugin by version.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.
    version = 'version_example' # str | Plugin version.

    try:
        # Uninstalls a plugin by version.
        api_instance.uninstall_plugin_by_version(plugin_id, version)
    except Exception as e:
        print("Exception when calling PluginsApi->uninstall_plugin_by_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 
 **version** | **str**| Plugin version. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Plugin uninstalled. |  -  |
**404** | Plugin not found. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plugin_configuration**
> update_plugin_configuration(plugin_id)

Updates plugin configuration.

Accepts plugin configuration as JSON body.

### Example

* Api Key Authentication (CustomAuthentication):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: CustomAuthentication
configuration.api_key['CustomAuthentication'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['CustomAuthentication'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PluginsApi(api_client)
    plugin_id = 'plugin_id_example' # str | Plugin id.

    try:
        # Updates plugin configuration.
        api_instance.update_plugin_configuration(plugin_id)
    except Exception as e:
        print("Exception when calling PluginsApi->update_plugin_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plugin_id** | **str**| Plugin id. | 

### Return type

void (empty response body)

### Authorization

[CustomAuthentication](../README.md#CustomAuthentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; profile="CamelCase", application/json; profile="PascalCase", text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Plugin configuration updated. |  -  |
**404** | Plugin not found or plugin does not have configuration. |  -  |
**503** | The server is currently starting or is temporarly not available. |  * Retry-After - A hint for when to retry the operation in full seconds. <br>  * Message - A short plain-text reason why the server is not available. <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

