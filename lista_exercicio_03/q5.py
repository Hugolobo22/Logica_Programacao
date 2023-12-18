def exibir_menu():
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def adicao():
    numero = int(input("Digite um número para exibir a tabuada de adição: "))
    for i in range(1, 11):
        resultado = numero + i
        print(f"{numero} + {i} = {resultado}")

def subtracao():
    numero = int(input("Digite um número para exibir a tabuada de subtração: "))
    for i in range(1, 11):
        resultado = numero - i
        print(f"{numero} - {i} = {resultado}")

def multiplicacao():
    numero = int(input("Digite um número para exibir a tabuada de multiplicação: "))
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

def divisao():
    numero = int(input("Digite um número para exibir a tabuada de divisão: "))
    for i in range(1, 11):
        resultado = numero / i
        print(f"{numero} / {i} = {resultado}")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        adicao()
    elif opcao == "2":
        subtracao()
    elif opcao == "3":
        multiplicacao()
    elif opcao == "4":
        divisao()
    elif opcao == "5":
        print("Programa encerrado. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")