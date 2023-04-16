import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    useraction = input("Type add, show, edit, delete or exit: ")
    useraction = useraction.strip()

    if useraction.startswith("add"):
        todo = useraction[4:]

        # In this method don't need colse method
        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()

        todos = functions.get_todos()

        #    similar

        # file = open('todos.txt','r')
        # todos = file.readlines()
        # file.close()

        todos.append(todo + '\n')  # with using function
        functions.write_todos(todos)  # with using function

        # ******  OR ******

        # with open('todos.txt', 'w') as file:
        #     file.writelines(todos)

        # ***** OR  *****

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

    elif useraction.startswith("show"):

        # In this method don't need colse method
        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()

        todos = functions.get_todos()

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        for index, item in enumerate(todos):
            item = item.capitalize().strip('\n')
            print(f"{index + 1}-{item}")

    elif useraction.startswith("edit"):
        try:
            number = int(useraction[5:])
            print(number)
            number = number - 1

            # with open('todos.txt', 'r') as file:
            #     todos = file.readlines()

            todos = functions.get_todos()  # with using function

            new_todo = input("enter the todo : ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)  # with using function
            # *******   OR    *********
            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
        except ValueError:
            print("Your comment is invalid")
            continue

    elif useraction.startswith("delete"):
        try:
            number = int(useraction[7:])

            # with open('todos.txt', 'r') as file:
            #     todos = file.readlines()

            todos = functions.get_todos()  # with using function

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)  # with using function

            # ******  OR   *****

            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif 'exit' in useraction:
        break

    else:
        print("You entered invalid item")
print("Good Bye!")
