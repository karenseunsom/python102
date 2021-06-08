user_input = str(input('Please enter a word: '))

def word_counter(string):
    letter_dictionary = {}
    for letter in string:
        if letter in letter_dictionary:
            letter_dictionary[letter] += 1
        else:
            letter_dictionary = 1
    print(letter_dictionary)

word_counter(user_input)


# Letter histogram
letters = {"a" : 0,"b" : 0,"c" : 0,"d" : 0,"e" : 0,"f" : 0,"g" : 0,"h" : 0,"i" : 0,"j" : 0,"k" : 0,
"l" : 0,"m" : 0,"n" : 0,"o" : 0,"p" : 0,"q" : 0,"r" : 0,"s" : 0,"t" : 0,"u" : 0,"v" : 0,"w" : 0,"x" : 0,"y" : 0, "z" : 0}

def letter_hist(word):
    word = word.lower()
    printvalues = ""
    if len(word) == 0:
        return "GIVE ME A WORD"
    for lets in word: 
        if lets in letters:
            letters[lets] += 1
    for key, value in letters.items():
        if value > 0:
            printvalues += (f"'{key}': {value}, ")
    print(printvalues)


user_input = str((input("Please enter a word: ")))

letter_hist(user_input)