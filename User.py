from ElGamalKeyPair import ElGamalKeyPair
from ElGamalSignature import ElGamalSignature

# Represents a user participating in a transaction with the ability to sign and verify those transactions
class User:
    def __init__(self, username: str, keypair: ElGamalKeyPair, balance: float = 0.0):
        self.username = username
        self.keypair = keypair
        self.balance = balance

    def sign_message(self, message: str):

        return ElGamalSignature.sign(message, self.keypair)

    def verify_signature(self, message: str, signature: tuple):

        return ElGamalSignature.verify(message, signature, self.keypair)

    def get_public_key(self):

        return self.keypair.get_public_key()

    def has_sufficient_balance(self, amount: float) -> bool:

        return self.balance >= amount

    def subtract_balance(self, amount: float):

        self.balance -= amount

    def add_balance(self, amount: float):

        self.balance += amount
