# use def function
def remove_trailing_spaces(s):
    words = len(s) - 1
    while words >= 0 and s[words] == ' ': # use while loop for loop checks
        words -= 1
    return s[:words+1] # return with plus one of words

# Get user input
user_input = input("Enter a string with trailing spaces: ")
trimmed_string = remove_trailing_spaces(user_input)

print(f'Original: "{user_input}"')
print(f'Trimmed: "{trimmed_string}"')
