"""
Description:
Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a
string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally
and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail.
Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C
    A       I       V       D       E       N
The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN
Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the
DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that
include punctuation. Don't filter out punctuation as they are a part of the string.
"""


def encode_rail_fence_cipher(string, n):
    return processing(string, n, True)


def decode_rail_fence_cipher(string, n):
    return processing(string, n, False)


def processing(string, n, encoding):
    string_len = len(string)
    distance = n * 2 - 2
    answer_list = list(string)
    string_list = list(string)
    counter = 0
    for i in range(n):
        if i == n - 1:
            next_step = distance
        else:
            next_step = distance - i*2
        index = i
        while index < string_len:
            if encoding:
                answer_list[counter] = string_list[index]
            else:
                answer_list[index] = string_list[counter]
            counter += 1
            index += next_step
            if next_step == distance:
                next_step = distance
            else:
                next_step = distance - next_step

    return "".join(answer_list)


print(encode_rail_fence_cipher("ABCdefsafbvghb", 3))
