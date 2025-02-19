from constructs import Construct
from aws_cdk import (
    Stack,
    CfnOutput,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

def __init__(self, scope: Construct, id: str, **kwargs):
    super().__init__(scope, id, **kwargs)

    # Defines an AWS Lambda resource
    my_lambda = _lambda.Function(
        self,
        "HelloHandler",
        function_name="cdk-lambda",
        runtime=_lambda.Runtime.PYTHON_3_7,
        code=_lambda.Code.from_asset("lambda"),
        handler="hello.handler",
    )

    gateway = apigw.LambdaRestApi(
        self,
        "Endpoint",
        handler=my_lambda,
    )