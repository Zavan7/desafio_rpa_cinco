import logging

from playwright.sync_api import Page

from pages.initial_page import BasePage

logger = logging.getLogger(__name__)


class TestExceptionChallenge(BasePage):
    '''
    Classe responsável por automatizar a etapa "Test Exceptions" do desafio.

    Fornece métodos para iniciar o desafio, preencher o campo de entrada
    e salvar as alterações realizadas na página.
    '''

    def __init__(
        self,
        page: Page,
        selector_button_challenge: str,
        input_selector: str,
        timeout: int = 4_000
    ) -> None:
        '''
        Inicializa a classe com a página, os seletores utilizados na
        automação e o tempo padrão de espera.

        Args:
            page (Page): Instância da página do Playwright.
            selector_button_challenge (str): Seletor do botão que inicia o desafio.
            input_selector (str): Seletor do campo de entrada.
            timeout (int, opcional): Tempo máximo de espera para localizar
                elementos na página. Padrão: 4000 ms.
        '''
        super().__init__(page, timeout)
        self.selector_button_challenge = selector_button_challenge
        self.input_selector = input_selector


    def test_exceptions_challenge(self) -> bool:
        '''
        Inicia o desafio e verifica se o campo de entrada foi exibido.

        O método aguarda o botão do desafio, valida se ele está habilitado,
        realiza o clique e espera até que o campo de entrada fique visível.

        Returns:
            bool:
                True se o desafio foi iniciado com sucesso.
                False caso o botão esteja desabilitado ou ocorra algum erro.
        '''

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
            logger.info('Área de input disponível')
            return True

        except Exception as e:
            logger.error(f'Erro, área de input indisponível: {e}')
            return False


    def input_challenge(self, text: str, input_selector: str) -> None:
        '''
        Preenche o campo informado com o texto recebido.

        Args:
            text (str): Conteúdo que será inserido no campo.
            input_selector (str): Seletor do campo que receberá o texto.
        '''

        try:
            logger.info(
                '5º - Iniciando o input de informações no campo selecionado'
            )

            if self.page.locator(input_selector).is_editable:
                self.page.locator(input_selector).fill(text)

            logger.info('Sucesso ao adicionar informações do campo de input')

        except Exception as e:
            logger.error(
                f'Erro ao adicionar informações no campo de input: {e}'
            )


    def save_challenge(self, button_save_selector: str) -> None:
        '''
        Clica no botão de salvar, caso ele esteja visível.

        Args:
            button_save_selector (str): Seletor do botão responsável por
                salvar as alterações realizadas.
        '''

        try:
            logger.info('6º - Salvando alterações feitas')

            button_save = self.page.locator(button_save_selector)

            if button_save.is_visible():
                button_save.click()
            logger.info('Sucesso ao salvar página, aguardar validação')

        except Exception as e:
            logger.error(f'Erro ao tentar salvar, conferir validação: {e}')