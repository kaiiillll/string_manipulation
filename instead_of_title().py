# use def function
def title_text(text):
    result = ""  
    new_word = True  

    for letter in text: # use for loop for looping the program until the need is met
        if letter == " ": # use if and elif statement
            new_word = True  
        elif new_word:
            if 'a' <= letter <= 'z':  
                letter = chr(ord(letter) - 32)  
            new_word = False  
        elif 'A' <= letter <= 'Z':  
            letter = chr(ord(letter) + 32)  

        result = result + letter  

    return result  # return until the need is met