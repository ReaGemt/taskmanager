# Импортируем библиотеку datetime для работы с временем
import datetime

# Создаем класс Task, который позволяет управлять задачами (делами)
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = datetime.datetime.strptime(deadline, "%d.%m.%Y")
        self.status = False

    # Время до дедлайн
    def time_remaining(self):
        time_remaining = self.deadline - datetime.datetime.now()
        return time_remaining

    # Строковое представление задачи включая описание, дедлайн, статус и оставшееся время до дедлайна.
    def __str__(self):
        status = 'Выполнено' if self.status else 'Не выполнено'
        time_remaining_str = str(self.time_remaining()).split(".")[0]
        return f"{self.description} (дедлайн: {self.deadline.strftime('%d.%m.%Y')}, статус: {status}, осталось времени: {time_remaining_str})"

# Класс для управления задачами
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []  # Добавленный атрибут для хранения выполненных задач

    # Создает новую задачу и добавляет ее в список задач
    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    # Удаляет задачу из списка задач
    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
    # Отмечает задачу выполненной
    def mark_task_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks.pop(task_index)
            task.status = True
            self.completed_tasks.append(task)  # Добавляем задачу в список выполненных задач

    # Выводит список текущих (не выполненных) задач
    def list_current_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. {task}")

    # Выводит список выполненных задач
    def list_completed_tasks(self):
        for idx, task in enumerate(self.completed_tasks):
            print(f"{idx + 1}. {task}")

    # Выводит список всех задач (выполненных и невыполненных).
    def list_all_tasks(self):
        print("Текущие задачи:")
        self.list_current_tasks()
        print("\nВыполненные задачи:")
        self.list_completed_tasks()


# Создаем менеджер задач и добавляем задачи
task_manager = TaskManager()
task_manager.add_task("Сделать домашнее задание по Python", "21.06.2024")
task_manager.add_task("Сходить в магазин", "20.06.2024")
task_manager.add_task("Выпить таблетку", "24.06.2024")
task_manager.add_task("Погулять вечером с собакой", "20.06.2024")
task_manager.add_task("Посмотреть передачу по телевизору", "28.06.2024")
task_manager.add_task("День рождения у племянника", "20.10.2024")
task_manager.add_task("Уезжаю в отпуск", "20.08.2024")

# Отмечаем некоторые задачи выполненными
task_manager.mark_task_done(0)  # Отметить вторую задачу выполненной
task_manager.mark_task_done(1)  # Отметить четвертую задачу выполненной

# Выводим список всех задач
print("Список всех задач:")
task_manager.list_all_tasks()

# Выводим список текущих (не выполненных) задач
print("\nТекущие задачи:")
task_manager.list_current_tasks()

# Выводим список выполненных задач
print("\nВыполненные задачи:")
task_manager.list_completed_tasks()
