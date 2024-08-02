from abc import ABC, abstractmethod
from random import choice

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')

class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de popular está buscando o cliente...')

class Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular está buscando o cliente...')

class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo está buscando o cliente...')

class VeiculoFactory(ABC):
    def __init__(self, tipo) -> None:
        self.carro = self. get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: # type: ignore
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()

class ZonaNorteVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo: # type: ignore
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        assert 0, 'Veiculo não exite'

class ZonaSulVeiculoFactory(VeiculoFactory):

    @staticmethod
    def get_carro(tipo: str) -> Veiculo: # type: ignore
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veiculo não exite'

if __name__ == '__main__':
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')
    for i in range(10):
        carro1 = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro1.buscar_cliente()

    print()
    print('ZONA SUL')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
