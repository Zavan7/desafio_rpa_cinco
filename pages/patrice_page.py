import logging

from playwright.sync_api import Page

from pages.initial_page import BasePage

logger = logging.getLogger(__name__)

class PatricePage(BasePage):
    def __init__(
        self,
        page: Page,
        selector_patrice: str,
        timeout: int = 4_000
    ) -> None:
        super().__init__(page, timeout)
        self.selecot_patrice = selector_patrice

    
    def click_patrice(self) -> None:

        logger.info('2º Patrice Page')

        try:
            self.page.wait_for_selector(
                self.selecot_patrice,
                timeout=self.timeout
            )

            self.page.locator(self.selecot_patrice).click()

            logger.info('Página Patrice acessada com sucesso')

        except Exception as e:
            logger.error(f'Error: {e}')
            raise