from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)
    
def after_scenario(context, scenario):
    context.browser.quit()