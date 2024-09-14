def somar (x, y):
    return x+y

def subtrair (x, y):
    return x-y

def multiplicar (x, y):
    return x*y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "ERRO y = 0"

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    if x >= 0:
        return x ** 0.5
    else:
        return "Erro: número negativo"
