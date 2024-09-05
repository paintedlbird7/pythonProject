from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



# 
# @when(u'open orange hrm homepage')
# def openHomePage(context):
#     context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')



@step("Navigate to orangehrm.com")
def orangehrm_url(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.driver.maximize_window()
    sleep(10)

@step("you verify logo present on page")
def verify_logo(context):
    logo = context.driver.find_element(By.XPATH,"//div[@class ='orangehrm-login-logo']/img[@alt='orangehrm-logo']")
    assert logo.is_displayed() is True

# @then(u'close browser')
# def closeBrowser(context):
#     context.driver.close()







