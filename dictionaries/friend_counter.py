ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

test_dictionary = {
    'happy': 'birthday',
    'buddies': 'matt'
}

def countFriends(dictionary):
    number_of_friends = len(dictionary['friends'])
    dictionary['friends_count'] = number_of_friends
    return dictionary['friends_count']

    


# print(countFriends(test_dictionary))

print(countFriends(ramit))
print(ramit)

# print(test_dictionary)
        
        
    