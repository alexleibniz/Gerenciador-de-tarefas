# test_task_manager.py
import pytest
from task_manager import TaskManager

@pytest.fixture
def task_manager():
    return TaskManager()

def test_create_task(task_manager):
    task = "Finalizar relatório"
    category = "Trabalho"

    task_manager.create_task(task, category)
    tasks = task_manager.list_tasks()

    assert len(tasks) == 1
    assert tasks[0] == task
    assert task_manager.list_tasks_by_category(category) == [task]

def test_create_multiple_tasks(task_manager):
    task1 = "Finalizar relatório"
    task2 = "Reunião com o time"
    category = "Trabalho"

    task_manager.create_task(task1, category)
    task_manager.create_task(task2, category)
    tasks = task_manager.list_tasks()

    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks
    assert task_manager.list_tasks_by_category(category) == [task1, task2]

def test_update_task(task_manager):
    task = "Finalizar relatório"
    updated_task = "Finalizar relatório e enviar"
    category = "Trabalho"

    task_manager.create_task(task, category)
    task_manager.update_task(0, updated_task)
    tasks = task_manager.list_tasks()

    assert len(tasks) == 1
    assert tasks[0] == updated_task

def test_delete_task(task_manager):
    task = "Finalizar relatório"
    category = "Trabalho"

    task_manager.create_task(task, category)
    task_manager.delete_task(0)
    tasks = task_manager.list_tasks()

    assert len(tasks) == 0
