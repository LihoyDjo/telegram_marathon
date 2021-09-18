def normalize(string):
    if string.isupper():
        string += '!'
    string = string.capitalize()
    return string
