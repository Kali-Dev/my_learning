# Uses python3
# -*- coding: utf-8 -*-
"""
@author: kalip

MaximumPairwiseProductProblem
Find the maximum product of two distinct numbers in a 
sequence of non-negative integers. 
Input: Asequenceofnon-negative integers. 
Output: The maximum value that can be obtained by multiplying 
two diﬀerent elements from the sequence.

"""
#num_list = [5,6,2,7,4]
"""n = int(input()) 
num_list = [int(x) for x in input().split()]
assert(len(num_list)==n)
product = 0
for idx,num in enumerate(num_list):
    for num2 in num_list[idx+1:]:
        if num!=num2:
            if num*num2 > product:
                product = num*num2
           
print(product)

"""
# the above algorithm takes n2 operations
# but all we need is max number of the list and second max number of 
# list to get max pair product

"""
n = int(input())
num_list = [int(x) for x in input().split()]
assert(len(num_list)== n)
max_ind = 0
max_num = 0
for idx,num in enumerate(num_list):
    if num > max_num:
        max_ind = idx
        max_num = num

max_num2 = 0
for idx2,num2 in enumerate(num_list):
    if (idx2 != max_ind) & num2>max_num2:
                max_num2 = num2
                max_ind2 = idx2
print(max_num*max_num2)
"""
n = int(input())
num_list = [int(x) for x in input().split()]
assert(len(num_list)== n)
sort_list = sorted(num_list)
print(sort_list[-1]*sort_list[-2])
