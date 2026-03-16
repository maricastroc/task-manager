from models import Task;

class TaskManager:
  def __init__(self):
    self.tasks: list[Task] = []

  def add_task(self, name: str) -> None:
    if not name.strip():
      raise ValueError('Invalid name.')
    self.tasks.append(Task(name))

  def list_tasks(self) -> str:
    if not self.tasks:
      raise ValueError('No tasks yet.')
    
    result = []

    for index, task in enumerate(self.tasks):
      status = "[ ✅ ]" if task.completed else "[ ❌ ]"
      result.append(f"{index + 1}. {status} {task.name}")

      return "\n".join(result)
    
  def edit_task(self, index: int, new_name=None, new_status=None):
    if index < 0 or index >= len(self.tasks):
      raise ValueError('Invalid task index.')
    
    task = self.tasks[index]

    if new_name is not None:
      if not new_name.strip():
        raise ValueError('Invalid task name.')
      task.name = new_name

    if new_status is not None:
      task.completed = new_status