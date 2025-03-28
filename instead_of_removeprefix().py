def remove_prefix(text, prefix): # use def dunction 
    length = len(prefix)  
    if text[:length] == prefix:  # # use if statement to Check if text starts with prefix
        return text[length:]  # use the return to remove the prefix
    return text