from ElGamalKeyPair import ElGamalKeyPair
from ElGamalSignature import ElGamalSignature
from User import User
from Transaction import Transaction
import secrets

def test_elgamal_signature_and_transaction():
    # Generate keypairs
    keypair_sender = ElGamalKeyPair.generate_keypair(512)
    keypair_receiver = ElGamalKeyPair.generate_keypair(512)

    # Create users with initial balances
    sender = User("Alice", keypair_sender, balance=1000)
    receiver = User("Bob", keypair_receiver, balance=500)

    # Prepare a message and sign it
    amount = 200
    message = f"{sender.username}->{receiver.username}:{amount}"
    
    # Sign the message
    signature = sender.sign_message(message)

    # Create transaction with valid signature and sufficient funds
    transaction = Transaction(sender, receiver, amount)

    print("Test 1: Valid transaction execution")
    assert transaction.is_valid(), "Signature should be valid!"
    assert transaction.execute(), "Transaction should succeed!"
    assert sender.balance == 800, f"Sender balance should be 800 but is {sender.balance}"
    assert receiver.balance == 700, f"Receiver balance should be 700 but is {receiver.balance}"

    print("Test 2: Double spending prevention")
    # Try to execute again - should fail
    assert not transaction.execute(), "Transaction should not execute twice!"

    print("Test 3: Invalid signature detection")
    # Tamper with message to invalidate signature
    fake_message = f"{sender.username}->{receiver.username}:{amount + 100}"
    fake_signature = signature
    assert not ElGamalSignature.verify(fake_message, fake_signature, sender.keypair), "Tampered message should invalidate signature!"

    print("Test 4: Insufficient funds")
    # Create transaction with amount greater than balance
    large_amount = 10000
    transaction2 = Transaction(sender, receiver, large_amount)
    assert transaction2.is_valid(), "Signature should be valid!"
    assert not transaction2.execute(), "Transaction should fail due to insufficient funds!"

    print("Test 5: Fake (random) signature rejection")
    # Use a completely fake random signature on a valid message
    fake_sig = (secrets.randbelow(keypair_sender.p), secrets.randbelow(keypair_sender.p - 1))
    assert not ElGamalSignature.verify(message, fake_sig, sender.keypair), "Verification should fail for a completely fake signature!"

    print("All tests passed!")

if __name__ == "__main__":
    test_elgamal_signature_and_transaction()
