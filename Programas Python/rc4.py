def KSA_PRGA(clave, menlen):
    key = clave
    lkey = len(key)
    k = [0] * lkey
    for i in range(0, lkey):
        k[i] = ord(key[i])
    
    s = [0] * 256

    for i in range(255):
        s[i] = i

    j = 0

    for i in range(255):

        j = ((j + s[i] + k[(i % lkey)]) % 256)

        Stemp = s[j]
        s[j] = s[i]
        s[i] = Stemp

    i = 0
    j = 0

    b = [0] * menlen

    x = 0
    while (x < menlen):
        i = (i + 1) % 256
        j = (j + s[i]) % 256

        Stem = s[j]
        s[j] = s[i]
        s[i] = Stem

        b[x] = s[(s[i] + s[j]) % 256]

        x += 1

    return b

def cifra_rc4(mensaje, clave):
    resultado = ""

    b = KSA_PRGA(clave, len(mensaje))

    z = [0] * len(b)
    c = [0] * len(mensaje)

    for k in range(len(c)):
        c[k] = ord(mensaje[k])
    

    for y in range(len(z)):

        o = b[y]
        p = c[y]

        z[y] = (o ^ p)

    for i in range(len(mensaje)):
        resultado += hex(z[i]) + " "; 

    return resultado

def descifra_rc4(mensaje, clave):
        resultado = ""
        
        palSplit = mensaje.split()
        
        b = KSA_PRGA(clave, len(palSplit))

        z = [0] * len(b)
        c = [0] * len(palSplit)
        
        for k in range(len(c)):
            c[k] = int(palSplit[k], base=16)

        for y in range(len(z)):

            o = b[y]
            p = c[y]

            z[y] = (o ^ p)

        for i in range(len(palSplit)):
            resultado += chr(z[i])

        return resultado    