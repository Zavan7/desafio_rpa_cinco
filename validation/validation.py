from playwright.sync_api import Page

from pages.initial_page import BasePage

import logging

logger = logging.getLogger(__name__)


class ValidationFinal(BasePage):
    """
    Responsável por realizar a validação final da automação.

    Verifica se o elemento esperado está visível na página após a
    execução das etapas anteriores e valida se o texto exibido
    corresponde ao texto esperado.
    """

    def __init__(
        self,
        page: Page,
        selector_validation: str,
    ):
        """
        Inicializa a classe de validação final.

        Args:
            page: Instância da página do Playwright.
            selector_validation: Seletor do elemento utilizado para
                validar a conclusão da automação.
        """
        super().__init__(page)

        self.selector_validation = selector_validation

    def validation_final(self, expected_text: str) -> bool:
        """
        Valida a visibilidade e o conteúdo do elemento de confirmação.

        O método localiza o elemento informado pelo seletor, verifica
        se ele está visível e compara o texto exibido na página com
        o texto esperado informado durante a chamada do método.

        Args:
            expected_text: Texto esperado no elemento de validação.

        Returns:
            True se o elemento estiver visível e o texto corresponder
            ao valor esperado. Retorna False caso o elemento não seja
            encontrado, o texto seja diferente ou ocorra algum erro.
        """

        try:
            logger.info('Validação final')

            locator = self.page.locator(
                self.selector_validation
            )

            if not locator.is_visible():
                logger.warning(
                    'Elemento de validação não encontrado'
                )
                return False

            html_text = locator.inner_text()

            if html_text != expected_text:
                logger.warning(
                    'Não foi possível validar o salvamento. '
                    f'Texto esperado: "{expected_text}" | '
                    f'Texto encontrado: "{html_text}"'
                )
                return False

            logger.info(
                'Informação salva e validada com sucesso'
            )
            return True

        except Exception as error:
            logger.error(
                'Erro ao localizar ou validar a informação: '
                f'{error}'
            )
            return False