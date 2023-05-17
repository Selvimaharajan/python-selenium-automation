from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&showRmrMe=1&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&pageId=webcs-yourorder&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcss%2Forder-history%3Fie%3DUTF8%26ref_%3Dnav_orders_first&prevRID=T2E06K386WCFZZQPA1V8&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(2)
driver.find_element(By.CSS_SELECTOR,'i.a-icon')
sleep(2)
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')
sleep(2)
driver.find_element(By.CSS_SELECTOR,'input#ap_customer_name')
sleep(2)
driver.find_element(By.ID,'ap_email')
sleep(2)
driver.find_element(By.ID,'ap_password')
sleep(2)
driver.find_element(By.ID,'ap_password_check')
sleep(2)
driver.find_element(By.CSS_SELECTOR,'input#continue')
sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href*='ap_register_notification_condition_of_use']")
sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href*='ap_register_notification_privacy_notice']")
sleep(2)
driver.find_element(By.CSS_SELECTOR,"a[href*='max_auth_age']")
sleep(2)