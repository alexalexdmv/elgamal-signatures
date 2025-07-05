import hashlib
from ElGamalKeyPair import ElGamalKeyPair
from math import gcd
import secrets

class ElGamalSignature:

    # Sign a message using ElGamal  signature scheme
    @staticmethod
    def sign(message: str, keypair: ElGamalKeyPair):

        while True:
            p, g, y = keypair.get_public_key()

            x = keypair.get_private_key()

            # Hash the message using SHA-256 and convert to integer
            h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

            # Choose a random k such that 1 < k < p-1 and gcd(k, p-1) = 1
            while True:
                k = secrets.randbelow(p-2) + 1

                if gcd(k, p-1) == 1:
                    break
            
            # Compute r = g^k mod p
            r = pow(g, k, p)

            # Compute modular inverse of k modulo (p-1)
            k_inv = pow(k, -1, p-1)

            # Compute s = k_inv * (H(m) - x * r) mod (p-1)
            s =  pow( ((h - x * r)*k_inv), 1 , p-1)

            # Check if signature is valid
            if s != 0:
                return (r, s)
            
            else:
                continue

    
    # Verify an ElGamal signature
    @staticmethod
    def verify(message: str, signature: tuple, keypair: ElGamalKeyPair):

        p, g, y = keypair.get_public_key()
        r, s = signature

        # Check if r and s are in valid ranges
        if not (0 < r < p) or not (0 < s < p - 1):
            return False

        
        # Hash the message using SHA-256 and convert to integer
        h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

        # Compute g^H(m) mod p
        left = pow(g, h, p)

        # Compute y^r * r^s mod p
        right = pow(y, r, p) * pow(r, s, p) % p

        return left == right



    
     