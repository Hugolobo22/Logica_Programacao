# Primeiro criamos as variáveis com as informações desejadas
idade = int(input("Informe a idade desejada:"))
anos = idade / 365
meses = (idade % 365) / 30
dias = (idade % 365) % 30

# Após os cálculos, exibimos o resultado na tela
print(("Sua idade em anos:"),anos)
print(("Sua idade em meses"),meses)
print(("Sua idade em dias"),dias)