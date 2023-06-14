from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


Click_Return_Order = (By.CSS_SELECTOR,"a[href*='nav_or']")
Signin_Click = (By.CSS_SELECTOR, "form[name='signIn']")
Email_exist=(By.CSS_SELECTOR,'input#ap_email')



@given('Open Amazon page')
def open_Amazon(context):
    context.driver.get('https://www.Amazon.com/')

@when('Click on Return and order icon')
def Click_Return_Order_icon(context):
        Return_Order_button= context.driver.find_element(*Click_Return_Order)
        Return_Order_button.click()

@then('Signin page is open')
def Verify_Signin_page(context):
    context.driver.find_element(*Signin_Click)



@then('{search_word} header is visible')
def Signin_header_is_visible(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'

@then('email field is exist')
def email_field_is_exist(context):
    context.driver.find_element(*Email_exist)
