from playwright.sync_api import Page

from pages.initial_page import BasePage

import logging

logger = logging.getLogger(__name__)


class ValidationFinal(BasePage):
    def __init__(self, page: Page, selector_validation: str):
        super().__init__(page)
        self.selector_validation = selector_validation


    def validation_final(self) -> bool:
        
        try:
            logger.info('7º - Validação final')
            
            locator = self.page.locator(self.selector_validation)
            
            if not locator.is_visible():
                logger.warning('Elemento não encontrado')
                return False
            
            logger.info('Exito em salvar')
            return True

        except Exception as e:
            logger.error('Error: ', e)
            return False
