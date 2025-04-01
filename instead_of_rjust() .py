# use def dunction
def right_justify(words, length):
    return ' ' * (length - len(words)) + words # return under the condition

# get the user input 
user_input = input("Enter a string: ")
length = int(input("Enter the total length: "))

# print the results
print(right_justify(user_input, length))