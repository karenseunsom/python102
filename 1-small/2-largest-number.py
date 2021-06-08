numbers = [1, 50, 3, 99999, -100000, -2, 42]

highest = float('-inf')
for num in numbers:
    if num > highest:
        highest = num

print(highest)        

# could highest = 0
# float('-inf') will make it negative number friendly.