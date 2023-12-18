# Inicializando variáveis
soma = 0
quantidade_numeros = 0

# Loop para ler números do teclado
while True:
    # Lê um número do teclado
    numero = int(input("Digite um número (digite 0 para encerrar): "))
    
    # Verifica se o número é zero para encerrar o loop
    if numero == 0:
        break
    
    # Adiciona o número à soma e incrementa a quantidade de números
    soma += numero
    quantidade_numeros += 1

# Calcula a média aritmética (evitando a divisão por zero)
media = soma / quantidade_numeros if quantidade_numeros != 0 else 0

# Exibe os resultados
print("\nQuantidade de números digitados:", quantidade_numeros)
print("Soma dos números:", soma)
print("Média aritmética dos números:", media)