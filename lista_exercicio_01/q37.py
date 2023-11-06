# primeiro informamos o tempo em segundos
valor = int(input("Informe a duração em segundos:"))

# Depois calculamos o valor para saber quantas horas e minutos tem naquele tempo
horas = int (valor / 3600)
minutos = int (valor % 3600 / 60)
segundos = int (valor % 3600 % 60)

# No final, exibimos o resultado final
print(horas,":",minutos,":",segundos)