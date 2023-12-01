# Solicitar a quantidade de kWh consumida e o tipo de instalação
kwh_consumidos = float(input("Digite a quantidade de kWh consumida: "))
tipo_instalacao = input("Digite o tipo de instalação (R para residências, I para indústrias, C para comércios): ")

# Definir os preços conforme a tabela
if tipo_instalacao == "R" or tipo_instalacao == "r":
    if kwh_consumidos <= 500:
        preco = 0.40 * kwh_consumidos
    elif kwh_consumidos <= 1000:
        preco = 0.65 * kwh_consumidos
    elif kwh_consumidos <= 5000:
        preco = 0.55 * kwh_consumidos
    else:
        preco = 0.60 * kwh_consumidos

elif tipo_instalacao == "C" or tipo_instalacao == "c":
    if kwh_consumidos <= 500:
        preco = 0.40 * kwh_consumidos
    elif kwh_consumidos <= 1000:
        preco = 0.65 * kwh_consumidos
    elif kwh_consumidos <= 5000:
        preco = 0.55 * kwh_consumidos
    else:
        preco = 0.60 * kwh_consumidos

elif tipo_instalacao == "I" or tipo_instalacao == "i":
    if kwh_consumidos <= 500:
        preco = 0.55 * kwh_consumidos
    elif kwh_consumidos <= 1000:
        preco = 0.60 * kwh_consumidos
    elif kwh_consumidos <= 5000:
        preco = 0.55 * kwh_consumidos
    else:
        preco = 0.60 * kwh_consumidos

else:
    print("Tipo de instalação inválido.")
    preco = 0  # Definir um preço nulo se o tipo de instalação for inválido

# Exibir o preço a pagar
print(f"Preço a pagar: R$ {preco:.2f}")