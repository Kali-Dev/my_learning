# Uses python3
"""
@author: kalip
"""
n = int(input())
fib_number_list = [0,1]
if n>1:
    for x in range(2,n+1):
        fib_number_list.append(fib_number_list[x-1]+fib_number_list[x-2])
print(fib_number_list[n])