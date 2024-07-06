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
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(3)
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(5)
driver.find_element(By.XPATH, "//label[@for='keepMeSignedIn']")
print("Test case Passed")

# Search item
# driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys('laptops')
# driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#
# sleep(7)
#
# expected_text = 'laptops'
# text_display = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
# assert expected_text in text_display, f"Expected text {expected_text} is not in the text displayed{text_display}."
# print("Test case Passed")

