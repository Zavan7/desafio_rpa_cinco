import logging

from playwright.sync_api import Page

from pages.initial_page import BasePage

logger = logging.getLogger(__name__)


class TestExceptionPage(BasePage):
    def __init__(
        self,
        page: Page,
        selector_page_exception: str,
        timeout: int = 4_000
    )-> None:
        super().__init__(page, timeout)
        self.selector_page_exception = selector_page_exception


    def click_test_exception(self) -> None:

        logger.info('3º Test Exception Page')

        try:
            self.page.wait_for_selector(
                self.selector_page_exception,
                timeout=self.timeout
            )

            self.page.locator(self.selector_page_exception).click()

            logger.info('Página TestExceptionPage acessada com sucesso')

        except Exception as e:
            logger.error(f'Error: {e}')
            raise
