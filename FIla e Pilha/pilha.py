pilha = [1, 2, 3 , 4, 5]
menu = '''Digite um dos itens abaixo:
E: Para empilhar um novo prato.
D: Para desempilhar, removendo um prato da pilha.
S: Sai do sistema.
'''
print(menu)
tamanho = len(pilha) - 1
adicionar = 6
while True:
    print("A sua Pilha é:", pilha)
    opcao = input("Escolha uma opção (E, D, S): ").upper()

    if opcao == 'D':
        pilha.pop(tamanho)
    elif opcao == 'E':
        pilha.append(adicionar)
        adicionar = adicionar + 1
    elif opcao == 'S':
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")