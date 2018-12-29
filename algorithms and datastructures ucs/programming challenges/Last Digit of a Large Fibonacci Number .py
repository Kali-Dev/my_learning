# Uses python3
"""
Created on Sat Dec 29 11:40:59 2018

@author: kalip
"""
n = int(input())
fib_last_number_list = [0,1]
if n>1:
    for x in range(2,n+1):
        fib_last_number_list.append((fib_last_number_list[x-1]+fib_last_number_list[x-2])%10)
print(fib_last_number_list[n])
