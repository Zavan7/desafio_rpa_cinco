from playwright.sync_api import sync_playwright
from time import sleep

url = 'https://practicetestautomation.com/'


with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    sleep(5)
    browser.close()