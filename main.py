from utils.calculadora import *

total = None

print("1 - Somar\n2 - subtrair\n3 - multiplicar\n4 - dividir\n5 - potencia\n6 - raiz_quadrada")
operacao = int(input("Qual o peração deseja usar: "))

x = float(input("Digite o primeiro valor: "))
if operacao != 6:
    y = float(input("Digite o segundo valor: "))

if operacao == 1:
    total = somar(x, y)
elif operacao == 2:
    total = subtrair(x, y)
elif operacao == 3:
    total = multiplicar(x, y)
elif operacao == 4:
    total = dividir(x, y)
elif operacao == 5:
    total = potencia(x, y)
elif operacao == 6:
    total = raiz_quadrada(x)

print(total)