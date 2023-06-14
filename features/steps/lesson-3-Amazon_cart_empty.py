from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

AMAZON_CART_ICON=(By.CSS_SELECTOR,"span#nav-cart-count")
EMPTY_CART_PAGE=(By.CSS_SELECTOR,"div.sc-your-amazon-cart-is-empty")

@given('Enter Amazon page')
def Enter_Amazon_page(context):
    context.driver.get('https://www.Amazon.com/')

@when('Click on cart icon')
def click_cart_icon(context):
    order_button=context.driver.find_element(*AMAZON_CART_ICON)
    context.driver.wait.until(EC.element_to_be_clickable(order_button))
    order_button.click()
@then('Your Amazon Cart empty page are shown')
def Verify_Amazon_empty_cart_page(context):
        context.driver.find_element(*EMPTY_CART_PAGE)
        #context.driver.wait.until(EC.new_window_is_opened())
