
from algo_coin.util import *


class Wallet(Endpoint):
    def __init__(self, type):
        if not isinstance(type, ExchangeType):
            raise TypeError
        self.type = type

    def get_type(self):
        return self.type

    def APIInit(self, key, secret):
        pass

    def deposit(self, source):
        pass

    def withdraw(self, destination):
        pass