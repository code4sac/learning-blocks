import json

import pytest
import pandas as pd

from learning_blocks_api import app
from learning_blocks_api.demo_aries_api import demo_aries_api


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {
            "api_type": "demo",
            "school_id": "994",
            "student_id": "99400002",
            "api_key": "477abe9e7d27439681d62f4e0de1f5e1"
        },
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


def test_lambda_handler(apigw_event):
    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"


def test_aries_demo_current_grades(apigw_event):
    ret = app.lambda_handler(apigw_event, "")
    assert ret["statusCode"] == 200
    query_string_parameters = apigw_event["queryStringParameters"]
    school_id = query_string_parameters["school_id"]
    student_id = query_string_parameters["student_id"]
    api_key = query_string_parameters["api_key"]
    assert query_string_parameters["api_type"] == "demo"
    assert query_string_parameters["school_id"] == "994"
    assert query_string_parameters["student_id"] == "99400002"
    assert query_string_parameters["api_key"] == "477abe9e7d27439681d62f4e0de1f5e1"
    api = demo_aries_api(school_id, student_id, api_key)
    csv_data = api.get_current_grades()
    assert isinstance(csv_data, list)
    # Test creating a csv file from JSON object returned from Aries API
    # df = pd.read_csv(csv_data)
    # headers = list(df.columns)
    # assert headers[0] == "StudentID"
    # assert headers[1] == "StudentReportCardCourses"


