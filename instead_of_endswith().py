def check_ends_with(text, ending): # use def function 
    text_length = len(text)
    ending_length = len(ending)

    if text[text_length - ending_length:] == ending:  # if statement to check the condition and return if false

        return True
    return False