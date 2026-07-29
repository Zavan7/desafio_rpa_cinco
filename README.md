# RPA Challenge #05 - ElementNotInteractableException / InvalidElementStateException

## 📋 Sobre o desafio

Este projeto evolui a implementação do desafio anterior, adicionando novos cenários de interação com elementos e tratamento de exceções utilizando **Python + Playwright**.

O primeiro cenário simula uma situação onde existem **dois botões `Save` com o mesmo atributo `name="Save"`**, porém apenas um deles está visível.

Ao utilizar um seletor genérico, o primeiro elemento localizado é invisível, resultando na exceção **ElementNotInteractableException**. O objetivo é identificar corretamente o elemento interativo, realizar a ação e validar que o registro foi salvo.

No segundo cenário, é trabalhado o tratamento da exceção **InvalidElementStateException**, onde um campo de input inicia desabilitado.

Antes de realizar ações como limpar ou inserir valores, é necessário alterar o estado do elemento através da interação com o botão **Edit**, garantindo que o campo esteja preparado para receber novas informações.

Além disso, o desafio demonstra que tentar interagir diretamente com elementos desabilitados pode gerar comportamentos diferentes, como a própria **ElementNotInteractableException**, reforçando a importância de validar o estado dos elementos antes da execução das ações.

---

## 🚀 Solução

A implementação foi desenvolvida utilizando **Python** e **Playwright**, explorando recursos como:

- Localização de elementos interativos;
- Sincronização automática;
- Validação de estados dos componentes;
- Tratamento de cenários de exceção;
- Organização da automação utilizando padrões de engenharia de software.

Além da resolução dos desafios propostos, o projeto foi estruturado pensando em evolução.

A ideia não é apenas criar uma automação que funcione, mas construir uma base que consiga receber novos desafios, novas funcionalidades e novos fluxos sem comprometer a estabilidade do código.

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
- Código modular e reutilizável;
- Estrutura preparada para crescimento contínuo.

---

## 🛠️ Tecnologias

- Python
- Playwright
- MongoDB
- Logging
- Page Object Model (POM)

---

## 📈 Evolução e escalabilidade

Desde o início, o objetivo deste projeto não foi apenas concluir desafios isolados, mas construir uma base de estudos que permita evoluir junto com a complexidade das automações.

A arquitetura foi pensada para crescer de forma saudável, evitando problemas comuns durante a evolução de projetos, como:

- Duplicação de código;
- Dificuldade de manutenção;
- Alterações que quebram funcionalidades existentes;
- Acoplamento excessivo entre componentes;
- Gargalos causados por uma estrutura pouco flexível.

Conforme novos desafios são adicionados, o foco é continuar melhorando a organização do projeto, aplicando boas práticas e identificando oportunidades de refatoração.

Este projeto funciona como uma sala de aula prática, onde cada novo cenário é uma oportunidade para aprofundar conhecimentos em automação, arquitetura de software e qualidade de código.

---

## 📚 Aprendizados

Mais do que resolver as exceções apresentadas nos desafios, este projeto reforça a importância de desenvolver automações pensando em sua evolução.

Durante a implementação, a preocupação não foi apenas fazer o fluxo funcionar, mas também construir uma estrutura que facilite futuras manutenções e refatorações.

Alguns pontos que venho trabalhando durante a evolução do projeto:

- Melhor organização de responsabilidades;
- Padronização de nomenclaturas;
- Clareza na definição de classes, métodos e variáveis;
- Redução de repetição de código;
- Identificação de comportamentos que podem ser reutilizados;
- Criação de componentes mais genéricos e flexíveis.

Um dos principais focos atuais é analisar a estrutura constantemente para evitar duplicações e encontrar oportunidades de abstração.

A ideia é que novas funcionalidades sejam adicionadas aproveitando componentes existentes, mantendo o código limpo, organizado e sustentável.

Um dos objetivos é que, ao revisitar este projeto daqui a alguns meses, eu consiga compreender rapidamente o fluxo da aplicação, identificar a responsabilidade de cada componente e realizar ajustes com segurança, sem precisar redescobrir o funcionamento do código.

Este é apenas o começo. Os próximos desafios trarão cenários mais complexos, exigindo uma atenção ainda maior à arquitetura, padrões de projeto e boas práticas de engenharia de software para construir automações cada vez mais robustas, escaláveis e fáceis de manter.
