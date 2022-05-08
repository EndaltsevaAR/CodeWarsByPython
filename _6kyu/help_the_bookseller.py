def stock_list(listOfArt, listOfCat):
    if len(listOfArt) == 0 or len(listOfCat) == 0:
        return ''
    letter_dict = dict()
    for word in listOfArt:
        if word[0:1] in letter_dict:
            letter_dict[word[0:1]] += int(word.split(" ")[1])
        else:
            letter_dict[word[0:1]] = int(word.split(" ")[1])
    result_str = ""
    for letter in listOfCat:
        number = 0
        if letter in letter_dict:
            number = letter_dict[letter]
        result_str += f"( {letter}: {number}) - "
    return result_str[0:len(result_str)-3]


l_art = ["ABAR 200", "CDXE 500", "DKWR 250", "BTSQ 890", "DRTY 600"]
l_cat = ["A", "B", "D"]
print(stock_list(l_art, l_cat))
