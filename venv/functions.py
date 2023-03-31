def get_todos(filepath="todos.txt"):
    """read a file and save its content to a local var"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def set_todos(todos, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos)

