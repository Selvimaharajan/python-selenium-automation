from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')
CHOOSE_EACH_COLOR=(By.CSS_SELECTOR,"#variation_color_name li")
SELECT_YOUR_PRODUCT_COLOR=(By.CSS_SELECTOR,"#variation_color_name .selection")



@given('get into amazon page')
def get_into_amazon(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')
@when('choose a each product color')
def choose_a_each_product_color(context):
    all_product=context.driver.find_elements(*CHOOSE_EACH_COLOR)
    sleep(1)
    for product in all_product:
     product.click()
     product_color=context.driver.find_element(*SELECT_YOUR_PRODUCT_COLOR).text
     print (product_color)

