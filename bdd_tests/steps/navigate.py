import time

@when('I open my browser')
def step_impl(context):
    assert context.browser is not None

@when('navigate to "{website_url}"')
@when('go to "{website_url}"')
def step_impl(context, website_url):
    context.browser.get(website_url)
    time.sleep(.5)
    assert website_url in context.browser.current_url

@then('I will see a page titled "{title}"')
@then('I will see a page named "{title}"')
def step_impl(context, title):
    assert title in context.browser.title
    
    