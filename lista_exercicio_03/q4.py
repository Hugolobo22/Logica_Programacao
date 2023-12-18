# Função para calcular as notas e exibir a relação
def calcular_notas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = [0, 0, 0, 0, 0, 0, 0]

    print(valor)

    for i in range(len(notas)):
        quantidade_notas[i] = valor // notas[i]
        valor = valor % notas[i]
        print(f"{quantidade_notas[i]} nota(s) de R$ {notas[i]},00")

# Leitura do valor inteiro
valor = int(input('Insira um número:'))

# Chamada da função para calcular e exibir as notas
calcular_notas(valor)