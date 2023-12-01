# Função para encontrar o maior e o menor entre três números
def encontrar_maior_menor(num1, num2, num3):
    maior = max(num1, num2, num3)
    menor = min(num1, num2, num3)
    return maior, menor

# Função para imprimir o resultado
def imprimir_resultado(maior, menor):
    print(f"MAIOR={maior}")
    print(f"MENOR={menor}")

# Entrada de dados
num1 = int(input("Insira o primeiro número:"))
num2 = int(input("Insira o segundo número:"))
num3 = int(input("Insira o terceiro número:"))

# Encontrar o maior e o menor
maior, menor = encontrar_maior_menor(num1, num2, num3)

# Imprimir o resultado
imprimir_resultado(maior, menor)