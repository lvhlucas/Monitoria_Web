Feature: Aluno Pede Monitor form

  Scenario: Aluno faz um pedido de monitor
    Given Usuario é autenticado
    And O aluno informa os seguintes campos: "<comentario>", "<prog1>", "<semestre>"
    When O aluno submeter o formulario
    Then Ele é redirecionado para a home page


