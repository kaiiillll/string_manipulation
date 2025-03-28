# use def function
def add_spaces(text, length):
    if len(text) < length:  # use if statement
        text = text + " " * (length - len(text))  
    return text   # return if false under the if condtion
