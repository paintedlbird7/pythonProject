# from lib2to3.fixes.fix_input import context

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import re

def before_all(context):
    ...

def before_feature(context, feature):
    context.URL = "https://ebay.com"

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()

# def before_step():
#     ...
#
def after_step(context, step):
    if step.status == "failed":
# clean the filename
        step_name = re.findall(r'\w+',step.name)
        step_name = '_'.join(step_name)
        context.driver.save_screenshot(f'{step_name}.png')

def after_scenario(context, scenario):
    context.driver.close() # close the window
    context.driver.quit()  # close the process

















