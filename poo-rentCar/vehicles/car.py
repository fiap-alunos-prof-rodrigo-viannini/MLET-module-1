"""
3. Herança
Definição:
A herança permite que você crie novas classes a partir de classes existentes, reutilizando código e criando uma
hierarquia de classes.

No código:

Car, Motorcycle e Truck são subclasses de Vehicle. Elas herdam os atributos e métodos da classe Vehicle e
podem adicionar seus próprios atributos e métodos.

---

4. Polimorfismo
Definição:
O polimorfismo permite que você trate objetos de diferentes classes de maneira uniforme. Objetos de diferentes classes
podem ser tratados através de uma interface comum.

No código:

O método exibir_info é polimórfico. Cada subclasse (Car, Motorcycle, Truck) implementa sua própria versão do método
exibir_info, mas todas podem ser chamadas da mesma maneira.
"""

from vehicles.vehicles import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, daily_price, doors):
        super().__init__(brand, model, year, daily_price)
        self._doors = doors  # Atributo que armazena o número de portas do carro

    def display_info(self):
        base_info = super().display_info()  # Obtém as informações básicas da classe pai
        return f"{base_info}, Portas: {self._doors}"  # Adiciona o número de portas às informações

