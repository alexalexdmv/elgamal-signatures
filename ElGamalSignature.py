import hashlib
import ElGamalKeyPair

class ElGamalSignature:

    def __init__(self, keypair: ElGamalKeyPair):

        self.p = keypair.p
        self.g = keypair.g
        self.__x = keypair.__x
        self.y = keypair.y

    
     