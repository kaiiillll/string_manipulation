# use def function
def check_starts_with(words, prefix):
    for words in range(len(prefix)): # use for loop
        if words[words] != prefix[words]: # under if statement check the condition and return if true
            return False
    return True
# Get user input
user_input = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

print(check_starts_with(user_input, prefix))

