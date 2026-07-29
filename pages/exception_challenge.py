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

            input_field = self.page.locator(input_selector)

            if not input_field.is_editable():
                raise RuntimeError(
                    'Campo de entrada não está disponível'
                )
            
            input_field.fill(text)

            value = input_field.input_value()

            if value != text:
                raise RuntimeError(
                    f'Falha ao preencher o campo. Valor esperado: "{text}", '
                    f'valor encontrado: "{value}".'
                )

            logger.info('Sucesso ao adicionar informações do campo de input')

        except Exception as e:
            logger.error(
                f'Erro ao adicionar informações no campo de input: {e}'
            )


    def save_challenge(
        self,
        button_save_selector: str,
        input_selector: str
    ) -> None:

        '''
        Clica no botão de salvar, caso ele esteja visível.

        Args:
            button_save_selector (str): Seletor do botão responsável por
                salvar as alterações realizadas.
        '''

        try:
            logger.info('6º - Salvando alterações feitas')

            button_save = self.page.locator(button_save_selector)
            input_field = self.page.locator(input_selector)

            value = input_field.input_value()

            if not value.strip():
                raise RuntimeError(
                    'Campo de entrada vazio. Não é possível salvar.'
                )

            if not button_save.is_visible():
                raise RuntimeError(
                    'Botão Save não está visível.'
                )

            button_save.click()

            logger.info('Sucesso ao salvar página, aguardar validação')

        except Exception as e:
            logger.error(f'Erro ao tentar salvar, conferir validação: {e}')

        
    def state_exception_challenge(
        self,
        input_selector_initial: str,
        button_edit_selector: str,
        button_save_selector: str
    ) -> None:

        '''
        Executa o desafio de tratamento do estado de um campo desabilitado.

            Recarrega a página, verifica se o campo de entrada está visível
            e valida se ele está disponível para edição. Caso o campo esteja
            desabilitado, aciona o botão de edição para habilitá-lo.

            Após habilitar o campo, remove o conteúdo existente, valida se o
            valor foi limpo corretamente e salva as alterações.

            Args:
                input_selector_initial: Seletor utilizado para localizar o
                campo de entrada inicial.
                button_edit_selector: Seletor utilizado para localizar o botão
                    responsável por habilitar a edição do campo.
                button_save_selector: Seletor utilizado para localizar o botão
                    responsável por salvar as alterações.

            Returns:
                None: O método não retorna valores. A execução é registrada
                por meio dos logs da aplicação.

            Raises:
                Exception: Registra nos logs qualquer erro ocorrido durante
                    a execução do desafio.
        '''

        logger.info('INICIANDO NOVO DESAFIO DENTRO DA MESMA PÁGINA')

        input_initial = self.page.locator(input_selector_initial)
        button_edit_inicial = self.page.locator(button_edit_selector)
        button_save_initial = self.page.locator(button_save_selector)

        try:
            self.page.reload()

            if not input_initial.is_visible():
                logger.warning('Compo input não está visível')
                return
            
            if not input_initial.is_editable():
                logger.info('Campo input não editável. Clicando em editar')
                button_edit_inicial.click()

            input_initial.clear()

            if input_initial.input_value() != '':
                logger.info('O campo não foi limpo. Salvamento cancelado.')
                return
            
            logger.info('Campo limpo com sucesso. Salvando alterações.')
            button_save_initial.click()
                

        except Exception as e:
            logger.error(f'Error: {e}')