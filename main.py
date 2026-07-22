# Importação dos módulos de página da automação

from config.log import setup_logging
from pages.initial_page import InitialPage
from pages.patrice_page import PatricePage
from pages.test_exceptions_page import TestExceptionPage
from pages.exception_challenge import TestExceptionChallenge

# Importação das libs chaves do projeto
from playwright.sync_api import sync_playwright
from datetime import UTC, datetime


# Importação das libs de controle e mapeamento da automação
# Gerenciamento de logs
import logging
from config.log import setup_logging
from db.mongo import MongoDB

# Libs para debug (Não vai pra produção)
from time import sleep


url = 'https://practicetestautomation.com/'
patrice_page_selector = '#menu-item-20'
test_exception_selection = "//a[text()='Test Exceptions']"
button_add_selector  = '#add_btn'
input_selector  = '#row2 .input-field'




logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()
    try:
        '''
        Iniciando objeto playwright
        '''
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()


            # 1º etapa
            initial_page = InitialPage(page, url)
            initial_page.open()


            # 2º etapa
            patrice_page = PatricePage(page, patrice_page_selector)
            patrice_page.click_patrice()


            # 3º etapa
            test_exception_page = TestExceptionPage(
                page, test_exception_selection
            )
            test_exception_page.click_test_exception()


            # 4º etapa
            test_challenge = TestExceptionChallenge(
                page,
                button_add_selector,
                input_selector
            )

            test_challenge.test_exceptions_challenge()

            # sleep(5)
            browser.close()

    except Exception as e:
        print(e)
        

if __name__ == '__main__':
    main()