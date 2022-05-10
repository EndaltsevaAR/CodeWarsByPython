"""
Description
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

Deadfish.parse("iiisdoso") =- new int[] {8, 64};
"""


def parse(data):
    result_list = list()
    result_sum = 0
    for letter in data:
        if letter == 'i':
            result_sum += 1
        elif letter == 'd':
            result_sum -= 1
        elif letter == 's':
            result_sum = result_sum**2
        elif letter == 'o':
            result_list.append(result_sum)
    return result_list

