# Documentação do Uber Simulator

O Uber Simulator é um projeto em Python que permite aos desenvolvedores simular o processo de uma viagem de Uber de forma detalhada, desde a criação de motoristas e passageiros até o cálculo de tarifas e simulação do ciclo de vida de uma viagem.

# Funcionalidades

1. Motorista:
   Cada motorista é representado por uma instância da classe `Driver`. Eles têm um nome, modelo do carro e podem estar disponíveis ou ocupados. O projeto permite verificar o status do motorista e alterar sua disponibilidade conforme necessário.

2. Passageiro:
   Os passageiros são representados por uma instância da classe `Passenger`. Cada passageiro possui um nome, origem e destino da viagem. O projeto oferece a funcionalidade de criar novos passageiros e registrar detalhes completos de suas viagens.

3. Viagem:
   A classe `Trip` é essencial para simular uma jornada específica entre um motorista e um passageiro. Antes de iniciar a viagem, o sistema verifica a disponibilidade do motorista e inicia o registro da viagem. A distância da viagem é inserida como entrada e usada para calcular a tarifa com base no preço do combustível por quilômetro.

4. Simulação de Viagem:
   Para replicar o fluxo de uma viagem real, o Uber Simulator calcula o tempo estimado de viagem com base na distância fornecida e na velocidade média definida. Após a simulação, o projeto registra o tempo estimado de viagem e conclui o ciclo de vida da viagem de forma precisa.

# Utilização

Para aproveitar ao máximo o Uber Simulator, siga estes passos simples:

1. Configuração Inicial:
   - Verifique se as classes `Driver`, `Passenger` e `Trip` estão corretamente implementadas e acessíveis dentro do diretório do projeto.

2. Execução do Script:
   - Execute o script `simulation.py` em um ambiente compatível com Python.
   - Ao solicitar, insira a distância da viagem em quilômetros para iniciar a simulação.

3. Simulação da Viagem:
   - O projeto iniciará a viagem simulada, calculando o tempo necessário com base na distância fornecida e na velocidade média configurada.

4. Visualização dos Resultados:
   - Durante a execução do script, observe como o Uber Simulator imprime o tempo estimado de viagem e atualiza o status do motorista de acordo com o ciclo de vida simulado da viagem.

# Simulador de Viagem

Abaixo está o código que você pode executar para iniciar a simulação de uma viagem utilizando o Uber Simulator:

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
