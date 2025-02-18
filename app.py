#!/usr/bin/env python3

import aws_cdk as cdk
from cdk_workshop.pipeline_stack import CdkSampleStack

app = cdk.App()
CdkSampleStack(app, "CdkSampleStack")

app.synth()