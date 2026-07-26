# Importação dos módulos de página da automação

from config.log import setup_logging
from pages.initial_page import InitialPage
from pages.patrice_page import PatricePage
from pages.test_exceptions_page import TestExceptionPage
from pages.exception_challenge import TestExceptionChallenge
from validation.validation import ValidationFinal

# Importação das libs chaves do projeto
from playwright.sync_api import sync_playwright
from datetime import UTC, datetime


# Importação das libs de controle e mapeamento da automação
# Gerenciamento de logs
import logging
from config.log import setup_logging
from db.mongo import MongoDB


url = 'https://practicetestautomation.com/'
page_patrice_selector = '#menu-item-20'
page_exception_selector = "//a[text()='Test Exceptions']"
button_add_selector  = '#add_btn'
input_selector  = '#row2 .input-field'
button_save_selector = '#save_btn .bnt'
tag_savad_locator = '#confirmation'

text = 'testando'



logger = logging.getLogger(__name__)

mongo = MongoDB()

def main() -> None:

    result = {
        'start_date': None,
        'end_date': None,
        'duration': None,
        'status': None,
        'error': None,
    }

    start_date = datetime.now(UTC)

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
            test_challenge.save_challenge(button_save_selector)

            # 7º - Validação final
            validacao = ValidationFinal(page, tag_savad_locator)
            validacao.validation_final()

            browser.close()

            status = 'Success'

            end_date = datetime.now(UTC)

    except Exception as e:
        error = f'Error: {e}'
        status = 'fail'

        print(e)

    finally:        
        duration = (end_date - start_date).total_seconds()

        result.update({
            'start_date': start_date,
            'end_date': end_date,
            'duration': duration,
            'status': status
        })

        try:
            mongo.insert(result)
            logger.info('Salvo no banco de dados')
        
        except Exception as e:
            logger.error('Error: ', e)
            result['error'] = str(e)

if __name__ == '__main__':
    main()