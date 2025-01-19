import math, re


# Accept a block of text input from the user.

block = input("Please write some text: ")

#       print()
print(type(block))
processed_block = block.casefold()

# Can I put a string into a list?
temp_list = [block]
print(block)
print(processed_block)
print(temp_list)
print(re.split(" " or ",", processed_block))
# for each in temp_list:
    # print(each)

# Parse the block and put it in a list to traverse



# print(dir(re))
#  Count how many times each word appears in the text (case-insensitive + ignore punctuation)

# Output the words sorted by frequency in descending order. If two words have the same frequency, sort them alphabetically.

