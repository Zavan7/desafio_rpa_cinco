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

# URL da aplicação usada no desafio
url = 'https://practicetestautomation.com/'

# Seletores utilizados durante a navegação
page_patrice_selector = '#menu-item-20'
page_exception_selector = "//a[text()='Test Exceptions']"
button_add_selector  = '#add_btn'
input_selector  = '#row2 .input-field'
button_save_selector = '#save_btn .bnt'
tag_savad_locator = '#confirmation'

# Texto utilizado para preencher a navegação
text = 'Pastel de Frango'


logger = logging.getLogger(__name__)

# Responsável por registrar o resultado da automação
mongo = MongoDB()

def main() -> None:

    # Estrutura que armazena os dados da execução para auditoria
    # e posterior persistência no MongoDB.
    result = {
        'start_date': None,
        'end_date': None,
        'duration': None,
        'status': None,
        'error': None,
    }

    # Marca o inicio da execução da automação
    start_date = datetime.now(UTC)

    setup_logging()
    try:

        # Inicializa o Playwright e abre uma nova sessão do navegador
        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            page = browser.new_page()


            # Etapa 1 - Acessa a página inicial
            initial_page = InitialPage(page, url)
            initial_page.open()


            # Etapa 2 - Navega até a página Patrice
            patrice_page = PatricePage(page, page_patrice_selector)
            patrice_page.click_patrice()


            # Etapa 3 - Acessa a página Test Exceptions
            test_exception_page = TestExceptionPage(
                page, page_exception_selector
            )
            test_exception_page.click_test_exception()


            # Etapa 4 - Inicia o desafio
            test_challenge = TestExceptionChallenge(
                page,
                button_add_selector,
                input_selector
            )

            test_challenge.test_exceptions_challenge()

            # 5º Etapa 5 - Preenche o campo de entrada
            test_challenge.input_challenge(text, input_selector)

            # Etapa 6 - Salva as alterações
            test_challenge.save_challenge(button_save_selector)

            # Etapa 7 - Valida se a operação foi concluída com sucesso
            validacao = ValidationFinal(page, tag_savad_locator)
            validacao.validation_final()

            # Encerra a sessão do navegador
            browser.close()

            status = 'Success'

            end_date = datetime.now(UTC)

    # Registra falha durante a execução da automação
    except Exception as e:
        error = f'Error: {e}'
        status = 'fail'

        print(e)

    finally:

        # Calcula o tempo total de execução da automação
        duration = (end_date - start_date).total_seconds()

        # Atualziando informações que serão inseridas no banco de dados
        result.update({
            'start_date': start_date,
            'end_date': end_date,
            'duration': duration,
            'status': status
        })

        # Persiste o resultado da execução no banco de dados
        try:
            
            # Inserindo informações no banco de dados
            mongo.insert(result)
            logger.info('Salvo no banco de dados')
        
        except Exception as e:
            logger.error(f'Erro ao salvar informações em banco de dados: {e}')
            result['error'] = str(e)

if __name__ == '__main__':
    main()