# Description: Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]

def unique_in_order(iterable):
    result_list = []
    if len(iterable) > 0:
       result_list.append(iterable[0])
    for letter in iterable:
        if result_list[-1] != letter:
            result_list.append(letter)
    return result_list

print(unique_in_order('AAAABBBCCDAABBB'))