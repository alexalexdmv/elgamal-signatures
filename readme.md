
# ElGamal Signature Scheme

  

This project implements ElGamal signatures and a demonstrational use case that simulates bank transactions.


---

## Files Overview

- `crypto_utils.py`  
  Utility functions for primes and generators

- `ElGamalKeyPair.py`  
  ElGamal key pair generation and access

- `ElGamalSignature.py`  
  Message signing and verification

- `miller_rabin_test.py`  
  Probabilistic primality testing with Miller-Rabin algorithm.

- `Transaction.py`  
  Transaction handling between users

- `User.py`  
  User class with balance and signature handling
  
 - `test.py`  
  Test cases for the overall system
  

---  

##  Test Scenarios

  

The following cases are tested in `test.py`:

  

* Valid transaction with correct signature

* Prevention of double execution (double spending)

* Detection of tampered messages with valid signature

* Handling transactions with insufficient funds

* Rejection of completely fake (random) signatures

  

---

  

##  Notes

  

* The ElGamal signature scheme relies on the discrete logarithm problem.

* The message, which needs to be signed, is hashed with SHA-256. A different hashing function can also be used, however ensure the output bit-length of the hashing function is less than the bit-length of prime p.

* Since generating large primes is computationally expensive, the bit-length of the prime number can be reduced. To do so, the `generating_keypair` method in `ElGamalKeyPair` needs to be adjusted. Note that smaller key sizes are more insecure.

* The code is commented in detail. Reading through the comments will provide insight into the mathematical, logical, and cryptographic principles behind the ElGamal signature scheme.

* This implementation should only be used for educational purposes. 

---
