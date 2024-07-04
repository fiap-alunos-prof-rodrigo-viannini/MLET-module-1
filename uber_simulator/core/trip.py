from core.driver import Driver
from core.passenger import Passenger
import time


class Trip:
    # Preço por quilômetro rodado
    GAS_PRICE_PER_KM = 0.20  # Exemplo de preço do combustível por km em unidades monetárias
    UBER_COMMISSION = 0.25  # Exemplo de comissão do Uber sobre o total da corrida (25%)

    def __init__(self, driver: Driver, passenger: Passenger, distance_km: float):
        # Inicializa o motorista, passageiro e a distância da viagem
        self.driver = driver
        self.passenger = passenger
        self.distance_km = distance_km
        self.start_time = None  # Armazena o tempo de início da viagem
        self.end_time = None  # Armazena o tempo de término da viagem

    def start_trip(self):
        if self.driver.available:
            self.driver.available = False
            self.start_time = time.time()
            print(
                f'Viagem iniciada! {self.passenger.name} está indo de {self.passenger.origin} para {self.passenger.destination}, percorrendo uma distância de {self.distance_km:.2f} km.')

    def end_trip(self):
        self.driver.available = True
        self.end_time = time.time()
        travel_time = self.end_time - self.start_time
        fare, uber_profit, driver_profit = self.calculate_fare()
        print(f'Viagem encerrada! {self.passenger.name} percorreu {self.distance_km:.2f} km em {travel_time:.2f} minutos.')
        print(f'Valor total da viagem: R$ {fare:.2f}')
        print(f'Parte do Uber: R$ {uber_profit:.2f}')
        print(f'Parte do motorista: R$ {driver_profit:.2f}')

    def calculate_fare(self):
        fare = self.distance_km * self.GAS_PRICE_PER_KM    # Calcular o valor da corrida
        uber_profit = fare * self.UBER_COMMISSION          # Calcular o lucro do Uber
        driver_profit = fare - uber_profit                 # Calcular o lucro do motorista
        return fare, uber_profit, driver_profit


