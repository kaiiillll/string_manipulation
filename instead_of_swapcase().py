# use def function
def swap_case(text):
    result = ""
    for letter in text:
        # use if-elif-else statement to run the condition
        if 'A' <= letter <= 'Z':  
            result += chr(ord(letter) + 32)  # Convert uppercase to lowercase
        elif 'a' <= letter <= 'z':  
            result += chr(ord(letter) - 32)  # Convert lowercase to uppercase
        else:
            result += letter  
    return result # return the result after undergoes boolean operator

