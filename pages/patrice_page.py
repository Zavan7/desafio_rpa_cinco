import logging

from playwright.sync_api import Page

from pages.initial_page import BasePage

logger = logging.getLogger(__name__)


class PatricePage(BasePage):
    '''
    Responsável por acessar a página "Patrice" da aplicação.

    Herda as funcionalidades da classe BasePage e realiza a interação
    necessária para navegar até a página desejada.
    '''

    def __init__(
        self,
        page: Page,
        selector_patrice: str,
        timeout: int = 4_000
    ) -> None:
        '''
        Inicializa a página Patrice.

        Args:
            page (Page): Instância da página do Playwright.
            selector_patrice (str): Seletor do elemento utilizado para
                acessar a página Patrice.
            timeout (int, opcional): Tempo máximo de espera para localizar
                elementos na página. Padrão: 4000 ms.
        '''
        super().__init__(page, timeout)
        self.selecot_patrice = selector_patrice

    
    def click_patrice(self) -> None:
        '''
        Aguarda o elemento da página Patrice ficar disponível e realiza
        o clique para acessá-la.

        Registra em log o início da operação e confirma o acesso em caso
        de sucesso.

        Raises:
            Exception: Exceção gerada caso ocorra erro durante a interação
                com a página.
        '''

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