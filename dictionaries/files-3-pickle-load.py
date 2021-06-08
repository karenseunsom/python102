import pickle

with open('todo.pickle', 'rb') as file_handle:
    todos = pickle.load(file_handle)

    for item in todos:
        print(f"{item['title']}")
        if item['completed']:
            print(f"Done: {item['title']}")
        else:
            print(f"Todo: {item['title']}")
