numbers = [1, 50, 3, 999999, 100000, 2, 42]

smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print(smallest) 