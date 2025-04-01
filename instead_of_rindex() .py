# def function
def custom_rindex(string, char):
    for position in range(len(string)-1, -1, -1):
        if string[position] == char:  # if statemnt character at position in string equals char
            return position # return position
    return -1

first_input = input("Enter a string: ")
second_input = input("Enter a character: ")

print(custom_rindex(first_input, second_input))
# end of function
