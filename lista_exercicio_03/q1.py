def imprimir_numeros_1_a_100():
    print("Números de 1 a 100:")
    for i in range(1, 101):
        print(i, end=" ")
    print("\n")

def imprimir_pares_50_a_100():
    print("Números pares de 50 a 100:")
    for i in range(50, 101, 2):
        print(i, end=" ")
    print("\n")

def contagem_regressiva_fogo():
    print("Contagem regressiva:")
    for i in range(10, -1, -1):
        if i == 0:
            print("Fogo!")
        else:
            print(i, end=", ")
    print("\n")

def numeros_pares_ou_impares():
    limite_superior = int(input("Digite um valor limite: "))
    escolha = input("Deseja ver os pares (P) ou ímpares (I)? ").upper()

    if escolha == "P":
        numeros = [i for i in range(1, limite_superior + 1) if i % 2 == 0]
        print(f"Números pares de 1 a {limite_superior}: {numeros}")
    elif escolha == "I":
        numeros = [i for i in range(1, limite_superior + 1) if i % 2 != 0]
        print(f"Números ímpares de 1 a {limite_superior}: {numeros}")
    else:
        print("Escolha inválida. Por favor, escolha 'P' para pares ou 'I' para ímpares.")

# Chamando as funções
imprimir_numeros_1_a_100()
imprimir_pares_50_a_100()
contagem_regressiva_fogo()
numeros_pares_ou_impares()