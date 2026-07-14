import logging

from playwright.sync_api import Page


logger = logging.getLogger(__name__)


class BasePage:
    def __init__ (self, page: Page, timeout: int = 4_000):
        self.page = page
        self.timeout = timeout


class InitialPage(BasePage):
    def __init__(self, page: Page, url: str, timeout:int = 4_000) -> None:
        super().__init__(page, timeout)
        self.url = url

    def open(self) -> None:

        logger.info('1º - Initial Page')

        try:
            self.page.goto(self.url, timeout=self.timeout)
            logger.info('Sucesso ao abrir a página')

        except Exception as e:
            logger.error(f'1º Initial Page {e}')
            raise
