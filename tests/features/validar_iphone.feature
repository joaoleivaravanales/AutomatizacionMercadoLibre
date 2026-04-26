Feature: Busqueda de Iphone y validacion de textos

  Scenario Outline: Buscar iphone en MercadoLibre
    Given el usuario está en la pagina principal
    When busca el producto "<producto>"
    And Presiono en el primer resultado
    Then Verifico que el titulo del producto sea "<titulo>"

  Examples:
    | producto | titulo                                                         |
    | iphone   | Apple iPhone 16e (128 Gb) - Blanco - Distribuidor Autorizado   |