from core.driver import Driver
from core.passenger import Passenger
from core.trip import Trip
import time
import random

def main():
    driver = Driver(
        "Elyas",
        "Audi TT"
    )

    passenger = Passenger(
        name="Maria",
        origin="Av Atlantica",
        destination="Av Salvador Alende"
    )

    # Nesta linha utilizq o codigo que chama a API do Google Maps e calcula a distancia "distance_google_maps"
    # Gera uma distância aleatória entre 5 e 20 km
    distance_km = random.uniform(5, 40)

    trip = Trip(
        driver,
        passenger,
        distance_km
    )

    trip.start_trip()

    # Tempo de espera aleatório entre 1 e 5 segundos
    random_sleep_time = random.uniform(1, 59)
    time.sleep(random_sleep_time)

    trip.end_trip()

if __name__ == "__main__":
    main()

