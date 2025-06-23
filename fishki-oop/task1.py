class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__logs = []
        return cls.__instance

    def log(self, message: str) -> None:
        self.__logs.append(message)

    def get_logs(self) -> list[str]:
        return self.__logs


logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]
