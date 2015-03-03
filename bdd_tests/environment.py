from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.support.ui import WebDriverWait

def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)
    
def after_scenario(context, scenario):
    context.browser.quit()
=======


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(2)
    
def after_scenario(context, scenario):
    if context.browser is not None:
        context.browser.quit()

>>>>>>> 402b0e6ff245198c5666ff8d53b1e477cf27f88a
