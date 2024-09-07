i = 1
entrada = 0
pergunta = None
print("O que deseja fazer?")
print("1 - Somar")
print("2 - Subtrair")
print("3 - dividir")
print("4 - multiplicar")

operacao = int(input("Digite sua escolha: "))

if (operacao == 1):
    entrada = float(input("Digite o valor : "))
    while(pergunta != "n"):
        entrada += float(input("Digite o valor : "))
        pergunta = input("Deseja adicionar mais um valor?(S/N) \n").lower()
    print(f"A soma dos valores digitados é = {entrada}")

if (operacao == 2):
    entrada = float(input("Digite o valor : "))
    while(pergunta != "n"):
        entrada -= float(input("Digite o valor : "))
        pergunta = input("Deseja adicionar mais um valor?(S/N) \n").lower()
    print(f"A Subtração dos valores digitados é = {entrada}")

if (operacao == 3):
    entrada = float(input("Digite o valor : "))
    while(pergunta != "n"):
        entrada /= float(input("Digite o valor : "))
        pergunta = input("Deseja adicionar mais um valor?(S/N) \n").lower()
    print(f"A Divisão dos valores digitados é = {entrada}")
    
if (operacao == 4):
    entrada = float(input("Digite o valor : "))
    while(pergunta != "n"):
        entrada *= float(input("Digite o valor: "))
        pergunta = input("Deseja adicionar mais um valor?(S/N) \n").lower()
    print(f"A Multiplicação dos valores digitados é = {entrada}")

    #Que Deus me perdoe!!!