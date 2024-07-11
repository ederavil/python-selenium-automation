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

driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&webAuthnChallengeIdForAutofill=shtMOKes6ghd86nnqPXLmV6la7mcA9aY%3ANA&webAuthnGetParametersForAutofill=eyJycElkIjoiYW1hem9uLmNvbSIsImNoYWxsZW5nZSI6InNodE1PS2VzNmdoZDg2bm5xUFhMbVY2bGE3bWNBOWFZIiwidGltZW91dCI6OTAwMDAwLCJhbGxvd0NyZWRlbnRpYWxzIjpudWxsLCJtZWRpYXRpb24iOiJjb25kaXRpb25hbCIsInVzZXJWZXJpZmljYXRpb24iOiJwcmVmZXJyZWQifQ%3D%3D&pageId=usflex&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=AV78YSMNJBDTYJ5VB3K2&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-icon-logo")

driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
driver.find_element(By.CSS_SELECTOR, "[name='email']")
driver.find_element(By.CSS_SELECTOR, "input.a-input-text.a-span12[name='password']")
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check.a-input-text[type='password']")
driver.find_element(By.CSS_SELECTOR, "input#continue")
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_conditions_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")

sleep(5)
