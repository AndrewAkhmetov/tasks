from __future__ import annotations


class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> Temperature:
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def celsius(self) -> float:
        return self._celsius

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @staticmethod
    def is_freezing(celsius: float) -> bool:
        return celsius <= 0
