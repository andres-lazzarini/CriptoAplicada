import random
import math
import numpy as np
from random import randint

def isPrime(n):
  if(n > 1):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
    return True
  else:
    return True

def Claves_RSA():
  ## Se buscan dos números p y q, diferentes y que sean primos
  mi = 151
  ma = 293
  val = False
  while val == False:
    p = randint(mi,ma)
    val = isPrime(p)
  
  val = False
  while val == False:
    q = randint(mi,ma)
    val = isPrime(q)
    if p == q:
      val = False
  
  n   = p*q
  phi = (p-1)*(q-1)

  ## Se calcula e como coprimo de phi
  val = False
  cd = 0
  while cd != 1 or val == False:
    n1 = randint(2,n)
    e  = randint(2,n1)
    val = isPrime(e)
    cd = math.gcd(e, phi)
  
  ## Se calcula d, inversio de e en mod phi
  val = 0
  d = 0
  while val != 1:
    d = d + 1
    val = np.mod(d*e, phi)
  
  ## Se imprimen las llaves
  print('La llave pública es (e = ', e, ', n = ', n, ')')
  print('La llave privada es (d = ', d, ', n = ', n, ')')
  
  return e, n, d


def cifra_RSA(texto, n, e):
  m1 = [ord(k) for k in texto]
  c1 = np.zeros(len(m1))
  for i in np.arange(len(m1)):
    m = m1[i]
    diff = 0
    if m > n:
      diff = m - n + 1
    m = m - diff
    qm = bin(e)
    c = 1
    for x in np.arange(len(qm)):
      if qm[x] == '1':
        c = np.mod(np.mod(c**2,n)*m,n)
      elif qm[x] == '0':
        c = np.mod(c**2,n)
    c1[i] = c
  
  cifrado = ""
  for i in np.arange(len(c1)):
    cifrado = cifrado + chr(int(c1[i]))
  
  print('El texto cifrado es: ', cifrado)
  return cifrado

def descifra_RSA(cifrado, n, d):
  m1 = [ord(k) for k in cifrado]
  c1 = np.zeros(len(m1))
  for i in np.arange(len(m1)):
    m = m1[i]
    diff = 0
    if m > n:
      diff = m - n + 1
    qm = bin(d)
    c = 1
    for x in np.arange(len(qm)):
      if qm[x] == '1':
        c = np.mod(np.mod(c**2,n)*m, n)
      elif qm[x] == '0':
        c = np.mod(c**2, n)
    c1[i] = c + diff
  
  descifrado = ""
  for i in np.arange(len(c1)):
    descifrado = descifrado + chr(int(c1[i]))
  
  print('El texto descifrado es: ', descifrado)
  return descifrado

# e, n, d = Claves_RSA()
# cifrado = cifra_RSA('El texto a cifrar', n, e)
# descifrado = descifra_RSA(cifrado, n, d)