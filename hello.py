#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def circshift(s):
    s1 = s[-1] + s
    s2 = s1[:-2]
    return s2


def maximumPower(s):
    # Write your code here
    for x in range(len(s)):
        num = int(s, 2)
        for y in range(15, 1, -1):
            if (num % (2 ** y) == 0):
                return (y)

        s=circshift(s)
    return(0)


if __name__ == '__main__':


    s = input()
    result = maximumPower(s)

    print(result)
