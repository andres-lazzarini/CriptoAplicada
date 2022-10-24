import random
import json
from math import pow

a=random.randint(2,10)

# funcion gcd maximo comun divisor
def gcd(a,b):
    if a<b:
        return gcd(b,a)
    elif a%b==0:
        return b
    else:
        return gcd(b,a%b)

# Funcion de generacion de claves
def gen_key(q):
    key= random.randint(pow(10,20),q)
    while gcd(q,key)!=1:
        key=random.randint(pow(10,20),q)
    return key

# funcion de powermod
def power(a,b,c):
    x=1
    y=a
    while b>0:
        if b%2==0:
            x=(x*y)%c
        y=(y*y)%c
        b=int(b/2)
    return x%c

def encryption(msg,q,h,g):
    ct=[]
    # se generan las claves
    k=gen_key(q)
    # se hacen los powermod
    s=power(h,k,q)
    p=power(g,k,q)

    # Se agrega cada caracter del mensaje a ct
    for i in range(0,len(msg)):
        ct.append(msg[i])
    # se multiplica cada caracter ct por s
    for i in range(0,len(ct)):
        ct[i]=s*ord(ct[i])
    return ct,p

def decryption(ct,p,key,q):
    # se convierte el ct string a list en res
    res = json.loads(ct)

    pt=[]
    # se hace un powermod para h
    h=power(p,key,q)
    
    # se hace la division de cada valor res entre h y se convierte a caracter
    for i in range(0,len(res)):
        pt.append(chr(int(res[i]/h)))
    return pt
