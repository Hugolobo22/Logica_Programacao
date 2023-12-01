# Solicitar a distância que o passageiro deseja percorrer em km
distancia = float(input("Digite a distância da viagem em km: "))

# Definir os preços conforme as condições
if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia

# Exibir o preço da passagem
print(f"O preço da passagem é: R$ {preco:.2f}")