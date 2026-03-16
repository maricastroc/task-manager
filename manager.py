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
      raise ValueError('\nNo tasks yet.')
    
    result = ['List of all tasks:']

    for index, task in enumerate(self.tasks):
      status = "[ ✅ ]" if task.completed else "[ ❌ ]"
    
      result.append(f"{index + 1}. {status} {task.name}")

    return "\n".join(result)
    
  def edit_task(self, index: int, new_name: str | None = None, new_status: bool | None = None) -> None:
    if index < 0 or index >= len(self.tasks):
      raise ValueError('Invalid task index.')
    
    task = self.tasks[index]

    if new_name is not None:
      if not new_name.strip():
        raise ValueError('Invalid task name.')
      task.name = new_name

    if new_status is not None:
      task.completed = new_status

  def finish_task(self, index: int) -> None:
    if index < 0 or index >= len(self.tasks):
      raise ValueError('Invalid task index.')
    
    self.tasks[index].completed = True

  def delete_task(self, index: int) -> None:
    if index < 0 or index >= len(self.tasks):
      raise ValueError('Invalid task index.')
    
    self.tasks.pop(index)

  def list_finished_tasks(self) -> str:
    if not self.tasks:
      return "No tasks yet."

    completed_tasks = [task for task in self.tasks if task.completed]

    if not completed_tasks:
      return "No finished tasks."
    
    result = ["Here are all your finished tasks:"]

    for index, task in enumerate(completed_tasks):
      result.append(f"{index + 1}. [ ✅ ] {task.name}")

    return "\n".join(result)

  def delete_finished_tasks(self) -> None:
      self.tasks = [task for task in self.tasks if not task.completed]