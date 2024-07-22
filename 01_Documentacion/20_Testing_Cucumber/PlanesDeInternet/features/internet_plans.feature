Feature: Apartado de Planes de Internet

  Scenario: Visualizar los planes de internet disponibles
    Given el usuario accede a la página de IMPACTONET
    When el sistema muestra los planes de internet disponibles
    Then el usuario debe ver el ancho de banda en la parte superior de cada plan
    And el usuario debe ver una imagen representativa de cada plan
    And el usuario debe ver una breve descripción del plan de internet
    And el usuario debe ver un botón etiquetado como "Cotizar" en cada plan

  Scenario: Seleccionar un plan para cotización
    Given el usuario está en la página de IMPACTONET
    When el usuario selecciona un plan específico
    Then el sistema debe redirigir al usuario a la página de contacto
    And el usuario debe poder llenar el formulario de contacto
    And el usuario debe poder enviar el formulario de contacto
