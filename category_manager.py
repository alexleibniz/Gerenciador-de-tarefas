# category_manager.py

from task_manager import TaskManager

class CategoryManager:
    def __init__(self):
        self.task_manager = TaskManager()

    def create_category(self, category):
        # Verifica se a categoria já existe
        if category in self.task_manager.categories:
            print(f"A categoria '{category}' já existe.")
        else:
            self.task_manager.categories[category] = []
            print(f"Nova categoria '{category}' criada com sucesso!")

    def list_categories(self):
        if self.task_manager.categories:
            print("Lista de categorias:")
            for category in self.task_manager.categories:
                print(f"- {category}")
        else:
            print("Não há categorias cadastradas.")

    def list_tasks_in_category(self, category):
        self.task_manager.list_tasks_by_category(category)

# Exemplo de uso
if __name__ == "__main__":
    category_manager = CategoryManager()

    while True:
        print("\n### Gerenciador de Categorias ###")
        print("1. Criar nova categoria")
        print("2. Listar todas as categorias")
        print("3. Listar notas de uma categoria")
        print("4. Voltar para o gerenciador de tarefas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nova_categoria = input("Digite o nome da nova categoria: ")
            category_manager.create_category(nova_categoria)
        elif opcao == "2":
            category_manager.list_categories()
        elif opcao == "3":
            categoria = input("Digite o nome da categoria para listar as notas: ")
            category_manager.list_tasks_in_category(categoria)
        elif opcao == "4":
            # Voltar para o gerenciador de tarefas
            break
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")
