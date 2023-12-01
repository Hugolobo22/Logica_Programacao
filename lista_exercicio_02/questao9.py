import random
# A)  Pesquise sobre o módulo random do Python e como importá-lo

# B) Gere um número inteiro aleatório entre 0 e 2
opcao_computador = random.randint(0, 2)

# C) Atribua o texto correspondente à opção do computador
if opcao_computador == 0:
    opcao_computador_texto = 'pedra'
elif opcao_computador == 1:
    opcao_computador_texto = 'papel'
else:
    opcao_computador_texto = 'tesoura'

# D) Leia a opção do jogador
opcao_jogador = input("Escolha pedra, papel ou tesoura: ")

# E) Compare as opções do computador e do jogador
if (opcao_jogador == 'pedra' and opcao_computador_texto == 'tesoura') or \
   (opcao_jogador == 'papel' and opcao_computador_texto == 'pedra') or \
   (opcao_jogador == 'tesoura' and opcao_computador_texto == 'papel'):
    print('Jogador venceu!')
    
# F) Caso contrário, o computador vence
else:
    print('Computador venceu!')

# G) Verifique se é um empate
if opcao_jogador == opcao_computador_texto:
    print('Empate!')