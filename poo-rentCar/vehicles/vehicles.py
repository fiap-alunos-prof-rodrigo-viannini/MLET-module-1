"""
1. Abstração
Definição:
A abstração permite que você se concentre nos aspectos essenciais de um objeto em vez de todos os seus detalhes.
É a ideia de criar uma classe que representa um conceito genérico.

No código:

A classe Vehicle é uma abstração de qualquer veículo. Contém atributos comuns a todos os veículos, como marca,
modelo, ano e preço diário.


---

2. Encapsulamento
Definição:
O encapsulamento é o princípio de esconder os detalhes internos de um objeto e expor apenas o que é necessário.
Isso é feito protegendo atributos e fornecendo métodos para acessá-los e modificá-los.

No código:

Atributos como _brand, _model, _year, _daily_price e _available são protegidos (indicado pelo underscore).
Métodos como check_availability, rent e return_vehicle fornecem uma interface controlada para interagir com esses atributos.
"""

class Vehicle:
    def __init__(self, brand, model, year, daily_price):
        self._brand = brand  # Atributo que armazena a marca do carro
        self._model = model  # Atributo que armazena o modelo do carro
        self._year = year  # Atributo que armazena o ano de fabricação do carro
        self._daily_price = daily_price  # Atributo que armazena o preço diário de aluguel do carro
        self._available = True  # Atributo que indica se o carro está disponível para aluguel

    def display_info(self):
        return f"Marca: {self._brand}, Modelo: {self._model}, Ano: {self._year}, Preço por dia: R${self._daily_price}"

    def check_availability(self):
        return self._available

    def rent(self):
        if self._available:
            self._available = False
            return f"{self._brand} {self._model} foi alugado com sucesso!"
        else:
            return f"{self._brand} {self._model} não está disponível."

    def return_vehicle(self):
        self._available = True
        return f"{self._brand} {self._model} foi devolvido com sucesso!"
