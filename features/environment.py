from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import re

def before_all(context):
    ...

def before_feature(context, feature):
    context.URL = "https://www.ebay.com"
    context.TIMEOUT = 20

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, context.TIMEOUT) #explcit wait

    # context.driver.implicitly_wait(40) # implicit wait

def after_step(context, step):
    if step.status == "failed":
# clean the filename
        step_name = re.findall(r'\w+',step.name) # ['open', 'eBay.com']
        step_name = '_'.join(step_name) # 'open_eBay.com
        context.driver.save_screenshot(f'{step_name}.png') #filename

def after_scenario(context, scenario):
    context.driver.close() # close the window
    context.driver.quit()  # close the process