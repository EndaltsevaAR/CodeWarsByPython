"""Description:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(array):
    zeros = [0] * array.count(0)
    for numb in array:
        if numb == 0:
            array.remove(numb)
    return array + zeros


print(move_zeros([1, 2]))
