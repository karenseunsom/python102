
# list of positive and negative numbersnumbers = [78, -1, -1000, 9001, 201]
numbers = [78, -1, -1000, 9001, 201]

# create a new empty list so we can add things to it
positive_numbers = []
# loop over each number
for num in numbers:
    # if number is positive
    if num > 0:
        # add to new list
        positive_numbers.append(num)
        
#  output new list
print(positive_numbers)


list_with_strings = ['things', 'stuff', 'others']
list_with_numbers = [0, 1, 2]
list_with_booleans = [True, False, True]
list_with_lots = ['things', 2, True, []]
