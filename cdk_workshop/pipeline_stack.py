import os
from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
    SecretValue
)

class CdkSampleStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pipeline = pipelines.CodePipeline(
            self, "Pipeline",
            pipeline_name="Ajuram-Pipeline",
            synth=pipelines.ShellStep("Synth",
                            input=pipelines.CodePipelineSource.git_hub("Ajuram-Prasanna/cdk-workshop", "master",
                                                             authentication=SecretValue.unsafe_plain_text(os.getenv("GH_TOKEN"))),
                            commands=[
                                "npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "npx cdk synth"
                            ]
                            )
        )