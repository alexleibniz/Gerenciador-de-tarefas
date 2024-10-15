# Gerenciador de Tarefas (Task Manager)

Este é um projeto simples em Python para gerenciar tarefas e categorizá-las.

## Requisitos

- Python 3.12.4 ou superior
- Nenhuma biblioteca externa é necessária além das bibliotecas padrão do Python.

## Arquitetura do Projeto

O projeto é dividido em dois principais scripts:

1. **`task_manager.py`**: Responsável pelo gerenciamento de tarefas, incluindo criação, listagem, atualização e exclusão de tarefas, bem como agrupamento por categorias.

2. **`category_manager.py`**: Gerencia as categorias associadas às tarefas, permitindo a criação de novas categorias, listagem de categorias existentes e listagem de tarefas dentro de categorias específicas.

## Diagrama de Classes Simplificado

```
+-----------------------------------------+
| TaskManager |
+-----------------------------------------+
| - tasks: List[str] |
| - categories: Dict[str, List[str]] |
+-----------------------------------------+
| + create_task(task: str, category: str) |
| + list_tasks() |
| + list_tasks_by_category(category: str) |
| + update_task(index: int, new_task: str)|
| + delete_task(index: int) |
+-----------------------------------------+

+-----------------------------------------+
| CategoryManager |
+-----------------------------------------+
| - task_manager: TaskManager |
+-----------------------------------------+
| + create_category(category: str) |
| + list_categories() |
| + list_tasks_in_category(category: str) |
+-----------------------------------------+
```

## Como Executar

1. Clone o repositório ou baixe os arquivos para seu ambiente local.
2. Abra um terminal e navegue até o diretório onde os arquivos estão localizados.
3. Para executar o gerenciador de tarefas, use o comando:
```
python3 task_manager.py
```
4. Siga as instruções exibidas no terminal para criar, listar, atualizar e excluir tarefas, bem como gerenciar categorias.

---

Este projeto foi desenvolvido como exemplo simples de gerenciamento de tarefas em Python. Sinta-se à vontade para modificar e expandir conforme suas necessidades.
