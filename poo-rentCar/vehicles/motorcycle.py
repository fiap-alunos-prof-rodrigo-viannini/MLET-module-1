# veiculos/moto.py
from vehicles.vehicles import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, daily_price, displacement):
        super().__init__(brand, model, year, daily_price)
        self._displacement = displacement  # Cilindradas da motocicleta em cc

    def display_info(self):
        base_info = super().display_info()  # Calls the display_info method from the base class
        return f"{base_info}, Displacement: {self._displacement}cc"  # Returns base class information and displacement
