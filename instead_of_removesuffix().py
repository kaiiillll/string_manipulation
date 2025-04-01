# use def function
def remove_suffix(words, suffix):
    if words.endswith(suffix): # use if statement for checking condition
        return wordwords[:len(words) - len(suffix)] # use return 
    return words

# Get user input
user_input = input("Enter a string: ")
suffix_to_remove = input("Enter the suffix to remove: ")
trimmed_string = remove_suffix(user_input, suffix_to_remove)

print(f'Original: "{user_input}"')
print(f'Trimmed: "{trimmed_string}"')

