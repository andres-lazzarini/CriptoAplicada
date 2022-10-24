import numpy as np

def cifra_des(texto):

    splitat = 4
    # Se separa el texto en 2
    left, right = texto[:splitat], texto[splitat:]

    # print(left)
    # print(right)
    # se declaran las 16 llaves
    k = ['hola', 'pelo', 'caca', 'pana', 'pena', 'milf', 'love', 'gege', 'jaja', 'yolo', 'papa', 'mama', 'bebe', 'baby', 'palo', 'pala']

    # Se convierten las partes en bytes
    righto = np.frombuffer(bytes(right, 'ascii'), dtype=np.uint8)
    lefto = np.frombuffer(bytes(left, 'ascii'), dtype=np.uint8)

    # print(lefto, righto)

    # ciclo para las 16 rondas
    for i in range(16):

        # se pasa la llave i a bytes
        ko = np.frombuffer(bytes(k[i], 'ascii'), dtype=np.uint8)

        # Se hacen la operaciones de XOR y se intercambian valores de la red
        temp = ko ^ righto
        rightTemp = righto
        righto = temp ^ lefto
        lefto = rightTemp

    # print(lefto, righto)

    # se regresan los valores de bytes a caracteres
    l = np.array(lefto, dtype='b').tobytes().decode("ascii")
    r = np.array(righto, dtype='b').tobytes().decode("ascii")

    # se juntan las dos partes 
    cifrado = l + r
    return cifrado

def descifra_des(texto):

    splitat = 4
    # Se separa el texto en 2
    left, right = texto[:splitat], texto[splitat:]

    # print(left)
    # print(right)
    # se declaran las 16 llaves
    k = ['hola', 'pelo', 'caca', 'pana', 'pena', 'milf', 'love', 'gege', 'jaja', 'yolo', 'papa', 'mama', 'bebe', 'baby', 'palo', 'pala']

    # Se convierten las partes en bytes
    righto = np.frombuffer(bytes(right, 'ascii'), dtype=np.uint8)
    lefto = np.frombuffer(bytes(left, 'ascii'), dtype=np.uint8)

    # print(lefto, righto)

    # Se hace el ciclo de 16 rondas, ahora al reves
    for i in range(15, -1, -1):

        # se pasa la llave i a bytes
        ko = np.frombuffer(bytes(k[i], 'ascii'), dtype=np.uint8)
        # se hacen las operaciones de XOR en sentido opuesto y se intercambian valores
        temp = ko ^ lefto
        leftTemp = lefto
        lefto = temp ^ righto
        righto = leftTemp

    # print(lefto, righto)

    # Se regresan los bytes a caracteres
    l = np.array(lefto, dtype='b').tobytes().decode("ascii")
    r = np.array(righto, dtype='b').tobytes().decode("ascii")

    # se juntan las dos partes
    descifrado = l + r
    return descifrado