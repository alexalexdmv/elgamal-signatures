import crypto_utils
import secrets


class ElGamalKeyPair:

    def __init__(self, p, g, x, y):
        self.p = p
        self.g = g
        self.__x = x
        self.y = y

    # Generate Elgamal key pair
    @classmethod
    def generate_keypair(cls, bit_length):

        # Enforce a large minimum bit length
        if bit_length < 512:
            bit_length = 512

        min_val = 1 << (bit_length - 1)
        max_val = (1<< bit_length) - 1

        # Compute large safe prime modulo p
        p, q = crypto_utils.generate_safe_prime(min_val, max_val)

        # Compute generator of the multiplicative group Z_p^*
        g = crypto_utils.find_generator(p, q)

        # Choose a random x < p-2, which will serve as the private key
        x = secrets.randbelow(p-2)

        # Compute the public key y
        y = pow(g, x, p)

        return cls(p, g, x, y)
    
    # Retrieve the public key
    def get_public_key(self):
        return (self.p, self.g, self.y)

    # Retrieve the private key
    def get_private_key(self):
        return self.__x
    
