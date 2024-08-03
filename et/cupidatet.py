import string

# Define the punctuation characters
PUNCT_TO_REMOVE = string.punctuation

# Example string with punctuation
example_string = "Hello, world! How are you?"

# Method 1: Using translate() with str.maketrans()
translation_table = str.maketrans('', '', PUNCT_TO_REMOVE)
cleaned_string = example_string.translate(translation_table)

print(cleaned_string)
