def invierte_numero(numero):
    res = 0
    while numero != 0:
        ultima_cifra = numero % 10
        res = res * 10 + ultima_cifra
        numero //= 10 #numero = numero // 10 
    return res 

def convierte_binario(numero):
    if numero == 0:
        return 0
    
    res = ""
    while numero != 0:
        numero, resto = numero // 2, numero % 2
        res = str(resto) + res
    
    return res 


def sumar_divisores_propios(numero):

    res = 0 
    for i in range(1, numero):
        if numero % i == 0:
            res += i
    return res 

def clasifica_numero(numero):
    if sumar_divisores_propios == numero:
        return "PERFECTO"
    elif sumar_divisores_propios 

def clasifica_rango(limite):
    for i in range(1, limite + 1):
        print(f"{i}: {clasifica_numero(i)}")


def busca_perfecto(posicion):
    n = 1
    contador = 0 
    while True: 
        if clasifica_numero(n) == "PERFECTO": 
            contador += 1
            if contador == posicion: 
                return n
        n += 1

        #TODO: REPASAR TEMA 3 Y HACER EJERCICIO 9 