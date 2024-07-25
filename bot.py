
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
session_path = "C:/selenium"
chrome_options.add_argument(f"user-data-dir={session_path}")
chrome_options.add_argument("--log-level=3")  # Set log level to suppress INFO and WARNING messages
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')

mobile_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
chrome_options.add_argument(f"user-agent={mobile_user_agent}")

driver = webdriver.Chrome(options=chrome_options)

url = "https://djdog.io/dog"
tapsemua = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/img[1]'
query = open("query.txt", "r")

driver.get(url+query.read())
while True:
    try:
        driver.get(url)
        claim = driver.find_element(By.XPATH,tapsemua)
        claim.click()
        print("sukses tap tap")
    except:
        pass
