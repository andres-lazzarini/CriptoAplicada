import os
import time
import rsa
import aes

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

    op = int (input('Seleccione una opcion de las de arriba: '))

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

        opc = int (input('Seleccione una opcion de las de arriba: '))

        if opc == 1:
            os.system('cls')
            print('op2')
        elif opc == 2: 
            os.system('cls')
            print('op2')
        elif opc == 3: 
            os.system('cls')
            men = input("DIgite mensaje a encriptar: ")
            key = input("\nDigite la llave: ")
            salida = aes.encrypt(key, men)
            print("\n\nMensaje encriptado: ", salida)
            sal = salida.decode(encoding='UTF-8',errors='ignore')
            print("Mensaje encriptado: ",sal)
            input("")
        elif opc == 4: 
            os.system('cls')
            print('op2')
        elif opc == 5: 
            os.system('cls')
            print('op2')
        elif opc == 6: 
            os.system('cls')
            e, n, d = rsa.Claves_RSA()
            texto = str(input('Ingrese el texto a cifrar: '))
            cifrado = rsa.cifra_RSA(texto, n, e)
            time.sleep(1)
        elif opc == 7: 
            os.system('cls')
            print('op2')
        elif opc == 8: 
            os.system('cls')
            exec(open("DifieHelman.py").read())
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
            print('op2')
        elif opd == 2: 
            os.system('cls')
            print('op2')
        elif opd == 3: 
            os.system('cls')
            men = input("DIgite mensaje a desencriptar ")
            key = input("\nDigite la llave: ")
            salida = aes.decrypt(key, men)
            input("")
            print("Mensaje desencriptado: ", salida)
            input("")
        elif opd == 4: 
            os.system('cls')
            print('op2')
        elif opd == 5: 
            os.system('cls')
            print('op2')
        elif opd == 6: 
            os.system('cls')
            textoc = str(input('Ingrese el texto a descifrar: '))
            n = int(input('Ingrese la n: '))
            d = int(input('Ingrese la d: '))
            descifrado = rsa.descifra_RSA(textoc, n, d)
            time.sleep(1)
        elif opd == 7: 
            os.system('cls')
            print('op2')
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