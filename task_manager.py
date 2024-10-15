class TaskManager:
    def __init__(self):
        self.tasks = []
        self.categories = {}

    def create_task(self, task, category):
        self.tasks.append(task)
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(task)
        print("Nova nota criada com sucesso!")
        return True  # Adiciona uma confirmação de sucesso

    def list_tasks(self):
        if not self.tasks:
            return []
        print("Lista de todas as notas:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")
        return self.tasks

    def list_tasks_by_category(self, category):
        return self.categories.get(category, [])

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            old_task = self.tasks[index]
            self.tasks[index] = new_task
            for category, tasks in self.categories.items():
                if old_task in tasks:
                    tasks[tasks.index(old_task)] = new_task
            print("Nota atualizada com sucesso!")
            return True  # Adiciona uma confirmação de sucesso
        else:
            print("Índice de nota inválido.")
            return False  # Adiciona uma confirmação de falha

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            for category, tasks in self.categories.items():
                if task in tasks:
                    tasks.remove(task)
            print("Nota excluída com sucesso!")
            return True  # Adiciona uma confirmação de sucesso
        else:
            print("Índice de nota inválido.")
            return False  # Adiciona uma confirmação de falha
