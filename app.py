#!/usr/bin/env python3

from aws_cdk import core

from pipeline_cdk.pipeline_cdk_stack import PipelineCdkStack


app = core.App()
PipelineCdkStack(app, "pipeline-cdk")

app.synth()
