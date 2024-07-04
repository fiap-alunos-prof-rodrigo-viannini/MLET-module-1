class Passenger:
    # O arquivo core/passenger.py define a classe Passenger que representa o passageiro.
    def __init__(self, name: str, origin: str, destination: str):
        # Inicializa o nome do passageiro, origem e destino da viagem
        self.name = name
        self.origin = origin
        self.destination = destination

    def __str__(self):
        # Retorna uma string representando o passageiro e sua viagem
        return f"{self.name} está viajando de {self.origin} para {self.destination}."





