# Description:
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    sum_of_sq = ""
    for n in str(num):
        sum_of_sq += str(int(n) * int(n))
    return sum_of_sq

