Feature: Apartado de fotos de IMPACTONET

  Scenario: El usuario intenta utilizar el botón "Hablar con Nosotros" sin redirección
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de "Acerca de Nosotros"
    Then el sistema despliega la información sobre la misión y visión de la empresa
    When el usuario presiona el botón "Hablar con Nosotros"
    Then el sistema no redirige a ninguna página
    And el usuario ve un mensaje de error o un mensaje de que la página no está disponible

  Scenario: El usuario no puede visualizar los trabajos realizados
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de "Acerca de Nosotros"
    And el usuario se dirige al sub-apartado de "Trabajos Realizados"
    Then el sistema intenta cargar las imágenes y descripciones de los trabajos realizados
    And el sistema no muestra ninguna imagen ni descripción
    Then el usuario ve un mensaje de error indicando que no se pueden cargar los trabajos realizados

  Scenario: El usuario visualiza errores en la carga de fotos en el apartado "Acerca de Nosotros"
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de "Acerca de Nosotros"
    Then el sistema despliega la información sobre la misión y visión de la empresa
    When el usuario intenta ver fotos relacionadas con la misión y visión
    Then el sistema no carga las fotos correctamente
    And el usuario ve un mensaje de error o fotos rotas

  Scenario: El usuario visualiza correctamente los trabajos realizados
    Given el usuario accede a la página de IMPACTONET
    When el usuario se dirige al apartado de "Acerca de Nosotros"
    And el usuario se dirige al sub-apartado de "Trabajos Realizados"
    Then el sistema carga las imágenes y descripciones de los trabajos realizados
    And el usuario puede ver las imágenes y leer las descripciones de cada trabajo realizado
    And el sistema permite navegar por los trabajos realizados mediante un carrusel interactivo
