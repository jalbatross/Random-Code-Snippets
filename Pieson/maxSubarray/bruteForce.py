#Finds the maximal contiguous subarray sum of
#an array in n^2 time

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

array = [-1, -2, 30, 50, 2, 5, -13, 8, -99, 5, 10, -22, 16, -4, 8, -10, 7, 0, 1]
print("Max was", bruteMax(array));