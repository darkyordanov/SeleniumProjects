from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

'''
This Python script automates a Google search using Selenium WebDriver.
It opens Google, handles cookie consent by rejecting all cookies, then searches for “bitcoin current price” and clicks on the first search result related to Binance.
The script waits for necessary elements to load using explicit waits and closes the browser after a 20-second delay.
'''

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path='/Users/chapi/Coding/GitHub24/WebScraping/Selenium/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://google.com')
wait = WebDriverWait(driver, 5)
try:
    # Wait for the cookie consent button with class name and click it
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "QS5gu") and contains(text(),"Reject all")]')))
    accept_cookies_button.click()
    print("Cookies accepted.")

except Exception as e:
    print(f"No cookie consent pop-up found or issue with locating it: {e}")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf'))
)

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
input_element.clear()
input_element.send_keys('bitcoin current price', Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Binance'))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Binance')
link.click()

time.sleep(20)

driver.quit()
