# Definição da lista global
lista_de_tarefas = []

# Função para adicionar uma tarefa à lista
def adicionar_tarefa(tarefa):
    lista_de_tarefas.append(tarefa)

# Função para exibir todas as tarefas na lista
def exibir_tarefas():
    print("Lista de Tarefas:")
    for idx, tarefa in enumerate(lista_de_tarefas, start=1):
        print(f"{idx}. {tarefa}")

# Adicionando tarefas à lista
adicionar_tarefa("Estudar Python")
adicionar_tarefa("Fazer compras")
adicionar_tarefa("Preparar apresentação")
adicionar_tarefa("Escreva aqui o nome da tarefa")
# Exibindo as tarefas
exibir_tarefas()