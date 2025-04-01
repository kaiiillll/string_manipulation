# for loop each word in the string 
def custom_index(string, char): # use def function
    for word in range(len(string)):
        if string[word] == char:  # if statement the character at index word in string is equal to char
            return word -1

first_input = input("Enter a string: ")
second_input = input("Enter a character: ")

result = custom_index(first_input, second_input)
print(result)
# end the for loop