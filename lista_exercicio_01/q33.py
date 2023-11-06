# Primeiro crio as variáveis para tempo e velocidade da viagem
tempo = int(input("Informe o tempo gasto na viagem:"))
velocidade = int(input("Informe a velocidade média da viagem:"))

# Após isso, calculamos a distância 
distancia = tempo * velocidade

# No final, calculamos quantos litros são necessários para percorrer a viagem (utilizando o valor informado do carro que gasta 12km por L)
litros = distancia / 12
print(("A quantidade de litros necessários são:"),litros)