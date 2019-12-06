// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
	"github.com/pulumi/pulumi/sdk/go/pulumi/config"
)

// Credentials for accessing the Grafana API.
func GetAuth(ctx *pulumi.Context) string {
	return config.Get(ctx, "grafana:auth")
}

// URL of the root of the target Grafana server.
func GetUrl(ctx *pulumi.Context) string {
	return config.Get(ctx, "grafana:url")
}
