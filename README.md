# RPA Challenge #05 - ElementNotInteractableException

## 📋 Sobre o desafio

Este desafio simula um cenário onde existem **dois botões `Save` com o mesmo atributo `name="Save"`**, porém apenas um deles está visível.

Ao utilizar um seletor genérico, o primeiro elemento localizado é invisível, resultando na exceção **ElementNotInteractableException**. O objetivo é identificar corretamente o elemento interativo, realizar a ação e validar que o registro foi salvo.

---

## 🚀 Solução

A implementação foi desenvolvida utilizando **Python** e **Playwright**, explorando os recursos de sincronização automática da biblioteca para localizar apenas elementos realmente interativos, tornando a automação mais estável e previsível.

Além da resolução do desafio, o projeto foi estruturado com foco em **legibilidade**, **manutenção** e **reutilização de código**, simulando a organização utilizada em projetos reais de RPA.

---

## 🏗️ Arquitetura

O projeto foi desenvolvido seguindo conceitos de Engenharia de Software, utilizando:

- Page Object Model (POM);
- Programação Orientada a Objetos (POO);
- Herança para reutilização da classe base (`BasePage`);
- Encapsulamento das responsabilidades de cada página;
- Logging estruturado para rastreabilidade da execução;
- Persistência de informações utilizando MongoDB;
- Separação de responsabilidades;
- Código modular e reutilizável.

---

## 🛠️ Tecnologias

- Python
- Playwright
- MongoDB
- Logging
- Page Object Model (POM)

---

## 📚 Aprendizados

Mais do que resolver a exceção apresentada no desafio, este projeto reforça a importância de desenvolver automações pensando em sua evolução.

Durante a implementação, a preocupação não foi apenas fazer o fluxo funcionar, mas também construir uma estrutura que facilite futuras manutenções e refatorações. Cada decisão de arquitetura buscou tornar o código mais previsível, legível e simples de evoluir.

Um dos pontos trabalhados foi a padronização da nomenclatura de variáveis, classes, funções e seletores. A intenção não era apenas utilizar nomes descritivos, mas deixar explícita a responsabilidade de cada elemento, tornando a leitura do código mais intuitiva.

### Exemplo:

**Antes**

```python
url = "https://practicetestautomation.com/"
practice_page_selector = "#menu-item-20"
test_exception_selector = "//a[text()='Test Exceptions']"
button_add_selector = "#add_btn"
input_selector = "#row2 .input-field"
```

**Depois**

```python
url = "https://practicetestautomation.com/"
page_practice_selector = "#menu-item-20"
page_exception_selector = "//a[text()='Test Exceptions']"
button_add_selector = "#add_btn"
button_save_selector = "#save_btn .btn"
input_selector = "#row2 .input-field"
```

Com essa convenção, basta ler o nome de um seletor para entender qual elemento ele representa, reduzindo ambiguidades e facilitando futuras alterações.

A ideia é que, ao revisitar este projeto daqui a alguns meses, eu consiga compreender rapidamente o fluxo da aplicação, identificar a responsabilidade de cada componente e realizar ajustes com segurança, sem precisar redescobrir o funcionamento do código.

Este é apenas o início. Os próximos desafios trarão cenários mais complexos, exigindo uma atenção ainda maior à arquitetura, aos padrões de projeto e às boas práticas de engenharia de software para construir automações cada vez mais robustas, escaláveis e de fácil manutenção.
