from pydoc import plain
from typing import ByteString
import pure_chacha20
import secrets

# encryption
def cifra_chacha(text):

    plaintext = bytes(text, 'ascii')

    key = secrets.token_bytes(32)
    nonce = secrets.token_bytes(12) # note the 12-byte/96-bit nonce from RFC 7539

    ciphertext = pure_chacha20.chacha20_xor(key, nonce, plaintext)
    # print(key)
    # print(nonce)
    print(ciphertext)

    key2 = int.from_bytes(key, "big") 
    nonce2 = int.from_bytes(nonce, "big") 

    # print(key2)
    # print(nonce2)

    key3 = key2.to_bytes(32, byteorder='big')
    nonce3 = nonce2.to_bytes(12, byteorder='big')

    print("Key: ", key3)
    print("Nonce: ", nonce3)

# decryption
def decifra_chacha(key3, nonce3, ciphertext):
    plaintext = pure_chacha20.chacha20_xor(key3, nonce3, ciphertext)
    print(plaintext.decode("ascii"))


texto = input("Ingrese un texto: ")
key = input("Ingrese la llave: ")
nonce = input("Ingrese el nonce: ")

# cifra_chacha(texto)
decifra_chacha(key, nonce, texto)