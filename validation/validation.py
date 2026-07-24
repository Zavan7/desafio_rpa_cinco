from playwright.sync_api import Page

from pages.initial_page import BasePage

import logging

logger = logging.getLogger(__name__)


class ValidationFinal(BasePage):
    def __init__(self, page: Page, selector_validation: str):
        super().__init__(page)
        self.selector_validation = selector_validation


    def Validation_final(self) -> None:
        ...