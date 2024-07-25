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
accept = "application/json, text/plain, */*"
accept_language = "en-US,en;q=0.9,id;q=0.8"
cache_control = "no-cache"
origin = "https://djdog.io"
pragma = "no-cache"
priority = "u=1, i"
sec_fetch_dest = "empty"
sec_fetch_mode = "cors"
sec_fetch_site = "same-site"

chrome_options.add_argument(f"accept={accept}")
chrome_options.add_argument(f"accept-language={accept_language}")
chrome_options.add_argument(f"cache-control={cache_control}")
chrome_options.add_argument(f"origin={origin}")
chrome_options.add_argument(f"pragma={pragma}")
chrome_options.add_argument(f"priority={priority}")
chrome_options.add_argument(f"sec-fetch-dest={sec_fetch_dest}")
chrome_options.add_argument(f"sec-fetch-mode={sec_fetch_mode}")
chrome_options.add_argument(f"sec-fetch-site={sec_fetch_site}")
chrome_options.add_argument(f"user-agent={mobile_user_agent}")

driver = webdriver.Chrome(options=chrome_options)

url = "https://djdog.io/dog#tgWebAppData=user%3D%257B%2522id%2522%253A6649740242%252C%2522first_name%2522%253A%2522saroed10%2522%252C%2522last_name%2522%253A%2522%2522%252C%2522username%2522%253A%2522saroed10%2522%252C%2522language_code%2522%253A%2522id%2522%252C%2522allows_write_to_pm%2522%253Atrue%257D%26chat_instance%3D-5808842632094863291%26chat_type%3Dsender%26auth_date%3D1721925505%26hash%3D4df5b20ecca82a19af7b660ade46e3fafbe98f59918414547c32fde9d515d082&tgWebAppVersion=7.6&tgWebAppPlatform=web&tgWebAppThemeParams=%7B%22bg_color%22%3A%22%23ffffff%22%2C%22button_color%22%3A%22%233390ec%22%2C%22button_text_color%22%3A%22%23ffffff%22%2C%22hint_color%22%3A%22%23707579%22%2C%22link_color%22%3A%22%2300488f%22%2C%22secondary_bg_color%22%3A%22%23f4f4f5%22%2C%22text_color%22%3A%22%23000000%22%2C%22header_bg_color%22%3A%22%23ffffff%22%2C%22accent_text_color%22%3A%22%233390ec%22%2C%22section_bg_color%22%3A%22%23ffffff%22%2C%22section_header_text_color%22%3A%22%233390ec%22%2C%22subtitle_text_color%22%3A%22%23707579%22%2C%22destructive_text_color%22%3A%22%23df3f40%22%7D"
tapsemua = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/img[1]'
prize = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[3]/img'
buybox = '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div[3]/div/span'
tap = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/img[2]'
home = '/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div[1]/img'

driver.get(url)
while True:
    try:
        driver.get(url)
        print("berhasil login")
        time.sleep(5)
        awal = driver.find_element(By.XPATH,home)
        awal.click()
        print("menu home")
        time.sleep(5)
        claim = driver.find_element(By.XPATH,tapsemua)
        claim.click()
        print("berhasil tap tap")
        time.sleep(5)
        hadiah = driver.find_element(By.XPATH,prize)
        hadiah.click()
        print("menu prize")
        time.sleep(5)
        buy = driver.find_element(By.XPATH,buybox)
        buy.click()
        print("berhasil buy box")
        time.sleep(5)
    except:
        pass
