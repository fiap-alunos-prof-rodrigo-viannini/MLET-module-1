# main.py
from vehicles.car import Car  # Importa a classe Car do módulo vehicles.car
from vehicles.motorcycle import Motorcycle  # Importa a classe Motorcycle do módulo vehicles.motorcycle
from vehicles.truck import Truck  # Importa a classe Truck do módulo vehicles.truck

def main():
    # Vamos criar um carro BMW X1, uma moto Suzuki GSX-R1000 e um caminhão Mercedes-Benz para o nosso sistema de aluguel de veículos
    carro = Car("BMW", "X1", 2020, 150, 4)  # Cria um objeto Car com marca BMW, modelo X1, ano 2020, velocidade máxima 150 e capacidade 4
    moto = Motorcycle("Suzuki", "GSX-R1000", 2019, 200, 1000)  # Cria um objeto Motorcycle com marca Suzuki, modelo GSX-R1000, ano 2019, velocidade máxima 100 e cilindrada 1000
    caminhao = Truck("Mercedes-Benz", "Actros", 2021, 300, 25000)  # Cria um objeto Truck com marca Mercedes-Benz, modelo Actros, ano 2021, velocidade máxima 300 e capacidade de carga 25000

    # Colocamos todos os veículos em uma lista para simplificar a iteração
    veiculos = [carro, moto, caminhao]

    # Para cada veículo, exibimos suas informações, alugamos, verificamos a disponibilidade e devolvemos
    for veiculo in veiculos:
        print(veiculo.display_info())  # Exibe as informações do veículo
        print(veiculo.rent())  # Simula o aluguel do veículo
        print(veiculo.check_availability())  # Verifica a disponibilidade do veículo
        print(veiculo.return_vehicle())  # Simula a devolução do veículo
        print(veiculo.check_availability())  # Verifica novamente a disponibilidade do veículo
        print()

if __name__ == "__main__":
    main()  # Chama a função principal se este arquivo for executado diretamente
