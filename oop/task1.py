class BankAccount:
    """
    Банковский счет с возможностью пополнения и снятия денег.
    В логике этого класса счет может быть только положительным.
    """
    def __init__(self, balance: int) -> None:
        self.__validate_amount(balance)
        self.__balance = balance

    def deposit(self, amount: int) -> None:
        self.__validate_amount(amount)
        self.__balance += amount

    def withdraw(self, amount: int) -> None:
        self.__validate_amount(amount)
        if amount > self.__balance:
            raise ValueError("Недостаточно средств.")
        self.__balance -= amount
    
    def get_balance(self) -> int:
        return self.__balance
    
    def __validate_amount(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise ValueError("Сумма/баланс должны быть целым числом.")
        if amount <= 0:
            raise ValueError("Сумма/баланс должны быть положительными.")
