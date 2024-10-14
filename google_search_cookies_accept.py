from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup ChromeDriver service
service = Service(executable_path='/Users/chapi/Coding/GitHub24/WebScraping/SimpleSeleniumProject/SimpleSeleniumProject/chromedriver')
driver = webdriver.Chrome(service=service)

# Open Google
driver.get('https://google.com')

# Setup WebDriverWait
wait = WebDriverWait(driver, 10)

time.sleep(2)

COUNTER = 30

# Check if the cookie consent pop-up appears and accept it
try:
    # Wait for the cookie consent button with class name and click it
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "QS5gu") and contains(text(),"Accept all")]')))
    accept_cookies_button.click()
    print("Cookies accepted.")
    print(COUNTER * '-')
except Exception as e:
    print(f"No cookie consent pop-up found or issue with locating it: {e}")
    print(COUNTER * '-')

# Wait for the search input field (textarea) to be clickable
# try:
#     input_element = wait.until(EC.element_to_be_clickable((By.NAME, 'q')))
#     input_element.click()  # Focus on the search bar
#     input_element.send_keys('bitcoin current price', Keys.ENTER)
# except Exception as e:
#     print(f"Issue with locating the search bar: {e}")

time.sleep(2)

try:
    input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
    print(f'Sucess click on the search bar')
    print(COUNTER * '-')
    time.sleep(1)
    
    input_search_element = input('What you want to search: ')
    # input_search_element = 'bitcoin current price'
    print(COUNTER * '-')
    
    input_element.send_keys(input_search_element, Keys.ENTER)
    print(f'Searching for: {input_search_element[:26]}')
    print(COUNTER * '-')
except Exception as e:
    print(f"Issue with locating the search bar: {e}")
    print(COUNTER * '-')

time.sleep(2)

# Wait for the results to load and find the first search result link
try:
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, '(//h3)[1]')))  # This locates the first <h3> tag in search results
    first_result.click()  # Click on the first search result
    print("Clicked on the first search result.")
    print(COUNTER * '-')
except Exception as e:
    print(f"Issue with locating the first search result: {e}")
    print(COUNTER * '-')

# Wait for some time to view the results
time.sleep(60)

# Close the browser
driver.quit()