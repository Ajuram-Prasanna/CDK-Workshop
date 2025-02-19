from constructs import Construct
from aws_cdk import (
    Stack,
    CfnOutput,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

def __init__(self, scope: Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)
