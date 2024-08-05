Feature: Página Principal de IMPACTONET

  Scenario: El usuario intenta acceder a una página no existente
    Given el usuario accede a la página principal de IMPACTONET
    When el usuario intenta acceder a una página no existente
    Then el sistema muestra un error 404

  Scenario: El usuario hace clic en un enlace incorrecto
    Given el usuario accede a la página principal de IMPACTONET
    When el usuario hace clic en un enlace incorrecto
    Then el sistema redirige a una página de error

  Scenario: El usuario navega correctamente por la página principal
    Given el usuario accede a la página principal de IMPACTONET
    When el usuario navega por la página principal correctamente
    Then el sistema muestra la página principal correctamente
    And el sistema muestra los beneficios correctamente

  Scenario: El usuario hace clic en un enlace roto
    Given el usuario accede a la página principal de IMPACTONET
    When el usuario hace clic en un enlace roto
    Then el sistema muestra una página de error

  Scenario: El usuario intenta cargar un recurso inexistente
    Given el usuario accede a la página principal de IMPACTONET
    When el usuario intenta cargar un recurso inexistente
    Then el sistema muestra un mensaje de error de recurso no encontrado
