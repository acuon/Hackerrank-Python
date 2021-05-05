#https://www.hackerrank.com/challenges/py-if-else/problem

#!/bin/python
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
print("Not Weird" if((n%2==0) and(n<5 or n>20)) else "Weird")
#if((n%2==0) and(n<5 or n>20)):
#    print "Not Weird"
#else:
#    print "Weird"
