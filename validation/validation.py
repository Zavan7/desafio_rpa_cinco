from playwright.sync_api import Page

from pages.initial_page import BasePage

import logging

logger = logging.getLogger(__name__)


class ValidationFinal(BasePage):
    '''
    Responsável por realizar a validação final da automação.

    Verifica se o elemento esperado está visível na página após a
    execução das etapas anteriores, indicando que a operação foi
    concluída com sucesso.
    '''

    def __init__(self, page: Page, selector_validation: str):
        '''
        Inicializa a classe de validação final.

        Args:
            page (Page): Instância da página do Playwright.
            selector_validation (str): Seletor do elemento utilizado
                para validar a conclusão da automação.
        '''
        super().__init__(page)
        self.selector_validation = selector_validation


    def validation_final(self) -> bool:
        '''
        Verifica se o elemento de validação está visível na página.

        O método localiza o elemento informado pelo seletor e valida sua
        visibilidade. Caso o elemento seja encontrado, considera que a
        automação foi concluída com sucesso.

        Returns:
            bool:
                True se o elemento de validação estiver visível.
                False caso o elemento não seja encontrado ou ocorra
                algum erro durante a validação.
        '''

        try:
            logger.info('7º - Validação final')

            locator = self.page.locator(self.selector_validation)

            if not locator.is_visible():
                logger.warning('Elemento de validação não encontrado')
                return False

            logger.info('Sua informação foi salva e validada')
            return True

        except Exception as e:
            logger.error(f'Erro, informação validadora não localizada {e}')
            return False