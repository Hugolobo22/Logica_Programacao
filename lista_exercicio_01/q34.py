# Primeiros criamos variáveis para cada informação
dias = int(input("Informe a quantidade de dias:"))
horas = int(input("Informe a quantidade de horas:"))
minutos = int(input("Informe a quantidade de minutos:"))
segundos = int(input("Informe a quantidade de segundos:"))

# Depois transformamos todos em segundos por meio de cálculos (Fórmulas) e somamos tudo
total = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + (segundos)

# No final, exibimos o resultado utilizando "print"
print("O total de segundos é:", total)