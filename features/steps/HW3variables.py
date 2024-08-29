from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
#
@step("goto {daily_deals}")
def click_deals(context, daily_deals):
    daily_deals = context.driver.find_element('xpath', f"//*[contains(@class, 'gh-') and text() = '{daily_deals}']")
    daily_deals.click()
    print("Clicked on the link  Daily Deals")


@step('go to {anything}')
def click_sell(context, anything):
    # sell = context.driver.find_element('xpath', f"//a[@class, 'gh-p') and text() = {Sell}]")
    btn = context.driver.find_element('xpath', f"//*[contains(@class, 'gh') and text() = '{anything}']")
    btn.click()
    sleep(4)
    print("go to  empty_box")

@step("check landing on {title}")
def check_landing(context, title):
    expected_title = context.driver.title
    assert expected_title == title



#
# @step('Click on the link {Watchlist}')
# def click_deals(context, Watchlist):
#     watchlist = context.driver.find_element('xpath', f"//*[contains(@class, 'gh-eb-li-a gh-rvi-menu') and text() = '{Watchlist}']")
#     watchlist.click()
#     sleep(4)
#     print("Click on the link My ebay")
#
# #MyEbay    "//a[@class='gh-eb-li-a gh-rvi-menu' and text()='My eBay']"
# @step('Click on the link {MyeBay}')
# def click_deals(context, MyeBay):
#     myeBay = context.driver.find_element('xpath', f"//*[contains(@class, 'gh-eb-li-a gh-rvi-menu') and text() = '{MyeBay}']")
#     myeBay.click()
#     sleep(4)
#     print("Click on the link My ebay")
#
# #Alert     "//i[@class='gh-sprRetina' and text()='Notification']"
# @step('Click on the link {Notification}')
# def click_deals(context, Notification):
#     notification = context.driver.find_element('xpath', f"//*[contains(@class, 'gh-sprRetina') and text() = '{Notification}']")
#     notification.click()
#     sleep(4)
#     print("Click on the link My ebay")
#
#
#


# * any tag will do
# "//*[@class = 'gh-p' and text() = ' Sell']"
# "//*[contains@class = 'gh-' and text() = '{empty_box}']"
# "//*[contains@class = 'gh-' and text() = '{empty_box}']"
# "//*[contains@class = 'gh-' and text() = '{empty_box}']"
# "//*[contains@class = 'gh-' and @title = '{empty_box}']"
# "//*[contains@class = 'gh-' and @alt = '{empty_box}']"





# @step('open eBay.com')
# def open_ebay(context):
#     context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     context.driver.get('https://ebay.com')
#

# @step("you verify logo present on page")
# def verify_logo(context):
#     logo = context.driver.find_element(By.XPATH,"//div[@class ='orangehrm-login-logo']/img[@alt='orangehrm-logo']")
#     assert logo.is_displayed() is True
#

# @step('open ebay.com')
# def open_ebay(context):
#     context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     context.driver.get('https://ebay.com')