from constructs import Construct
from aws_cdk import (
    Stage
)
from .pipeline_stack import CdkSampleStack

class PipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = CdkSampleStack(self, 'WebService')