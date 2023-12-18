# Função para adicionar um contato à agenda
def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

# Função para buscar o telefone de um contato na agenda
def buscar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    if nome in agenda:
        print(f"O número de telefone de {nome} é: {agenda[nome]}")
    else:
        print(f"Contato {nome} não encontrado.")

# Função principal que controla o fluxo do programa
def main():
    agenda = {}  # Dicionário para armazenar os contatos

    while True:
        print("\nAgenda de Contatos:")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_contato(agenda)
        elif escolha == '2':
            buscar_contato(agenda)
        elif escolha == '3':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()