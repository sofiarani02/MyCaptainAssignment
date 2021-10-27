test = input("Enter the string: ")


def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def most_frequent(test):
    letters = [letter.lower() for letter in test if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        a = str(count)
        b = a.zfill(2)
        print(letter, "=",b)

most_frequent(test)
