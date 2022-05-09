"""/*
Description
A bookseller has lots of books classified in 26 categories labeled A, B, ... Z. Each book has a code c of 3, 4, 5 or
more characters. The 1st character of a code is a capital letter which defines the book category.

In the bookseller's stocklist each code c is followed by a space and by a positive integer n (int n >= 0) which
indicates the quantity of books of this code in stock.

For example an extract of a stocklist could be:

L = {"ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"}.
or
L = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"] or ....
You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :

M = {"A", "B", "C", "W"}
or
M = ["A", "B", "C", "W"] or ...
and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity
according to each category.

For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket a list of pairs):

(A : 20) - (B : 114) - (C : 50) - (W : 0)
where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to
"BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.
 */
 """


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
