# use def function
def capitalize_text(text):
    if text == "":
        return text  
    first = text[0]
    if 'a' <= first <= 'z': # if statement to test the condition
        first = chr(ord(first) - 32)  
    rest = ""
    for letter in text[1:]: # use for loop to run until the need is met
        if 'A' <= letter <= 'Z': # if statement to test the condition
            letter = chr(ord(letter) + 32)  
        rest = rest + letter  
    return first + rest  # return if the need is done
