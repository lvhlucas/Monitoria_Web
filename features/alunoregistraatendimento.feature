Feature: Monitor registra atendimento form

  Scenario: Monitor registra atendimento
    Given Usuario é autenticado e é um monitor
    And O monitor informa os seguintes campos: 2018-12-31, 2, linkimg.png, qtdaluno
    When O monitor submeter o formulario
    Then O monitor é redirecionado para a home page


