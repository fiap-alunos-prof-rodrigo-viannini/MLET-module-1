class Driver:
    # O arquivo core/driver.py define a classe Driver que representa o motorista.
    def __init__(self, name: str, car: str):
        # Inicializa o nome do motorista e o carro que ele dirige
        self.name = name
        self.car = car
        self.available = True  # Define o status do motorista como disponível

    def __str__(self):
        # Retorna uma string representando o motorista e seu status
        status = 'disponível' if self.available else 'ocupado'
        return f"{self.name} está dirigindo um {self.car} e está atualmente {status}."

