"""Description:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(array):
    zeros = [0] * array.count(0)
    not_nulls = list()
    for numb in array:
        if numb != 0:
            not_nulls.append(numb)
    return not_nulls + zeros


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
