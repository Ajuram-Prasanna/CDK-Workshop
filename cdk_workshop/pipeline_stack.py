import os
from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
    SecretValue
)





def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)





class CdkSampleStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        pipeline = pipelines.CodePipeline(
            self, "Pipeline",
            pipeline_name="Ajuram-Pipeline",
            synth=pipelines.ShellStep("Synth",
                            input=pipelines.CodePipelineSource.git_hub("Ajuram-Prasanna/cdk-workshop", "main",
                                                             authentication=SecretValue.unsafe_plain_text("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")),
                            commands=[
                                "npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "npx cdk synth"
                            ]
                            )
        )