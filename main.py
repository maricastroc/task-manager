from manager import TaskManager

def main():
  manager = TaskManager()

  while True:
    print("\nTask List Manager Menu")
    print("\n1. Add Task")
    print("2. See Tasks")
    print("3. Edit Task")
    print("4. Finish Task")
    print("5. Delete Finished Tasks")
    print("6. Leave Menu")

    option = input("\nEnter your choice: ")

    if not option.isdigit():
      print('\nInvalid choice...')
      continue
    
    option = int(option)

    if option < 1 or option > 6:
      print('\nInvalid Choice...')
      continue

    elif option == 1:
      task_name = input("\nPlease, inform your task's name: ").strip()

      if not task_name:
        print('\nInvalid name.')
      else:
        manager.add_task(task_name)
        print('\nTask successfully added!')

    elif option == 2:
      try:
        print(manager.list_tasks())

      except ValueError as e:
        print(e)

    elif option == 3:
      try:
        print('\nList of all tasks:')
        print(manager.list_tasks())

        while True:
          index_input = input("\nEnter the task number: ")

          if not index_input.isdigit():
              print("\nInvalid task index.")
              continue

          index = int(index_input) - 1

          if index < 0 or index >= len(manager.tasks):
              print("\nInvalid task index.")
              continue

          break

        new_name = input("\nNew name (empty to keep): ").strip() or None

        while True:
          status_input = input("\nIs task completed? (y/n or empty): ").strip().lower()

          if status_input in ("y", "n", ""):
            break

          print('\nInvalid option.')

        new_status = None

        if status_input == "y":
            new_status = True
        elif status_input == "n":
            new_status = False

        manager.edit_task(index, new_name, new_status)

        print('\nTask successfully updated!')
      except ValueError as e:
        print(e)

    elif option == 4:
      try:
        print('\nList of all tasks:')
        print(manager.list_tasks())

        while True:
          index_input = input("\nEnter the task number: ")

          if not index_input.isdigit():
              print("\nInvalid task index.")
              continue

          index = int(index_input) - 1

          if index < 0 or index >= len(manager.tasks):
              print("\nInvalid task index.")
              continue

          break

        manager.finish_task(index)

        print('\nTask successfully updated!')
      except ValueError as e:
        print(e)
    elif option == 5:
      print(f"\n {manager.list_finished_tasks()}")

      completed_tasks = [task for task in manager.tasks if task.completed]

      if len(completed_tasks) == 0:
        continue

      while True:
          user_input = input("\nDo you really want to delete all finished tasks? (y/n): ").strip().lower()

          if user_input not in ("y", "n"):
              print("\nInvalid option.")
              continue

          break

      if user_input == "y":
        manager.delete_finished_tasks()
        print("\nTasks successfully deleted!")
      
      continue
    elif option == 6:
      break

  print('See you soon!')

if __name__ == "__main__":
    main()