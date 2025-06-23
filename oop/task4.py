from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self) -> str:
        pass

    @abstractmethod
    def stop_engine(self) -> str:
        pass

    @abstractmethod
    def move(self) -> str:
        pass


class Car(Transport):
    def start_engine(self) -> str:
        return "Двигатель машины запущен"

    def stop_engine(self) -> str:
        return "Двигатель машины остановлен"

    def move(self) -> str:
        return "Машина движется"


class Boat(Transport):
    def start_engine(self) -> str:
        return "Двигатель лодки запущен"

    def stop_engine(self) -> str:
        return "Двигатель лодки остановлен"

    def move(self) -> str:
        return "Лодка движется"
