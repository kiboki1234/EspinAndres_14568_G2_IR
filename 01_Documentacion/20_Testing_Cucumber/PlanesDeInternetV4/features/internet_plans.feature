Feature: Visualización y cotización de planes de Internet

  Scenario: El usuario visualiza y cotiza un plan de Internet
    Given el usuario accede a la página de INPACTONET
    When el usuario visualiza los planes de Internet disponibles
    Then el usuario debe ver el ancho de banda en la parte superior de cada plan
    And el usuario debe ver una imagen representativa de cada plan
    And el usuario debe ver una breve descripción del plan de Internet
    And el usuario debe ver un botón etiquetado como "Cotizar" en cada plan
    When el usuario selecciona un plan específico
    Then el usuario es redirigido a la página de contacto
    And el usuario llena el formulario de contacto
    And el sistema envía el mensaje del usuario a la secretaria
    Then la secretaria recibe el mensaje del sistema
    And la secretaria responde el mensaje de acuerdo con la información solicitada
    And el sistema envía la respuesta de la secretaria al usuario
    Then se establece comunicación entre la secretaria y el usuario

  Scenario: El sistema no muestra los planes de Internet
  Given el usuario accede a la página de INPACTONET
  When el usuario visualiza los planes de Internet disponibles
  Then el usuario no debe ver ningún plan de Internet
  And el usuario no puede seleccionar ningún plan

  Scenario: Los planes de Internet no muestran el ancho de banda
  Given el usuario accede a la página de INPACTONET
  When el usuario visualiza los planes de Internet disponibles
  Then el usuario debe ver una imagen representativa de cada plan
  And el usuario debe ver una breve descripción del plan de Internet
  And el usuario debe ver un botón etiquetado como "Cotizar" en cada plan
  But el usuario no debe ver el ancho de banda en los planes

  Scenario: El usuario no es redirigido a la página de contacto
  Given el usuario accede a la página de INPACTONET
  When el usuario visualiza los planes de Internet disponibles
  And el usuario selecciona un plan específico
  Then el usuario no es redirigido a la página de contacto

  Scenario: El sistema no envía el mensaje al seleccionar un plan
  Given el usuario accede a la página de INPACTONET
  When el usuario visualiza los planes de Internet disponibles
  And el usuario selecciona un plan específico
  And el usuario es redirigido a la página de contacto
  And el usuario llena el formulario de contacto
  Then el sistema no envía el mensaje del usuario a la secretaria
  And la secretaria no recibe el mensaje del sistema




