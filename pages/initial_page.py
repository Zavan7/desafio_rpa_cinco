import logging

from playwright.sync_api import Page


logger = logging.getLogger(__name__)


class BasePage:
    '''
    Classe base para todas as páginas da automação.

    Armazena a instância da página do Playwright e o tempo padrão
    de espera utilizado pelas classes filhas.
    '''

    def __init__(self, page: Page, timeout: int = 4_000):
        '''
        Inicializa a classe base.

        Args:
            page (Page): Instância da página do Playwright.
            timeout (int, opcional): Tempo máximo de espera para operações
                na página. Padrão: 4000 ms.
        '''
        self.page = page
        self.timeout = timeout


class InitialPage(BasePage):
    '''
    Responsável por acessar a página inicial da aplicação.

    Herda as funcionalidades da classe BasePage e realiza a navegação
    para a URL informada.
    '''

    def __init__(self, page: Page, url: str, timeout: int = 4_000) -> None:
        '''
        Inicializa a página inicial.

        Args:
            page (Page): Instância da página do Playwright.
            url (str): Endereço da página que será acessada.
            timeout (int, opcional): Tempo máximo de espera para o
                carregamento da página. Padrão: 4000 ms.
        '''
        super().__init__(page, timeout)
        self.url = url

    def open(self) -> None:
        '''
        Acessa a URL configurada para a página inicial.

        Registra em log o início da navegação e informa se a página foi
        carregada com sucesso. Caso ocorra algum erro durante o acesso,
        a exceção é registrada e propagada para a camada chamadora.

        Raises:
            Exception: Exceção gerada durante a navegação para a página.
        '''

        logger.info('1º - Initial Page')

        try:
            self.page.goto(self.url, timeout=self.timeout)
            logger.info('Sucesso ao abrir a página inicial')

        except Exception as e:
            logger.error(f'Erro ao iniciar a página: {e}')
            raise