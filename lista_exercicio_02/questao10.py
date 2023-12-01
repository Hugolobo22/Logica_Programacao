import random
# A) Pesquise sobre o módulo random do Python e como importá-lo.

# B) Gere um número inteiro aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# C) Inicialize a variável palpite com 0
palpite = 0

# D) Loop enquanto o palpite for errado
while palpite != numero_secreto:
    # D) Leia do usuário o próximo palpite
    palpite = int(input("Digite seu palpite: "))

    # E) Compare palpite com numero_secreto e forneça dicas
    if palpite > numero_secreto:
        print("Tente um número menor.")
    elif palpite < numero_secreto:
        print("Tente um número maior.")

# F) Exiba "Parabéns!! Você acertou o numero_secreto"
print(f"Parabéns!! Você acertou o número secreto: {numero_secreto}")