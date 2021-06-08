# want to ask user what they want to add to list.

import json

# todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

with open('todos.json', 'r') as file_handle:
    # contents = file_handle.read()
    # print(contents['name'])
    todos = json.load(file_handle)

def print_todos():
    print('------ Todos ------')
    count = 1
    for todo in todos:
        print(f"{count}: {todo}")
        count += 1
    print('-------------------')

while True: 
        print("""
Choose an option:        )

1. Print Todos
2. Add Todos
3. Remove Todo
0. Quit
        """)
        user_choice = input('')

        if user_choice == '1':
            print_todos()

        elif user_choice == '2':
        # add new item
            new_item = input("What do you want to add? ")
            todos.append(new_item)

        elif user_choice == '3':
            # delete a todo
            index = 0
            for todo in todos:
                print(f"{index}: {todo}")
                index += 1
            delete_index = int(input("Which item would you like to delete? "))
            del todos[delete_index - 1]

        elif user_choice == '0':
            # exit the program loop
            break


with open('todos.json', 'w') as file_handle:
    json.dump(todos, file_handle)
