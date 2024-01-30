tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def mostrar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa no momento.")
    else:
        print("Lista de Tarefas:")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"{index}. {tarefa}")

def remover_tarefa():
    mostrar_tarefas()
    if tarefas:
        indice = int(input("Digite o número da tarefa a ser removida: "))
        if 1 <= indice <= len(tarefas):
            tarefa_removida = tarefas.pop(indice - 1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Índice inválido.")
    else:
        print("Nenhuma tarefa para remover.")

while True:
    print("\n--- Gerenciador de Tarefas ---")
    print("1. Adicionar Tarefa")
    print("2. Mostrar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        mostrar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "4":
        print("Saindo do Gerenciador de Tarefas. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
