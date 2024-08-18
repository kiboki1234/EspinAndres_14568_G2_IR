Feature: Apartado de Contacto en IMPACTONET

  Scenario: El usuario llena y envía el formulario de contacto exitosamente
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "José Martínez", "jose.martinez@gmail.com" y "Estoy interesado en los planes de Internet."
    And el usuario presiona el botón "Enviar"
    Then el sistema envía la información del formulario al correo de la empresa
    And el usuario ve un mensaje de confirmación de envío exitoso

  Scenario: El usuario intenta enviar el formulario de contacto sin llenar todos los campos
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario presiona el botón "Enviar" sin llenar los campos
    Then el sistema muestra un mensaje de error solicitando llenar todos los campos

  Scenario: El usuario intenta enviar el formulario con un nombre inválido
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "J" como nombre, "juan.perez@hotmail.com" y "Estoy interesado en sus planes."
    And el usuario presiona el botón "Enviar"
    Then el sistema muestra un mensaje de error indicando que el nombre es demasiado corto

  Scenario: El usuario intenta enviar el formulario con un nombre que contiene números
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "Juan123", "juan.perez@hotmail.com" y "Me gustaría saber más sobre los servicios."
    And el usuario presiona el botón "Enviar"
    Then el sistema muestra un mensaje de error indicando que el nombre no debe contener números

  Scenario: El usuario intenta enviar el formulario con un correo electrónico inválido (sin arroba)
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "María López", "marialopezgmail.com" y "Estoy interesada en el plan de alta velocidad."
    And el usuario presiona el botón "Enviar"
    Then el sistema muestra un mensaje de error indicando que el correo electrónico es inválido

  Scenario: El usuario intenta enviar el formulario con un correo electrónico inválido (sin dominio)
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "Carlos Fernández", "carlos@impactonet" y "Quisiera saber más sobre el servicio empresarial."
    And el usuario presiona el botón "Enviar"
    Then el sistema muestra un mensaje de error indicando que el correo electrónico es inválido

  Scenario: El usuario intenta enviar el formulario con un mensaje demasiado corto
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "Laura García", "laura.garcia@yahoo.com" y "Hola"
    And el usuario presiona el botón "Enviar"
    Then el sistema muestra un mensaje de error indicando que el mensaje es demasiado corto

  Scenario: El usuario intenta enviar el formulario con un mensaje demasiado largo
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "Alberto Morales", "alberto.morales@outlook.com" y "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus imperdiet, nulla et dictum interdum, nisi lorem egestas odio, vitae scelerisque enim ligula venenatis dolor. Maecenas nisl est, ultrices nec congue eget, auctor vitae massa."
    And el usuario presiona el botón "Enviar"
    Then el sistema muestra un mensaje de error indicando que el mensaje excede el número máximo de caracteres permitidos

  Scenario: El usuario llena y envía el formulario por WhatsApp exitosamente
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario llena el formulario con "Lucía García", "lucia.garcia@gmail.com" y "Estoy interesada en el plan de fibra óptica."
    And el usuario presiona el botón "Enviar por WhatsApp"
    Then el sistema envía la información del formulario por WhatsApp
    And el usuario ve un mensaje de confirmación de envío exitoso por WhatsApp

  Scenario: El usuario intenta enviar el formulario por WhatsApp sin llenar todos los campos
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de contacto
    Then el sistema despliega el formulario de contacto
    When el usuario presiona el botón "Enviar por WhatsApp" sin llenar los campos
    Then el sistema muestra un mensaje de error solicitando llenar todos los campos antes de enviar por WhatsApp

