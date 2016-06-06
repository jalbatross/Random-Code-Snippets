#Finds the maximal contiguous subarray sum of an array recursively.
#Runs in nlogn time.

import math
import time
import random

def bruteMax(A):
    max = A[0];
    sum = A[0];
    low = 0;
    high = len(A) - 1;
    for i in range(0, len(A)-1):
        sum=A[i];
        for j in range(i+1, len(A) -1):
            sum += A[j];
            if sum >= max:
                max = sum;
                high = j;
                low = i;
    return (low, high, max);

def findMaxCrossingSubarray(arr, low, mid, high):
    leftSum =float('-inf')
    sum, maxLeft, maxRight = 0, 0, 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    rightSum = float('-inf')
    sum = 0
    for j in range(mid, high):
        sum += arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j

    return (maxLeft, maxRight, leftSum + rightSum - arr[mid])

def findMaxSubarray(arr, low, high):
    if low == high:
        return (low,high, arr[high])
    else:
        mid = math.floor((low + high)/2)
        (leftLow, leftHigh, leftSum) = findMaxSubarray(arr, low, mid)
        (rightLow, rightHigh, rightSum) = findMaxSubarray(arr, mid+1, high)
        (midLow, midHigh, midSum) = findMaxCrossingSubarray(arr, low, mid, high)
    if leftSum >= rightSum and leftSum >= midSum:
        return (leftLow, leftHigh, leftSum)
    elif rightSum >= leftSum and rightSum >= midSum:
        return (rightLow, rightHigh, rightSum)
    else:
        return (midLow, midHigh, midSum)

def recursiveAlt(arr, low, high):
    if high - low <= 93:
        return bruteMax(arr)
    elif low == high:
        return(low, high, arr[high])
    else:
        mid = math.floor((low + high)/2)
        (leftLow, leftHigh, leftSum) = findMaxSubarray(arr, low, mid)
        (rightLow, rightHigh, rightSum) = findMaxSubarray(arr, mid+1, high)
        (midLow, midHigh, midSum) = findMaxCrossingSubarray(arr, low, mid, high)
    if leftSum >= rightSum and leftSum >= midSum:
        return (leftLow, leftHigh, leftSum)
    elif rightSum >= leftSum and rightSum >= midSum:
        return (rightLow, rightHigh, rightSum)
    else:
        return (midLow, midHigh, midSum)

variableArray = [5, -1]
size = 2
timeBrute , timeRecurse, timeRecurseAlt = -1, 0, 0
start= 0

while (timeBrute < timeRecurse):
    variableArray.append(random.uniform(-100,100))
    start = time.clock()
    bruteMax(variableArray)
    timeBrute = time.clock() - start

    start = time.clock()
    findMaxSubarray(variableArray, 0, len(variableArray)-1)
    timeRecurse = time.clock() - start

    start = time.clock()
    recursiveAlt(variableArray, 0, len(variableArray)-1)
    timeRecurseAlt = time.clock() - start

    size += 1

print("Recursive was found to be faster at n= ", size, " \n Brute time: ", timeBrute, 
      "\n recursive time: ", timeRecurse, '\n  Alt recursive time: ',
      timeRecurseAlt)


print("===== Comparison of alternate recursive and Bruteforce===")
variableArray = []
size = 1
timeBrute , timeRecurseAlt = -1, 0
start= 0

while (timeBrute < timeRecurseAlt):
    variableArray.append(random.uniform(-100,100))
    start = time.clock()
    bruteMax(variableArray)
    timeBrute = time.clock() - start

    start = time.clock()
    recursiveAlt(variableArray, 0, len(variableArray)-1)
    timeRecurseAlt = time.clock() - start

    size += 1

print("Alternate recursive faster at n=" , size, 
      "\n Brute time: ", timeBrute, 
      "\n Alt recursive time: ", timeRecurseAlt)

#Answer to 4.1-3 in CLRS:
# The problem size n_0 that gives the crossover point at which the
# recursive algorithm beats the brute force algorithm  is approximately
# 92. 
#
#Changing the base case of the recursive algorithm to use the brute-force
#algorithm whenever the problem size is less than n_0 changes the crossover
#point to around n_0 = 2 usually. There is some variation.
