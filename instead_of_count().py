# use def function
def custom_count(string, char):
    count = 0
    for char in string: # for loop
        if second == char: # use if statement 
            count += 1
    return count

first_input = input("Enter a string: ") # PRINT Enter a strin
second_input = input("Enter a character: ")
print("Count:", custom_count(first_input, second_input))
