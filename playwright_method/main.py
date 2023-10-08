from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
import re

# Set your constants here
import sys
sys.path.append('..')
from config import *
from helpers import *

proxy = None
if USE_PROXY:
    proxy = {
        "server": f"http://{PROXY_HOST}:{PROXY_PORT}",
        "username": PROXY_USER,
        "password": PROXY_PASS
    }

with sync_playwright() as p:
    browser = p.chromium.launch(headless=HEADLESS, proxy=proxy)
    context = browser.new_context()

    page = context.new_page()
    page.goto(URL)
    page.wait_for_selector('.b-input__input').fill(INPUT)
    page.wait_for_selector('button[data-test-id="btnSearch"]').click()
    page.wait_for_selector('div[data-test-id="resultsCount"]').is_visible()
    expect(page.locator('div[data-test-id="resultsCount"]')
           ).to_have_text(re.compile(RESULT_REGEX))

    result_text = page.locator('div[data-test-id="resultsCount"]').inner_text()

    print(f"[!] Total Result: {get_total_results(result_text)}")

    browser.close()
