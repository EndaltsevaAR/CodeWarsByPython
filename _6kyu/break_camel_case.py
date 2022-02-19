# Description:
# Complete the solution so that the function will break up camel casing, using a space between words.

import re

def solution(s):
    return re.sub(r'([A-Z])', r' \1', s)
