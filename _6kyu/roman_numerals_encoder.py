def solution(n):
    result = ""
    translate_list = list()
    translate_list.append(tuple(1000, 'M'))
    translate_list.append(tuple(900, 'CM'))
    translate_list.append(tuple(500, 'D'))
    translate_list.append(400, 'CD')
    translate_list.append(100, 'C')
    translate_list.append(90, 'XC')
    translate_list.append(50, 'L')
    translate_list.append(40, 'XL')
    translate_list.append(10, 'X')
    translate_list.append(9, 'IX')
    translate_list.append(5, 'V')
    translate_list.append(4, 'IV')
    translate_list.append(1, 'I')

    return