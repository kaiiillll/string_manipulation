# use def function
def center_text(text, width):
    if len(text) < width:  # if statement 
        spaces = width - len(text)  # Find how many spaces needed
# Divide spaces on both sides
        right_spaces = spaces - left_spaces  # Make sure total spaces match
        text = (" " * left_spaces) + text + (" " * right_spaces)  # Add spaces
    return text  # return the text under the condition