#This script iteratively finds the p times that an array 
#with length n originally consisting of sorted decreasing
#objects has been shifted.

def iterativeP(a, len):
    p = 0
    start = 0;
    end = len - 1;
    mid = 0;
    if (len % 2) == 0:
        mid = int((len/2) - 1);
    else:
        mid = int((len - 1)/2);
    while a[start] < a[end]:
        print ("start, end, mid: ", start,  " " , end , " " , mid)
        if end - start <= 1 :
           p = start;
           return p+ 1;
        if a[start] < a[mid]:
            end = mid
        else:
            start = mid
        if ((end - start) % 2) == 0:
            mid = int(((end - start) / 2) + start)
        else:
            mid = int(((end - start - 1) / 2) + start)

    return p + 1;

originalArray = [10, 9 , 8, 7, 6, 5, 4, 3, 2, 1];
shiftedArray = [3, 2, 1, 10, 9, 8, 7, 6, 5, 4];
shiftedLongArray = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9 , 8 , 7, 6, 5, 4, 3, 2, 1, 33, 32, 31, 30, 29, 28, 27, 26, 25]
print ("The array was shifted ", iterativeP(shiftedLongArray, 33) , " times");