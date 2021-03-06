from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(2)
    
def after_scenario(context, scenario):
    if context.browser is not None:
        context.browser.quit()

