from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
This Python script automates the popular online game “Cookie Clicker” using Selenium.
It opens the game, accepts the cookie consent pop-up, selects the English language, and continuously clicks the cookie to gather points.
As the cookie count increases, the script also checks the available products and purchases them if the player has enough cookies.
The bot runs in an infinite loop to maximize cookie production, simulating gameplay without manual interaction.
'''

service = Service(executable_path='/Users/chapi/Coding/GitHub24/WebScraping/Selenium/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/')

cookie_id = 'bigCookie'
cookies_id = 'cookies'
product_price_prefix = 'productPrice'
product_prefix = 'product'

wait = WebDriverWait(driver, 5)

# Accept the cookie consent
try:
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="fc-button fc-cta-consent fc-primary-button"]')))
    accept_cookies_button.click()
    print("Cookies accepted.")
except Exception as e:
    print(f"No cookie consent pop-up found or issue with locating it: {e}")

# Select the English language
wait.until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "English")]')))
language = driver.find_element(By.XPATH, '//*[contains(text(), "English")]')
language.click()

# Start clicking the cookie in a loop
while True:
    try:
        # Find and click the cookie element
        cookie = driver.find_element(By.ID, cookie_id)
        cookie.click()
        
        # Get the current cookie count
        cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
        cookies_count = int(cookies_count.replace(",", ""))
        
        # Buy products if you have enough cookies
        for i in range(4):
            product_price_element = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
            
            if not product_price_element.isdigit():
                continue

            product_price = int(product_price_element)
            
            if cookies_count >= product_price:
                product = driver.find_element(By.ID, product_prefix + str(i))
                product.click()
                break

    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(1)  # Add a small delay to prevent the loop from running too fast