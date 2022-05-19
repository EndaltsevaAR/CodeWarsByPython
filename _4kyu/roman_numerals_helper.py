"""Create a RomanNumerals class that can convert a roman numeral to and from an integer value. It should follow the API
demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000"""


class RomanNumerals:

    def to_roman(val):
        result = ""
        translate_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                          (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
                          (4, 'IV'), (1, 'I')]
        for pair in translate_list:
            while val / pair[0] >= 1:
                result += pair[1]
                val -= pair[0]
        return result

    def from_roman(roman_num):
        result = 0
        translate_list = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                          (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'),
                          (4, 'IV'), (1, 'I')]
        for pair in translate_list:
            while roman_num.startswith(pair[1]):
                result += pair[0]
                if len(roman_num) > len(pair[1]):
                    roman_num = roman_num[len(pair[1])::]
                else:
                    roman_num = ""
                    break
        return result


print(RomanNumerals.from_roman("IV"))