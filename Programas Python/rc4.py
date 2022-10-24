# Funcion KSA y PRGA
def KSA_PRGA(clave, menlen):
    key = clave
    # longitud de la clave
    lkey = len(key) 

    # Se convierte la clave en un arreglo de caracteres
    k = [0] * lkey
    for i in range(0, lkey):
        k[i] = ord(key[i])
    
    # se declara el arreglo s con una longitud de 256
    s = [0] * 256

    # Se le da valores a s de 0 a 255
    for i in range(255):
        s[i] = i

    # Se inicia j en 0
    j = 0

    # se hace el KSA
    for i in range(255):

        j = ((j + s[i] + k[(i % lkey)]) % 256)

        # Se hacen las permutaciones correspondientes
        Stemp = s[j]
        s[j] = s[i]
        s[i] = Stemp

    # Se inicia i y j en 0
    i = 0
    j = 0

    #Se hace PRGA 
    # se declara el arreglo b con una longitud igual a la del mensaje
    b = [0] * menlen

    # Se inicia x en 0
    x = 0
    # mientras x sea menor a la longitud del mensaje
    while (x < menlen):
        i = (i + 1) % 256
        j = (j + s[i]) % 256

        # se hacen las permutaciones correspondientes
        Stem = s[j]
        s[j] = s[i]
        s[i] = Stem

        # Se guardan valores en b
        b[x] = s[(s[i] + s[j]) % 256]

        x += 1

    return b

def cifra_rc4(mensaje, clave):
    resultado = ""

    # Se genra la b
    b = KSA_PRGA(clave, len(mensaje))

    # se declara Z con longitud de b
    z = [0] * len(b)
    # se declara c con longitud del mensaje
    c = [0] * len(mensaje)

    # Se asignan los valores del mensaje en c
    for k in range(len(c)):
        c[k] = ord(mensaje[k])
    
    # se usa la operacion del XOR entre c y b y se guardan en z
    for y in range(len(z)):

        o = b[y]
        p = c[y]

        z[y] = (o ^ p)

    # Se convierten los valores a hex
    for i in range(len(mensaje)):
        resultado += hex(z[i]) + " "; 

    return resultado

def descifra_rc4(mensaje, clave):
        resultado = ""
        
        # Se separan los valores en hex
        palSplit = mensaje.split()
        
        # Se genera la b
        b = KSA_PRGA(clave, len(palSplit))

        # Se declara z con longitud de b
        z = [0] * len(b)
        # se delcara c con longitud de los valores en hex
        c = [0] * len(palSplit)
        
        # se guardan los valores hex en deciman en c
        for k in range(len(c)):
            c[k] = int(palSplit[k], base=16)

        # se usa el XOR con b y c y se guardan en Z
        for y in range(len(z)):

            o = b[y]
            p = c[y]

            z[y] = (o ^ p)

        # Se convierten los valores en Z a caracteres
        for i in range(len(palSplit)):
            resultado += chr(z[i])

        return resultado    