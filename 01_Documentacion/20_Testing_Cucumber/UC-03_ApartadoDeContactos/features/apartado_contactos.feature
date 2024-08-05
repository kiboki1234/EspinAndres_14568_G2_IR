Feature: Apartado de Contacto en IMPACTONET

  Scenario: El usuario llena y envía el formulario de contacto exitosamente
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "Test User", "test@example.com" y "Estoy interesado en el plan de Internet."
    And el usuario presiona el botón "Enviar"
    Then el sistema envía la información del formulario al correo de la empresa
    And el usuario ve un mensaje de confirmación de envío exitoso

  Scenario: El usuario intenta enviar el formulario de contacto sin llenar todos los campos
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario presiona el botón "Enviar" sin llenar los campos
    Then el sistema muestra un mensaje de error solicitando llenar todos los campos

  Scenario: El usuario visualiza la información de contacto y el mapa de ubicación
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema muestra la dirección física "Nueva Loja, Av. Vicente Lucio / L. Guerrero, Nueva Loja, Ecuador"
    And el sistema muestra el número telefónico "+593 95 87 0928"
    And el sistema muestra el correo electrónico "impactonetrzb@gmail.com"
    And el sistema muestra un mapa interactivo con la ubicación de la empresa
