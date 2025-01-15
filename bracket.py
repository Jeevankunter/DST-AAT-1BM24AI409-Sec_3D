import math
import os
import random
import re
import sys


def isBalanced(s):
    stack = []
    matching_bracket = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in matching_bracket.values():  
            stack.append(char)
        elif char in matching_bracket.keys():
            if stack and stack[-1] == matching_bracket[char]:
                stack.pop()
            else:
                return "NO"

    return "YES" if not stack else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
