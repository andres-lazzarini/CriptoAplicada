import pure_salsa20
import secrets

key = secrets.token_bytes(32)
nonce = secrets.token_bytes(8)
plaintext = b"hello world"

# encryption
ciphertext = pure_salsa20.salsa20_xor(key, nonce, plaintext)

print(key)
print(nonce)
print(ciphertext)

key2 = int.from_bytes(key, "big") 
nonce2 = int.from_bytes(nonce, "big") 

print(key2)
print(nonce2)

key3 = key2.to_bytes(32, byteorder='big')
nonce3 = nonce2.to_bytes(8, byteorder='big')

print(key3)
print(nonce3)

# decryption
assert plaintext == pure_salsa20.salsa20_xor(key3, nonce3, ciphertext)
print(plaintext)