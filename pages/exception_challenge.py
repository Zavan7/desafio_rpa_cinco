import logging

from playwright.sync_api import Page

from pages.initial_page import BasePage

logger = logging.getLogger(__name__)


class TestExceptionChallenge(BasePage):
    def __init__(
        self,
        page: Page,
        selector_button_challenge: str,
        input_selector: str,
        timeout: int = 4_000
    )-> None:
        super().__init__(page, timeout)
        self.selector_button_challenge = selector_button_challenge
        self.input_selector = input_selector


    def test_exceptions_challenge(self) -> bool:
        
        try:
            logger.info('4° - Test Exceptions')
            self.page.wait_for_selector(
                self.selector_button_challenge,
                timeout=self.timeout
            )

            test_button = self.page.locator(self.selector_button_challenge)

            if not test_button.is_enabled():
                return False
            
            test_button.click()

            self.page.locator(self.input_selector).wait_for(
                state='visible',
                timeout=20_000
            )
            logger.info('Apareceu o trem lá')
            return True

            
        
        except Exception as e:
            logger.error(f'3° - Test Exceptions\nError: {e}')
            return False



    def input_challenge(self, text: str, input_selector: str) -> None: 

        try:
            logger.info('5º - Iniciando o input de informações no campo selecionado')

            if self.page.locator(input_selector).is_editable:
                self.page.locator(input_selector).fill(text)

        except Exception as e:
            logger.error('Error: ', e)


    def save_challenge(self, button_save_selector: str) -> None:

        try:
            logger.info('6º - Salvando alterações feitas')

            button_save = self.page.locator(button_save_selector)

            if button_save.is_visible():   
                button_save.click()

        except Exception as e:
            logger.error('Error: ', e)