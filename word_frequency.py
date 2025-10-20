#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")

user_sentence = user_sentence.replace('.', '')
user_sentence = user_sentence.replace('!', '')
user_sentence = user_sentence.replace('?', '')

user_sentence = user_sentence.lower()
word_list = user_sentence.split(' ')

words = []
frequencies = []

for i in word_list:
    if words.count(i) > 0:
        index = words.index(i)
        frequencies[index] = frequencies[index] + 1
    else:
        words.append(i)
        frequencies.append(1)

print("Output:")
for i in range(len(words)):
    print(words[i], ":", frequencies[i])

    
