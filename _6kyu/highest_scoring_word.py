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