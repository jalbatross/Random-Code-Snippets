#This file recursively finds the p times that an array 
#with length n originally consisting of sorted decreasing
#objects has been shifted.

import math;

originalArray = [10, 9 , 8, 7, 6, 5, 4, 3, 2, 1];
shiftedArray = [3, 2, 1, 10, 9, 8, 7, 6, 5, 4];

print (originalArray);
print (shiftedArray);

def findP(someArray, len):
    if len == 2 and someArray[0] < someArray[1]:
        return len;
    if someArray[0] > someArray[len - 1]:
        return 0;
    else:
        print("recur");
        newIndex = math.ceil(len/2);
        findP(someArray[0:newIndex], newIndex);

findP(shiftedArray,len(shiftedArray));