import sys
tarefas = []

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "status": "pendente"
    }
    tarefas.append(tarefa)
    print(f"Tarefa, '{nome}' Adicionado com sucesso!")

def listar_tarefas():
       print("Tarefas:")
       for tarefa in tarefas:
            print(f"Nome: {tarefa["nome"]}")
            print(f"Descricao: {tarefa["descricao"]}")
            print(f"Prioridade: {tarefa["prioridade"]}")
            print(f"Categoria: {tarefa["categoria"]}")
            print(f"Status: {tarefa["status"]}")

print("---------------------------------------")

def marcar_concluida(nome):
     for tarefa in tarefas:
          if tarefa["nome"] == nome:
               tarefa["status"] = "concluida"
               print(f"Tarefa '{nome}' marcada como concluída!")
               return
          print(f"Tarefa '{nome}' não encontrada.")

def filtrar_por_prioridade(prioridade):
     print(f"Tarefas com prioridade'{prioridade}':")
     for tarefa in tarefas:
          encontrou = False
          if tarefa["prioridade"] == prioridade:
            print(f"Nome: {tarefa["nome"]}")
            print(f"Descricao: {tarefa["descricao"]}")
            print(f"Prioridade: {tarefa["prioridade"]}")
            print(f"Categoria: {tarefa["categoria"]}")
            print(f"Status: {tarefa["status"]}")
            encontrou = True
     if not encontrou:
          print(f"Nenhuma tarefa encontrada com prioridade '{prioridade}'")       

print("---------------------------------------")

def filtrar_por_categoria(categoria):
     print(f"Tarefas com categoria '{categoria}':")
     encontrou = False
     for tarefa in tarefas:
          if tarefa["categoria"] == categoria:
            print(f"Nome: {tarefa["nome"]}")
            print(f"Descricao: {tarefa["descricao"]}")
            print(f"Prioridade: {tarefa["prioridade"]}")
            print(f"Categoria: {tarefa["categoria"]}")
            print(f"Status: {tarefa["status"]}")
          encontrou = True
     if not encontrou:
        print(f"Nenhuma tarefa encontrada com categoria '{categoria}'")

print("---------------------------------------")

def editar_tarefa(nome):
     encontrou = False
     for tarefa in tarefas:
          if tarefa["nome"] == nome:
               print("Editar tarefa:")
               novo_nome = input("Nome: ")
               tarefa["nome"] = novo_nome
               tarefa["descricao"] = input("Descrição: ")
               tarefa["categoria"] = input("Categoria: ")
               print(f"Tarefa '{nome}' editada com sucesso!")
               encontrou = True
               return
          if not encontrou:
               print(f"Tarefa '{nome}' não encontrada.")

def excluir_tarefa(nome):
     encontrou = False
     for tarefa in tarefas:
          if tarefa["nome"] == nome:
               tarefas.remove(tarefa)
               print(f"Tarefa '{nome}' excluída com sucesso!")
               encontrou = True
               return
          if not encontrou:
               print(f"Tarefa '{nome}' não encontrada.")

def resultado_final():
    print("Resultado final:")
    print(f"Total de tarefas: {len(tarefas)}")
    print(f"Tarefas concluídas: {len([t for t in tarefas if t['status'] == 'concluida'])}")
    print(f"Tarefas pendentes: {len([t for t in tarefas if t['status'] == 'pendente'])}")               


def main():
     while True:
          print("Menu:")
          print("1. Adicionar tarefa")
          print("2. Listar tarefas") 
          print("3. Marcar tarefa como concluída") 
          print("4. Filtrar tarefas por prioridade") 
          print("5. Filtrar tarefas por categoria") 
          print("6. Editar tarefa") 
          print("7. Excluir tarefa") 
          print("8. Resultado final") 
          print("9. Sair.")  
          opcao = input("Escolha uma opção: ")
          if opcao == "1":
               nome = input("Nome da tarefa: ")
               descricao = input("Nome da descrição: ")
               prioridade = input("Nome da prioridade: ")
               categoria = input("Nome da categoria: ")
               adicionar_tarefa(nome, descricao, prioridade, categoria)
          
          elif opcao == "2":
               listar_tarefas()
          elif opcao == "3":
               nome = input("Nome da tarefa a marcar como concluída: ")
               marcar_concluida(nome)
          elif opcao == "4":
               prioridade = input("Prioridade para filtrar: ")
               filtrar_por_prioridade(prioridade)
          elif opcao == "5":
               categoria = input("Categoria a filtrar: ")
               filtrar_por_categoria(categoria)
          elif opcao == "6":
               nome = input("Nome da tarefa a editar: ")
               editar_tarefa(nome)
          elif opcao == "7":
               nome = input("Nome da tarefa a excluir: ")
               excluir_tarefa(nome)
          elif opcao == "8":
               nome = input("Resultado final.")
               resultado_final(nome)     
          elif opcao == "9":
               print("Saindo...")
               sys.exit()
          else:
               print("\033[33mOpção inválida.\033[0m \033[31mTente novamente!\033[0m")

main()