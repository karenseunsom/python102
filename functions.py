def add(num1, num2):
    return num1 + num2

def add5(num):
    return add(num, 5)

# print(add(15, 5))
# print(add(13, 13))
# print(add(2, 2))

user_num = int(input('What number would you like to add 5 to? '))
print(add5(user_num))


