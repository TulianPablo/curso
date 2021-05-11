from behave import given, when, then
import request


@given(u'set http request url "{request_url}"')
def step_impl(context, request_url):
    context.request_url=request_url
    context.request_header={}
    pass


@given(u'set http request header "{api_key}" equal "{api_value}"')
def step_impl(context, api_key, api_value):
    context.request_header[api_key] = api_value
    pass


@when(u'send GET http request')
def step_impl(context):
    context.response=request.get(url=context.request_url, headers=context.request_header)
    pass


@then(u'response http request code should be "{response_status_code}"')
def step_impl(context, response_status_code):
    assert_that(context.response_status_code,equal_to(int(response_status_code)))
    pass


