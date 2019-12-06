// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";

export interface DataSourceJsonData {
    /**
     * The role
     * ARN to be assumed by Grafana when using the CloudWatch data source.
     */
    assumeRoleArn?: pulumi.Input<string>;
    /**
     * The authentication type
     * type used to access the data source.
     */
    authType: pulumi.Input<string>;
    /**
     * 
     * A comma-separated list of custom namespaces to be queried by the CloudWatch
     * data source.
     */
    customMetricsNamespaces?: pulumi.Input<string>;
    defaultRegion: pulumi.Input<string>;
}

export interface DataSourceSecureJsonData {
    /**
     * The access key required
     * to access the data source.
     */
    accessKey: pulumi.Input<string>;
    /**
     * The secret key required
     * to access the data source.
     */
    secretKey: pulumi.Input<string>;
}
