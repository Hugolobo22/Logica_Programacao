# Primeiro atribuo os valores das variáveis
distancia = float(input("Informe a distância total percorrida (em KM):"))
litro = float(input("Informe o total de combustível gasto (em litros):"))

# Depois calculo o valor do consumo médio
consumo = distancia / litro 

# No final, exibo o resultado do cálculo através de um "print"
print("O consumo médio do automóvel é:", consumo, "km/l")