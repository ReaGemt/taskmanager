# Task Manager
Task Manager - это программа для управления задачами. Она позволяет добавлять новые задачи, отмечать 
их как выполненные и выводить списки текущих и выполненных задач.

## Установка
Для работы с Task Manager вам потребуется Python 3.x. Скачайте проект с репозитория:

Копировать код: 
git clone https://github.com/your_username/task-manager.git
cd task-manager

## Использование
1. Добавление задач
Для добавления новой задачи используйте метод add_task у объекта TaskManager. Пример:
task_manager.add_task("Сделать домашнее задание по Python", "21.06.2024")
task_manager.add_task("Сходить в магазин", "20.06.2024")

2. Отметка задачи как выполненной
Чтобы отметить задачу как выполненную, используйте метод mark_task_done с указанием индекса задачи. Пример:
task_manager.mark_task_done(1)  # Отметить вторую задачу выполненной

3. Вывод списка задач
Вывод всех задач
Чтобы вывести список всех задач (включая выполненные и текущие), используйте метод list_all_tasks:
task_manager.list_all_tasks()

4. Вывод текущих задач
Для вывода только текущих (невыполненных) задач используйте метод list_current_tasks:
task_manager.list_current_tasks()

5. Вывод выполненных задач
Для вывода только выполненных задач используйте метод list_completed_tasks:
task_manager.list_completed_tasks()

Пример использования
```python
from task_manager import TaskManager

# Создаем менеджер задач
task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task("Сделать домашнее задание по Python", "21.06.2024")
task_manager.add_task("Сходить в магазин", "20.06.2024")

# Отмечаем задачи как выполненные
task_manager.mark_task_done(1)

# Выводим список всех задач
print("Список всех задач:")
task_manager.list_all_tasks()

# Выводим список текущих задач
print("\nТекущие задачи:")
task_manager.list_current_tasks()

# Выводим список выполненных задач
print("\nВыполненные задачи:")
task_manager.list_completed_tasks()
```

## Лицензия
Этот проект лицензирован под лицензией MIT - подробности смотрите в файле LICENSE.