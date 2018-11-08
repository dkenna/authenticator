from ecdsa import SigningKey, NIST384p
from ecdsa.util import randrange_from_seed__trytryagain
from binascii import hexlify, unhexlify
#from jose import jwk
#from jose.utils import base64url_decode
import sys


'''
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
private_key = ec.generate_private_key( ec.SECP384R1(), default_backend()  )
print(dir(private_key))
print(private_key.private_numbers().public_numbers)
'''

seed = b'50db965ca9a96ac58dc757f9f79f8135c323080f105eb1f43c05ea38b9b90cde232bd7c938e960f90974fb42f981e458'
secexp = randrange_from_seed__trytryagain(unhexlify(seed), NIST384p.order)
ecdsa_key = SigningKey.from_secret_exponent(secexp, curve=NIST384p)
ecdsa_pub = ecdsa_key.get_verifying_key()
rsa_key = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
"""
rsa_pub = """ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDp9BbX0M0Nqk5c8mdFMcZrlOB5NX93sqnTAzZVWPxoaLmIWXk8eHJuE5MBN9cJZ53E4Zgweog/MIhG/+Cx4wNquKODjkq5ykkItuuVpQzWGmZECnqSr6l+oTC334QDT0PR3DkcxtelC9jbLpu7EjanRJkXGR/CXUN9bQpBCyy7Cdbc6K8R6FcFi8szRnApuEx9Vk4t3U2HdWlhRQrxHmHrFq3vLAoD8MyCEBegV8CXC7ggDMd3A0d8WLlajLdANergS+3ASkABlZwg0hHqVCAGFw6AUGvX3QoU3Nb1ZcL0WXF7oZQRoPsvjYwFJLAcyTQB27W+x1TQ/4pC7i3xkTSyslEreYklMX6pK02eK9EyhmjMIgH8+TdoGKqAYrL8IS6+3/+IMDjBWL6atd7z9c1x81SSdLuBFFWfNZVw+91+/qZf1e48LSpHxgUhegpEvJnokzHjz92dUkVbTfocWIxzAhNyFdx9fIzWfH8uWORrS//f8UBnD9GehBk2EYbyIFGCPuqInfpJKbl44NPM2pejOsDZRWyE0GUS47tVos6xKjkpZLY5q9AEMX7Sn7Ue7Tq+bmupbHLPPQX14B72HoG9oUkTS/2kuG0uLhp1V4aPV59Fy1L0ZF4F0LZY0VQw0JEmnkfkSXG+UozzBhVBDvi/S/DXFLy5mhiRYXKkdDTWUw== dkenna@MacBook-Pro.local"""

"""print(hexlify(key.to_string()))
print(hexlify(pub.to_string()))
print(dir(key))
print(dir(pub))"""
#print(jsonpickle.encode(pub))
#sys.exit()

class KeyGenerator:
    def make_key(seed):
        secexp = randrange_from_seed__trytryagain(seed, NIST384p.order)
        key = SigningKey.from_secret_exponent(secexp, curve=NIST384p)
        pub = key.get_verifying_key()
        return (key,pub)
