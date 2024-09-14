from utils.calculadora import *

total = None

print("1 - Somar\n2 - subtrair\n3 - multiplicar\n4 - dividir\n")
operacao = int(input("Qual o peração deseja usar: "))

x = float(input("Digite o primeiro valor: "))
y = float(input("Digite o segundo valor: "))

if operacao == 1:
    total = somar(x, y)
elif operacao == 2:
    total = subtrair(x, y)
elif operacao == 3:
    total = multiplicar(x, y)
elif operacao == 4:
    total = dividir(x, y)

print(total)