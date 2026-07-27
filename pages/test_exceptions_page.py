import logging

from playwright.sync_api import Page

from pages.initial_page import BasePage

logger = logging.getLogger(__name__)


class TestExceptionPage(BasePage):
    '''
    Responsável por acessar a página "Test Exception" da aplicação.

    Herda as funcionalidades da classe BasePage e realiza a navegação
    até a página do desafio Test Exception.
    '''

    def __init__(
        self,
        page: Page,
        selector_page_exception: str,
        timeout: int = 4_000
    ) -> None:
        '''
        Inicializa a página Test Exception.

        Args:
            page (Page): Instância da página do Playwright.
            selector_page_exception (str): Seletor do elemento utilizado
                para acessar a página Test Exception.
            timeout (int, opcional): Tempo máximo de espera para localizar
                elementos na página. Padrão: 4000 ms.
        '''
        super().__init__(page, timeout)
        self.selector_page_exception = selector_page_exception


    def click_test_exception(self) -> None:
        '''
        Aguarda o elemento da página Test Exception ficar disponível e
        realiza o clique para acessá-la.

        Registra em log o início da operação e confirma o acesso em caso
        de sucesso.

        Raises:
            Exception: Exceção gerada caso ocorra erro durante a interação
                com a página.
        '''

        logger.info('3º Test Exception Page')

        try:
            self.page.wait_for_selector(
                self.selector_page_exception,
                timeout=self.timeout
            )

            self.page.locator(self.selector_page_exception).click()

            logger.info('Página TestExceptionPage acessada com sucesso')

        except Exception as e:
            logger.error(f'Erro ao acessar a página Test Exception: {e}')
            raise