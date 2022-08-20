#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    b=arr[n-1]
    for i in range(n,0,-1):
        
        if b<arr[i-1]:
            if i-1==0:
                arr[1]=arr[0]
                for i in range(n):
                    print(arr[i],end=" ")
                arr[0]=b
                for i in range(n):
                    print(arr[i],end=" ")
                
                return
            else:
                arr[i]=arr[i-1]
                for i in range(n):
                    print(arr[i],end=" ")
            print()
        elif b>arr[i-1]:
            
            arr[i]=b
            for i in range(n):
                print(arr[i],end=" ")
            print()
            return
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

