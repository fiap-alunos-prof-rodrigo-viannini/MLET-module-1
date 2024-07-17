# veiculos/caminhao.py
from vehicles.vehicles import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, daily_price, cargo_capacity):
        super().__init__(brand, model, year, daily_price)
        self._cargo_capacity = cargo_capacity  # Capacidade de carga em quilogramas

    def display_info(self):
        base_info = super().display_info()  # Obtém informações da classe pai
        return f"{base_info}, Cargo Capacity: {self._cargo_capacity}kg"  # Retorna informações completas com a capacidade de carga
