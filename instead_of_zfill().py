def custom_zfill(string, number):
    if len(string) >= number: # CONVERT number to integer
        return string
    return '0' * (number - len(string)) + string

# INPUT input_string
input_string = input("Enter a string or number: ") # PRINT Enter a string or number
number = int(input("Enter the desired number: ")) 

print("Output:", custom_zfill(input_string, number))
