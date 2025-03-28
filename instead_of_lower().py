# use def function
def to_lowercase(text):
    result = ""
    for words in text:  # Loop through each character in text
        if 'A' <= words <= 'Z':  # if-else statement for checking the true and false
            result += chr(ord(words) + 32)  
        else:
            result += words  # Keep other characters the same
    return result