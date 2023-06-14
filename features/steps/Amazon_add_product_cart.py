from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')
SEARCH_PRODUCT=(By.CSS_SELECTOR,'input#twotabsearchtextbox')
SEARCH_ICON=(By.CSS_SELECTOR,'input#nav-search-submit-button')
ALL_PRODUCT=(By.XPATH,"//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
ADD_TO_CART=(By.CSS_SELECTOR, 'input#add-to-cart-button')
CART_ICON=(By.CSS_SELECTOR,'span#nav-cart-count')
@given('Goto Amazon page')
def Goto_Amazon_page (context):
    context.driver.get('https://www.amazon.com/')
@when('enter the product {search_word} in the search field')
def product_search(context, search_word):
    search = context.driver.find_element(*SEARCH_PRODUCT)
    search.clear()
    search.send_keys(search_word)


@when('enter on search icon')
def click_search_icon(context):
        context.driver.find_element(*SEARCH_ICON).click()
        sleep(1)
@then('choose your product')
def choose_your_product(context):
        all_Products = context.driver.find_elements(*ALL_PRODUCT)
        sleep(1)
        all_Products[0].click()
@then('click add to cart icon')
def click_add_to_cart_icon (context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(1)


@then('confirm that selected product in the cart')
def confirm_that_selected_product_in_the_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(1)
