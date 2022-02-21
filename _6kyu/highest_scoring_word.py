# Description: Given a string of words, you need to find the highest scoring word.
#
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#
# You need to return the highest scoring word as a string.
#
# If two words score the same, return the word that appears earliest in the original string.
#
# All letters will be lowercase and all inputs will be valid.

def high(x):
    list = x.split(" ")
    words = {}
    maxim = 0
    for word in list:
        sumOfLetter = 0
        for letter in word:
            sumOfLetter += ord(letter) - 96
        if maxim < sumOfLetter:
            maxim = sumOfLetter
        words[word] = sumOfLetter
    for item in words.items():
        if item[1] == maxim:
            return item[0]

print(high('man i need a taxi up to ubud'))