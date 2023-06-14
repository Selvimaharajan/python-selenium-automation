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
driver.get('https://www.amazon.com/')

mySignIn=driver.find_element(By.ID,'nav-link-accountList-nav-line-1')
sleep(4)
mySignIn.click()
sleep(2)
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
sleep(2)
myEmailTextBox=driver.find_element(By.ID,"ap_email")
sleep(2)
myEmailTextBox.send_keys('selvimaharajan@gmail.com')
continueButton=driver.find_element(By.ID,'continue')
#conditions=driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
conditions=driver.find_element(By.XPATH,"//a[contains(@href,ap_signin_notification_condition_of_use)]")
privacy=driver.find_element(By.XPATH,"//a[contains(@href,ap_mobile_signin_notification_privacy_notice)]")

needHelp=driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")
forgotPassword=driver.find_element(By.ID,'auth-fpp-link-bottom')

otherIssuesWithSignIn=driver.find_element(By.ID,'ap-other-signin-issues-link')
print('Test Passed')

driver.quit()