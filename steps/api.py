from behave import given, when, then


@given(u'set http request url "{request_url}"')
def step_impl(context, request_url):
    pass


@given(u'set http request header "{api_key}" equal "{api_value}"')
def step_impl(context, api_key, api_value):
    pass


@when(u'send GET http request')
def step_impl(context):
    pass


@then(u'response http request code should be "{response_status_code}"')
def step_impl(context, response_status_code):
    pass


