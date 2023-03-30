import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    # file = open('todos.txt', 'w')
    # file.close()
    # with open('todos.txt', 'r') as file:
    #     todos = file.readlines()
    todos = functions.get_todos('todos.txt')


    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'
        todos.append(todo)

        functions.set_todos(todos)

    elif user_action.startswith('show'):
        new_todos = [item.strip('\n') for item in todos]

        for index, todo in enumerate(new_todos):
            # todo = todo.strip('\n') --remove breaklines without using list comprehension
            row = f"{index + 1}-{todo.capitalize()}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            index = int(user_action[5:])
            if index > len(todos):
                exit("there is no todo for that number")
            new_todo = input("Enter new todo:") + '\n'
            todos[index - 1] = new_todo

            functions.set_todos(todos)
        except ValueError:
            print("Command is invalid.")


    elif user_action.startswith('complete'):
        try:
            index = int(user_action[9:]) - 1
            todos.pop(index)

            functions.set_todos(todos)
        except IndexError:
            print("Index is out of range")
        except ValueError:
            print("Command is invalid.")
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid.")

print('Bye')