#https://www.hackerrank.com/challenges/write-a-function/problem

import calendar
def is_leap(year):
    leap = calendar.isleap(year)
    #(OR)
    #leap = True if(year%4==0 and (year%400==0 or year%100!=0)) else False
    #(OR)
    #if(year%4==0 and (year%400==0 or year%100!=0)):
    #    leap = True
    
    return leap

year = int(raw_input())
print is_leap(year)
