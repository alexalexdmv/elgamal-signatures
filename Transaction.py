from User import User

class Transaction:
    def __init__(self, sender: User, receiver: User, amount: float):
        
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.message = f"{sender.username}->{receiver.username}:{amount}"
        self.signature = sender.sign_message(self.message)
        self.executed = False

    # Verifies the digital signature using the sender's public key
    def is_valid(self):

        return self.sender.verify_signature(self.message, self.signature)

    def execute(self):

        # Prevent double spending
        if self.executed:

            return False  

        # Check if the signature is valid before proceeding
        if not self.is_valid():

            print("Invalid signature.")

            return False
        # Ensure the sender has enough balance to send the amount
        if not self.sender.has_sufficient_balance(self.amount):

            print("Insufficient funds.")

            return False

        # Deduct the amount from the sender's balance
        self.sender.subtract_balance(self.amount)

        # Add the amount to the receiver's balance
        self.receiver.add_balance(self.amount)

        # Mark the transaction as completed
        self.executed = True

        return True
