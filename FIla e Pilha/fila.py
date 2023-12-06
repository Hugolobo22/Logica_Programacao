fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
menu = '''Digite um dos itens abaixo:
A: Remove o primeiro item da fila.
F: Adiciona um item ao fim da fila.
S: Termina o código.
'''
print(menu)
adicionar = 11
while True:
    print("A sua fila é:", fila)
    opcao = input("Escolha uma opção (A, F, S): ").upper()

    if opcao == 'A':
        fila.pop(0)
    elif opcao == 'F':
        fila.append(adicionar)
        adicionar = adicionar + 1
    elif opcao == 'S':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")