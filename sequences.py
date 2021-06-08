# Strings
"example"

# Integers
7

# floats
7.7

# Booleans
True
False

# List

languages = ['python', 'javascript', 'html', 'css', 'php', 'C#']
empty_list = []

# access items in list by index
# print(languages[0])

# accessing items outside of possible values will throw an IndexError
# print(languages[10])

# access items from end of list with negative index
# print(languages[-1])

# print(languages[2: ])

# index = 0
# while index < len(languages):
#     print(f"No, {languages[index]} is the best languate")
#     index +=1 

for lang in languages:
    print("NO, " + lang + " is the best language")