import math
import os
import random
import re
import sys


def twoStacks(maxSum, a, b):
    sum_a, sum_b = 0, 0
    count = 0
    i, j = 0, 0

    while i < len(a) and sum_a + a[i] <= maxSum:
        sum_a += a[i]
        i += 1
    count = i

    while j < len(b):
        sum_b += b[j]
        j += 1

        while sum_a + sum_b > maxSum and i > 0:
            i -= 1
            sum_a -= a[i]

        if sum_a + sum_b <= maxSum:
            count = max(count, i + j)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
