from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


#SEARCH_INPUT = (By.NAME, 'q')
#SEARCH_SUBMIT = (By.NAME, 'btnK')
BEST_SELLER_LINK=(By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')
@given('Open Amazon best seller page')
def Open_Amazon_best_seller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(60)

@then('Confirm {link_count} links exist')
def Confirm_5_links_exist (context, link_count ):
   all_links_count = len(context.driver.find_elements(*BEST_SELLER_LINK))
   print("all products count",all_links_count,type( all_links_count))
   print("expected links count",int(link_count),type(int(link_count)))
   assert int(link_count) ==  all_links_count, f'Expected link count {link_count}  does not match actual link count {all_links_count}'
