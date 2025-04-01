# use def function to do task specifically
def check_all_lowercase(words):
    for character in words:  # use for loop
        if character < 'a' or character > 'z':  # use if statement to check under the condition that will check the lower
            return False
    return True

# get the user input
user_input = input("Enter a string: ")

# print the modified inputs
is_lowercase = check_all_lowercase(user_input)
print(f'Is the string all lowercase? {is_lowercase}')