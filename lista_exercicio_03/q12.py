# Contagem Regressiva Recursiva:
def contagem_regressiva_recursiva(n):
    if n <= 0:
        print("Contagem regressiva concluída!")
    else:
        print(n)
        contagem_regressiva_recursiva(n - 1)

# Solicita ao usuário um número inteiro
numero_usuario = int(input("Digite um número inteiro para a contagem regressiva: "))
contagem_regressiva_recursiva(numero_usuario)

# Contagem Regressiva Iterativa:
def contagem_regressiva_iterativa(n):
    while n > 0:
        print(n)
        n -= 1
    print("Contagem regressiva concluída!")

# Solicita ao usuário um número inteiro
numero_usuario = int(input("Digite um número inteiro para a contagem regressiva: "))
contagem_regressiva_iterativa(numero_usuario)