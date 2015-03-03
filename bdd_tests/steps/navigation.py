from behave import *
import time

@given('I launch my browser')
def step_impl(context):
    assert context.browser is not None

@when('I navigate to "{destination_url}"')
def step_impl(context, destination_url):
    context.browser.get(destination_url)
    time.sleep(0.5)
    assert destination_url in context.browser.current_url

@then('I should see a page titled "{page_title}"')
def step_impl(context, page_title):
    assert page_title in context.browser.title
