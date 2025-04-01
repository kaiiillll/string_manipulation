# use def function to do specfic task
def to_uppercase(words):
    result = ""
    for character in words:
        if 'a' <= character <= 'z': # use if-else statement for checking under condition
            result += chr(ord(character) - 32)
        else:
            result += character
    return result  # return if true

# Get user input
words = input("Enter a string: ")
print("Uppercase:", to_uppercase(words))