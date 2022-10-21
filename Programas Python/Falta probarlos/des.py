import numpy as np

texto = "HolaMund"

def cifra_des(texto):

    splitat = 4
    left, right = texto[:splitat], texto[splitat:]

    # print(left)
    # print(right)

    k = ['hola', 'pelo', 'caca', 'pana', 'pena', 'milf', 'love', 'gege', 'jaja', 'yolo', 'papa', 'mama', 'bebe', 'baby', 'palo', 'pala']

    righto = np.frombuffer(bytes(right, 'ascii'), dtype=np.uint8)
    lefto = np.frombuffer(bytes(left, 'ascii'), dtype=np.uint8)

    # print(lefto, righto)

    for i in range(16):

        ko = np.frombuffer(bytes(k[i], 'ascii'), dtype=np.uint8)
        temp = ko ^ righto
        rightTemp = righto
        righto = temp ^ lefto
        lefto = rightTemp

    # print(lefto, righto)

    l = np.array(lefto, dtype='b').tobytes().decode("ascii")
    r = np.array(righto, dtype='b').tobytes().decode("ascii")

    cifrado = l + r
    return cifrado

def descifra_des(texto):

    splitat = 4
    left, right = texto[:splitat], texto[splitat:]

    # print(left)
    # print(right)

    k = ['hola', 'pelo', 'caca', 'pana', 'pena', 'milf', 'love', 'gege', 'jaja', 'yolo', 'papa', 'mama', 'bebe', 'baby', 'palo', 'pala']

    righto = np.frombuffer(bytes(right, 'ascii'), dtype=np.uint8)
    lefto = np.frombuffer(bytes(left, 'ascii'), dtype=np.uint8)

    # print(lefto, righto)

    for i in range(15, -1, -1):

        ko = np.frombuffer(bytes(k[i], 'ascii'), dtype=np.uint8)
        temp = ko ^ lefto
        leftTemp = lefto
        lefto = temp ^ righto
        righto = leftTemp

    # print(lefto, righto)

    l = np.array(lefto, dtype='b').tobytes().decode("ascii")
    r = np.array(righto, dtype='b').tobytes().decode("ascii")

    descifrado = l + r
    return descifrado

cifrado = cifra_des(texto)
print(cifrado)

descifrado = descifra_des(cifrado)
print(descifrado)