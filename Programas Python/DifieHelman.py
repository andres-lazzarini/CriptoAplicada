import random
from random import randint

if __name__ == '__main__':

	P = int (input('Ingrese el valor de P: '))
	G = int (input('Ingrese el valor de G:'))
	
	# Se imprimen los valores de P y G
	print('El valor de P es :%d'%(P))
	print('El valor de G es :%d'%(G))
	
	# Se declara a con valor random y se imprime
	a = random.randint(1, P - 1)
	print('La llave privada de Alice es :%d'%(a))

	# Calculo de A = g^a mod p
	Ax = int(pow(G,a,P))
	
	# Se declara b con valor random y se imprime
	b = random.randint(1, P - 1)
	print('La llave privada de Bob es :%d'%(b))

	# Calculo de B= g^b mod p
	By = int(pow(G,b,P))
	
	# Calculo de Ka = B^a mod p y Kb = A^b mod p
	ka = int(pow(By,a,P))
	kb = int(pow(Ax,b,P))
	
	# Se imprimen las llaves 
	print('La Llave secreta de Alice es : %d'%(ka))
	print('La llave secreta de Bob es : %d'%(kb))