# Ler os valores de entrada
hora_inicial = float(input("Insira a Hora inicial:"))
minuto_inicial = float(input("Insira o Minuto inicial:"))
hora_final = float(input("Insira a Hora final:"))
minuto_final = float(input("Insira o Minuto final:"))

# Calcular a duração em minutos
inicio_em_minutos = hora_inicial * 60 + minuto_inicial
fim_em_minutos = hora_final * 60 + minuto_final

# Calcular a duração total em minutos
duracao_em_minutos = fim_em_minutos - inicio_em_minutos

# Verificar se a duração ultrapassou um dia (24 horas)
if duracao_em_minutos <= 0:
    duracao_em_minutos += 24 * 60  # Adicionar 24 horas

# Calcular horas e minutos da duração total
duracao_horas = duracao_em_minutos // 60
duracao_minutos = duracao_em_minutos % 60

# Exibir o resultado
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")