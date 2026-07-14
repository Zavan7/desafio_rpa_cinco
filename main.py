import logging
from time import sleep
from playwright.sync_api import sync_playwright

from config.log import setup_logging
from pages.initial_page import InitialPage

url = 'https://practicetestautomation.com/'

logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()
    try:
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()

            initial_page = InitialPage(page, url)
            initial_page.open()

            sleep(5)
            browser.close()

    except Exception as e:
        print(e)
        

if __name__ == '__main__':
    main()