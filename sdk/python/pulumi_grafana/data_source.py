# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class DataSource(pulumi.CustomResource):
    access_mode: pulumi.Output[str]
    """
    The method by which the browser-based Grafana
    application will access the data source. The default is "proxy", which means
    that the application will make requests via a proxy endpoint on the Grafana
    server.
    """
    basic_auth_enabled: pulumi.Output[bool]
    """
    - If true, HTTP basic authentication will
    be used to make requests.
    """
    basic_auth_password: pulumi.Output[str]
    """
    The
    password to use for basic auth.
    """
    basic_auth_username: pulumi.Output[str]
    """
    The
    username to use for basic auth.
    """
    database_name: pulumi.Output[str]
    """
    The name of the
    database to use on the selected data source server.
    """
    is_default: pulumi.Output[bool]
    """
    If true, the data source will be the default
    source used by the Grafana server. Only one data source on a server can be
    the default.
    """
    json_datas: pulumi.Output[list]
    """
    The default region
    and authentication type to access the data source. `json_data` is documented
    in more detail below.
    
      * `assumeRoleArn` (`str`) - The role
        ARN to be assumed by Grafana when using the CloudWatch data source.
      * `authType` (`str`) - The authentication type
        type used to access the data source.
      * `customMetricsNamespaces` (`str`) - 
        A comma-separated list of custom namespaces to be queried by the CloudWatch
        data source.
      * `defaultRegion` (`str`)
    """
    name: pulumi.Output[str]
    """
    A unique name for the data source within the Grafana
    server.
    """
    password: pulumi.Output[str]
    """
    The password to use to
    authenticate to the data source.
    """
    secure_json_datas: pulumi.Output[list]
    """
    The access and
    secret keys required to access the data source. `secure_json_data` is
    documented in more detail below.
    
      * `accessKey` (`str`) - The access key required
        to access the data source.
      * `secretKey` (`str`) - The secret key required
        to access the data source.
    """
    type: pulumi.Output[str]
    """
    The data source type. Must be one of the data source
    keywords supported by the Grafana server.
    """
    url: pulumi.Output[str]
    """
    The URL for the data source. The type of URL required
    varies depending on the chosen data source type.
    """
    username: pulumi.Output[str]
    """
    The username to use to
    authenticate to the data source.
    """
    def __init__(__self__, resource_name, opts=None, access_mode=None, basic_auth_enabled=None, basic_auth_password=None, basic_auth_username=None, database_name=None, is_default=None, json_datas=None, name=None, password=None, secure_json_datas=None, type=None, url=None, username=None, __props__=None, __name__=None, __opts__=None):
        """
        The data source resource allows a data source to be created on a Grafana server.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_mode: The method by which the browser-based Grafana
               application will access the data source. The default is "proxy", which means
               that the application will make requests via a proxy endpoint on the Grafana
               server.
        :param pulumi.Input[bool] basic_auth_enabled: - If true, HTTP basic authentication will
               be used to make requests.
        :param pulumi.Input[str] basic_auth_password: The
               password to use for basic auth.
        :param pulumi.Input[str] basic_auth_username: The
               username to use for basic auth.
        :param pulumi.Input[str] database_name: The name of the
               database to use on the selected data source server.
        :param pulumi.Input[bool] is_default: If true, the data source will be the default
               source used by the Grafana server. Only one data source on a server can be
               the default.
        :param pulumi.Input[list] json_datas: The default region
               and authentication type to access the data source. `json_data` is documented
               in more detail below.
        :param pulumi.Input[str] name: A unique name for the data source within the Grafana
               server.
        :param pulumi.Input[str] password: The password to use to
               authenticate to the data source.
        :param pulumi.Input[list] secure_json_datas: The access and
               secret keys required to access the data source. `secure_json_data` is
               documented in more detail below.
        :param pulumi.Input[str] type: The data source type. Must be one of the data source
               keywords supported by the Grafana server.
        :param pulumi.Input[str] url: The URL for the data source. The type of URL required
               varies depending on the chosen data source type.
        :param pulumi.Input[str] username: The username to use to
               authenticate to the data source.
        
        The **json_datas** object supports the following:
        
          * `assumeRoleArn` (`pulumi.Input[str]`) - The role
            ARN to be assumed by Grafana when using the CloudWatch data source.
          * `authType` (`pulumi.Input[str]`) - The authentication type
            type used to access the data source.
          * `customMetricsNamespaces` (`pulumi.Input[str]`) - 
            A comma-separated list of custom namespaces to be queried by the CloudWatch
            data source.
          * `defaultRegion` (`pulumi.Input[str]`)
        
        The **secure_json_datas** object supports the following:
        
          * `accessKey` (`pulumi.Input[str]`) - The access key required
            to access the data source.
          * `secretKey` (`pulumi.Input[str]`) - The secret key required
            to access the data source.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-grafana/blob/master/website/docs/r/data_source.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['access_mode'] = access_mode
            __props__['basic_auth_enabled'] = basic_auth_enabled
            __props__['basic_auth_password'] = basic_auth_password
            __props__['basic_auth_username'] = basic_auth_username
            __props__['database_name'] = database_name
            __props__['is_default'] = is_default
            __props__['json_datas'] = json_datas
            __props__['name'] = name
            __props__['password'] = password
            __props__['secure_json_datas'] = secure_json_datas
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['url'] = url
            __props__['username'] = username
        super(DataSource, __self__).__init__(
            'grafana:index/dataSource:DataSource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_mode=None, basic_auth_enabled=None, basic_auth_password=None, basic_auth_username=None, database_name=None, is_default=None, json_datas=None, name=None, password=None, secure_json_datas=None, type=None, url=None, username=None):
        """
        Get an existing DataSource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_mode: The method by which the browser-based Grafana
               application will access the data source. The default is "proxy", which means
               that the application will make requests via a proxy endpoint on the Grafana
               server.
        :param pulumi.Input[bool] basic_auth_enabled: - If true, HTTP basic authentication will
               be used to make requests.
        :param pulumi.Input[str] basic_auth_password: The
               password to use for basic auth.
        :param pulumi.Input[str] basic_auth_username: The
               username to use for basic auth.
        :param pulumi.Input[str] database_name: The name of the
               database to use on the selected data source server.
        :param pulumi.Input[bool] is_default: If true, the data source will be the default
               source used by the Grafana server. Only one data source on a server can be
               the default.
        :param pulumi.Input[list] json_datas: The default region
               and authentication type to access the data source. `json_data` is documented
               in more detail below.
        :param pulumi.Input[str] name: A unique name for the data source within the Grafana
               server.
        :param pulumi.Input[str] password: The password to use to
               authenticate to the data source.
        :param pulumi.Input[list] secure_json_datas: The access and
               secret keys required to access the data source. `secure_json_data` is
               documented in more detail below.
        :param pulumi.Input[str] type: The data source type. Must be one of the data source
               keywords supported by the Grafana server.
        :param pulumi.Input[str] url: The URL for the data source. The type of URL required
               varies depending on the chosen data source type.
        :param pulumi.Input[str] username: The username to use to
               authenticate to the data source.
        
        The **json_datas** object supports the following:
        
          * `assumeRoleArn` (`pulumi.Input[str]`) - The role
            ARN to be assumed by Grafana when using the CloudWatch data source.
          * `authType` (`pulumi.Input[str]`) - The authentication type
            type used to access the data source.
          * `customMetricsNamespaces` (`pulumi.Input[str]`) - 
            A comma-separated list of custom namespaces to be queried by the CloudWatch
            data source.
          * `defaultRegion` (`pulumi.Input[str]`)
        
        The **secure_json_datas** object supports the following:
        
          * `accessKey` (`pulumi.Input[str]`) - The access key required
            to access the data source.
          * `secretKey` (`pulumi.Input[str]`) - The secret key required
            to access the data source.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-grafana/blob/master/website/docs/r/data_source.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["access_mode"] = access_mode
        __props__["basic_auth_enabled"] = basic_auth_enabled
        __props__["basic_auth_password"] = basic_auth_password
        __props__["basic_auth_username"] = basic_auth_username
        __props__["database_name"] = database_name
        __props__["is_default"] = is_default
        __props__["json_datas"] = json_datas
        __props__["name"] = name
        __props__["password"] = password
        __props__["secure_json_datas"] = secure_json_datas
        __props__["type"] = type
        __props__["url"] = url
        __props__["username"] = username
        return DataSource(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

