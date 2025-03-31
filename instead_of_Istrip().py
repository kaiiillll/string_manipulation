# instead of Istrip()
def remove_leading_spaces(s): # use def function to run the same output
    num = 0
    while num < len(s) and s[num] == ' ': # use while function 
        num += 1
    return s[num:]
