from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

AMAZON_CART_ICON=(By.CSS_SELECTOR,"span#nav-cart-count")
EMPTY_CART_PAGE=(By.CSS_SELECTOR,"div.sc-your-amazon-cart-is-empty")

@given('Enter Amazon page')
def Enter_Amazon_page(context):
    context.driver.get('https://www.Amazon.com/')

@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*AMAZON_CART_ICON).click()
    sleep(1)

@then('Your Amazon Cart empty page are shown')
def Verify_Amazon_empty_cart_page(context):
        context.driver.find_element(*EMPTY_CART_PAGE).click()
        sleep(1)
