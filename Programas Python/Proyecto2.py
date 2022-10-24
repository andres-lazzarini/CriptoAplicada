import os
import time
import rsa
import des 
import rc4
import aes
import ElGamal
import random
import Chacha
import Salsa
import DifieHelman

while True:

    print('------------------------------------------------------')
    print('    ____                             __           ___ ')
    print("   / __ \_________  __  _____  _____/ /_____     |__ \\")
    print('  / /_/ / ___/ __ \/ / / / _ \/ ___/ __/ __ \    __/ /')
    print(' / ____/ /  / /_/ / /_/ /  __/ /__/ /_/ /_/ /   / __/ ')
    print('/_/   /_/   \____/\__, /\___/\___/\__/\____/   /____/ ')
    print('                 /____/                               ')
    print('                                                      ')
    print('------------------------------------------------------')

    print('------------------------------------------------------')
    print('-------- Cifrado y Descifrado de Informacion ---------')
    print('------------------------------------------------------')

    print('¿Que Tu Quiere Hacer?')
    print('1. Cifrar')
    print('2. Descifrar')
    print('0. Salir')

    op = int(input('Seleccione una opcion de las de arriba: '))

    if op == 1: 
        os.system('cls')
        print('---------------------------------------------------')
        print('-------                CIFRAR               -------')
        print('---------------------------------------------------')
        print('¿Con Que Quieres Cifrar?')
        print('1. RC4')
        print('2. DES')
        print('3. AES')
        print('4. ChaCha20')
        print('5. Salsa20')
        print('6. RSA')
        print('7. ElRamal')
        print('8. Diffie Hellman')

        opc = int(input('Seleccione una opcion de las de arriba: '))

        if opc == 1:
            os.system('cls')
            msg = input("Ingrese un mensaje: ")
            clave = input("Ingrese una clave: ")
            cifrado  = rc4.cifra_rc4(msg, clave)
            print(cifrado)
            time.sleep(1)
        elif opc == 2: 
            os.system('cls')
            texto = str(input("Ingrese el texto a cifrar: "))
            cifrado = des.cifra_des(texto)
            print("El texto cifrado es: ", cifrado)
            time.sleep(1)
        elif opc == 3: 
            os.system('cls')
            men = input("DIgite mensaje a encriptar: ")
            llave = input("\nDigite la llave: ")
            mencifrado = aes.encrypt(llave, men)
            print("\n\nMensaje encriptado: ", mencifrado)
            time.sleep(1)
        elif opc == 4: 
            os.system('cls')
            texto = input("Ingrese un texto: ")
            cifrado, key, nonce = Chacha.cifra_chacha(texto)
            print("El texto cifrado es: ", cifrado)
            print("El texto key es: ", key)
            print("El texto nonce es: ", nonce)
            time.sleep(1)
        elif opc == 5: 
            os.system('cls')
            texto = input("Ingrese un texto: ")
            scifrado, skey, snonce = Salsa.cifra_salsa(texto)
            print("El texto cifrado es: ", scifrado)
            print("El texto key es: ", skey)
            print("El texto nonce es: ", snonce)
            time.sleep(1)
        elif opc == 6: 
            os.system('cls')
            e, n, d = rsa.Claves_RSA()
            texto = str(input('Ingrese el texto a cifrar: '))
            cifrado = rsa.cifra_RSA(texto, n, e)
            time.sleep(1)
        elif opc == 7: 
            os.system('cls')
            msg = input("Ingrese un mensaje: ")
            q = random.randint(pow(10, 20), pow(10, 50))
            print("q: ",q)
            g = random.randint(2, q)
            key = ElGamal.gen_key(q)
            print("Key: ",key)
            h = ElGamal.power(g, key, q)
            ct, p = ElGamal.encryption(msg, q, h, g)
            print("Mensaje encriptado: ", ct)
            print("P: ",p)
            time.sleep(1)
        elif opc == 8: 
            os.system('cls')
            DifieHelman.difie_helman()
            time.sleep(1)
        else: 
            os.system('cls')
            print('¡¡¡Opcion Invalida!!!')

    elif op == 2: 
        os.system('cls')
        print('---------------------------------------------------')
        print('-------             DESCIFRAR               -------')
        print('---------------------------------------------------')
        print('¿Con Que Quieres Descifrar?')
        print('1. RC4')
        print('2. DES')
        print('3. AES')
        print('4. ChaCha20')
        print('5. Salsa20')
        print('6. RSA')
        print('7. ElRamal')

        opd = int(input('Seleccione una opcion de las de arriba: '))

        if opd == 1:
            os.system('cls')
            cmsg = input("Ingrese un mensaje: ")
            clave = input("Ingrese una clave: ")
            descifrado = rc4.descifra_rc4(cmsg, clave)
            print("El mensaje descifrado es: ", descifrado)
            time.sleep(1)
        elif opd == 2: 
            os.system('cls')
            texto = str(input("Ingrese el texto a descifrar: "))
            descifrado = des.descifra_des(texto)
            print("El texto descifrado es: ", descifrado)
            time.sleep(1)
        elif opd == 3: 
            os.system('cls')
            menCifrado = str(input("DIgite mensaje a descifrar: "))
            llave = input("\nDigite la llave: ")
            mendescifrado = aes.decrypt(llave, mencifrado)
            print("Mensaje desencriptado: ", mendescifrado)
            time.sleep(1)
        elif opd == 4: 
            os.system('cls')
            Cifrado = input("Ingrese el texto cifrado: ")
            Key = input("Ingrese el key: ")
            Nonce = input("Ingrese el Nonce: ")
            Chacha.decifra_chacha(key, nonce, cifrado)
            time.sleep(1)
        elif opd == 5: 
            os.system('cls')
            Scifrado = input("Ingrese el texto cifrado: ")
            Skey = input("Ingrese el key: ")
            Snonce = input("Ingrese el Nonce: ")
            Salsa.descifra_salsa(skey, snonce, scifrado)
            time.sleep(1)
        elif opd == 6: 
            os.system('cls')
            textoc = str(input('Ingrese el texto a descifrar: '))
            n = int(input('Ingrese la n: '))
            d = int(input('Ingrese la d: '))
            descifrado = rsa.descifra_RSA(textoc, n, d)
            time.sleep(1)
        elif opd == 7: 
            ct = input("Ingrese el mensaje cifrado: ")
            p = int(input("ingrese la P: "))
            q = int(input("ingrese la q: "))
            key = int(input("ingrese la llave: "))
            pt=ElGamal.decryption(ct,p,key,q)
            d_msg=''.join(pt)
            print("Mensaje Decifrado: ",d_msg)
            time.sleep(1)
        else: 
            os.system('cls')
            print('¡¡¡Opcion Invalida!!!')

    elif op == 0:
        os.system('cls')
        print('Saliendo...')
        break
    else:
        os.system('cls')
        print('¡¡¡Opcion Invalida!!!')