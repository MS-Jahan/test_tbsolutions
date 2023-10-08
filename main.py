
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os, time
from extension import proxies
from config import *
from helpers import *

# Prevent SSL verification Restriction for webdriver_manager
# Details https://github.com/SergeyPirogov/webdriver_manager/issues/608#issuecomment-1721706727
os.environ["WDM_SSL_VERIFY"] = "0" 

debug("[*] Modules loaded...")

chrome_options = webdriver.ChromeOptions()

# If proxy is used
if USE_PROXY:
    proxies_extension = proxies(PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT)
    chrome_options.add_extension(proxies_extension)
    debug("[*] Proxy extension loaded...")

if HEADLESS:
    chrome_options.add_argument("--headless=new") # if headless mode is needed

# Use the installed ChromeDriver with Selenium
debug("[*] Ensuring updated chromedriver... (ignore warnings)")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.set_page_load_timeout(30)

# Visit the url
debug("[*] Visiting URL...")
driver.get(URL)
time.sleep(10)

# Get input field and send input
debug("[*] Waiting for input field to be filled...")
input_field = WebDriverWait(driver, DEFAULT_DELAY).until(EC.presence_of_element_located((By.CLASS_NAME, "b-input__input")))
input_field.send_keys(INPUT)

# Get submit button by button attribute
debug("[*] Waiting for submit button to be clicked...")
submit_btn = WebDriverWait(driver, DEFAULT_DELAY).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test-id="btnSearch"]')))
submit_btn.click()

# Get result text
WebDriverWait(driver, DEFAULT_DELAY).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[data-test-id="resultsCount"]'), "Displaying"))
result_div = WebDriverWait(driver, DEFAULT_DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="resultsCount"]')))
result_text = get_total_results(result_div.text)

print(f"[!] Total Result: {result_text}")

driver.quit()