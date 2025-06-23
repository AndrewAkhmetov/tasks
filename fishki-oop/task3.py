from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPaymentProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Processing credit card payment of {amount} dollars"


class PayPalPaymentProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Processing PayPal payment of {amount} dollars"


class CryptoPaymentProcessor(PaymentProcessor):
    def pay(self, amount: float ) -> str:
        return f"Processing crypto payment of {amount} dollars"
