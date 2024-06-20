# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание
# задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

import datetime

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = datetime.datetime.strptime(deadline, "%d.%m.%Y")
        self.status = False

    def time_remaining(self):
        time_remaining = self.deadline - datetime.datetime.now()
        return time_remaining

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)
    def mark_task_done(self, task_index):
        self.tasks[task_index].status = True
    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        for idx, task in enumerate(current_tasks):
            time_remaining_str = str(task.time_remaining()).split(".")[0]
            print(f"{idx + 1}. {task.description} (дедлайн: {task.deadline}, осталось времени: {time_remaining_str})")

# Список задач
task_manager = TaskManager()
task_manager.add_task("Сделать домашнее задание по Python", "21.06.2024")
task_manager.add_task("Сходить в магазин", "20.06.2024")
task_manager.add_task("Выпить таблетку", "24.06.2024")
task_manager.add_task("Погулять вечером с собакой", "20.06.2024")
task_manager.add_task("Посмотреть передачу по телевизору", "28.06.2024")
task_manager.add_task("День рождения у племянника", "20.10.2024")
task_manager.add_task("Уезжаю в отпуск", "20.08.2024")

task_manager.mark_task_done(1)  # Отметить вторую задачу выполненной
task_manager.mark_task_done(3)  # Отметить четвертую задачу выполненной

print("Список задач:")
for idx, task in enumerate(task_manager.tasks):
    print(f"{idx + 1}. {task.description} (дедлайн: {task.deadline}, статус: {'Выполнено' if task.status else 'Не выполнено'})")

print("Текущие задачи:")
task_manager.list_current_tasks()  # Вывести список текущих (не выполненных) задач

