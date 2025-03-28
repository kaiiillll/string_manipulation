# instead of Istrip()
# use def function to run the same output
# use while function 
def remove_leading_spaces(s):
    num = 0
    while num < len(s) and s[num] == ' ':
        num += 1
    print(f"Number of leading spaces removed: {num}")
    return s[num:]

# Option 1: Predefined test string
test_string = "   Hello, World!   "
print("Testing with predefined string:")
result = remove_leading_spaces(test_string)
print(f"Resulting string: '{result}'\n")

# Option 2: User input
user_string = input("Enter a string with leading spaces: ")
result = remove_leading_spaces(user_string)
print(f"Resulting string: '{result}'")

