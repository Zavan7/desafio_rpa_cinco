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
page_patrice_selector = '#menu-item-20'
page_exception_selector = "//a[text()='Test Exceptions']"
button_add_selector  = '#add_btn'
input_selector  = '#row2 .input-field'
save_button_selector = '#save_btn .bnt'

text = 'testando'



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
            patrice_page = PatricePage(page, page_patrice_selector)
            patrice_page.click_patrice()


            # 3º etapa
            test_exception_page = TestExceptionPage(
                page, page_exception_selector
            )
            test_exception_page.click_test_exception()


            # 4º etapa
            test_challenge = TestExceptionChallenge(
                page,
                button_add_selector,
                input_selector
            )

            test_challenge.test_exceptions_challenge()

            # 5º Digitando no input do site
            test_challenge.input_challenge(text, input_selector)

            # 6º Salvando informação adicionada
            test_challenge.save_challenge(save_button_selector)

            sleep(5)
            browser.close()

    except Exception as e:
        print(e)
        

if __name__ == '__main__':
    main()