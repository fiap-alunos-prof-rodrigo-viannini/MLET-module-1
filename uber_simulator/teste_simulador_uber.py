import sys
import os
import time

# Adiciona o diretório 'C://PROJECTS//FIAP-MLET//uber_simulator//core' ao sys.path
sys.path.append(r"C://PROJECTS//FIAP-MLET//uber_simulator//core")

# Importa as classes Driver, Passenger e Trip do pacote uber_simulator
from driver import Driver
from passenger import Passenger
from trip import Trip

def main():
    # Cria uma instância do Driver (Motorista) com nome e modelo do carro
    driver = Driver("Elyas", "Audi TT")

    # Cria uma instância do Passenger (Passageiro) com nome, origem e destino
    passenger = Passenger(
        name="Maria",
        origin="Av Atlantica",
        destination="Av Salvador Alende"
    )

    # Solicita a distância da viagem em quilômetros ao usuário
    distance_km = float(input("Digite a distância da viagem em quilômetros: "))

    # Cria uma instância da Trip (Viagem) com o motorista, passageiro e distância
    trip = Trip(driver, passenger, distance_km)

    # Inicia a viagem
    trip.start_trip()

    # Calcula o tempo de viagem baseado na distância e na velocidade média
    average_speed_kmh = 50  # Velocidade média em km/h
    travel_time_hours = distance_km / average_speed_kmh  # Tempo de viagem em horas
    travel_time_minutes = travel_time_hours * 60  # Tempo de viagem em minutos

    # Imprime o tempo de viagem esperado
    print(f"Tempo de viagem simulado: {travel_time_minutes:.2f} minutos")

    # Simula o tempo de viagem com uma pausa de 2 segundos
    time.sleep(2)

    # Encerra a viagem
    trip.end_trip()

# Ponto de entrada do script
if __name__ == "__main__":
    main()
