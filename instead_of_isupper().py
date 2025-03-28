# use def function 
def check_uppercase(text):
    for letter in text:  #  use for Loop through each character
        if 'a' <= letter <= 'z':  # Check if any lowercase letter exists
            return False  #  use If statement found, return False (not all uppercase)
    return True 