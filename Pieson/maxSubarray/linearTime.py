# Nonrecursive linear time algorithm for Maximum subarray sum problem
# 4.1-5 in CLRS

def linearSubarraySum(arr):
    var sum = 0
    var max = float('-inf')
    low, high = 0, 0
    for i in range(0, len(arr)):
        sum += a[i]
        if (sum >= max):
            high = i
            max = sum

#scratchwork:
# {3, 1, -5,0, -2, 6,7, 9, 2, -11, 4}
# a maximum subarray of {0, 5} is either
# a maximum subarray of {0,4} or a maximum subarray of 
# {1, 4} or {2, 4} or {3, 4} or {4, 4}

#Max subarray of {0 -> 2} is {0 -> 1}
#A maximum subarray of {0 -> 3} is either
#a maximum subarrayof {0 -> 2} OR a maximum subarray of {1, 3} OR {2, 3}
# OR {3, 3}

#if j+1 is Negative, then the maximum subarray of j+1 is a maximum subarray
# of {0 -> j}
# otherwise is j+1 is positive, then the maximum subarray of {0 -> j+1}
# is {0 -> j+1}
# if i know a maximum subarray from the points {0 -> j}
# develop a way to find a maximum subarray of {i -> j+1 } in constant time


#{-1, 2, 3}
#the maximum subarray seen at index 0 is -1
# the maximum subarray seen at index 1 is 1

#Knowing a maximum subarray of {-1, 2}, extend the answer to 
#find a maximum subarray ending att index 2 by using the following
#observation: a maximum subarray of {0, 2} is either:

# - A maximum subarray of {0, 1}
# OR - A subarray {1, 2} or {2,2}

#why are these mutually exclusive? That's what I don't understand.

# If max of {0, 1}, then cannot be a subarray {1, 2} or {2, 2} SINCE
# the index 2 is NOT INCLUDED in {0, 1}

#generally:

# A maximum subarray of the array {0, j} cannot be a subarray
# {0, j+1}, { 1, j+1}, ... {j+1 , j+ 1} because a maximum subarray
# of {0, j } does not ever include the index j+1. Otherwise it
# wouldn't be a subarray of {0, j}

# Now, the mutual exclusivity makes sense.

# Using this information, determine a maximum subarray of the form
# {i...j+1 } in constant time based on knowing a maximum subarray ending
# at index j.

# So it's either the maximum is the max from {0, j} or one of the 
# subarrays {0, j+1} ... {j+1, j+1}

#We can find the maximum subarray of {0, j+1} in time 
# (j +1 - 1) = j like so:
# say the max for {0, j} is subMax and we know it
# simply compare subMax to the sums for the subarrays:
# {0, j+1}, {1, j+1} , {2, j+1}, ... {j+1, j+1}
# then the max of these is the max subarray of {0, j+1}!

#this algorithm has j comparisons and j sums. For each step
# simply add a new value and compare it with subMax (2j time)

#Here would be the algorithm in action:

# say we have {3, -5, 1, 4, -7, 11, 1, -5, -6, 9, 2} as
# an array. Let's try to find the maximum subarray of {0, 3}
# given that the maximum subarray of {0, 2} is {0, 0}.

# A maximum subarray of {0, 3} is either the maximum subarray of {0, 2}
# = {0, 0} = 3 OR a subarray {0, 3}, {1, 3}, {2, 3}, {3, 3}

# j = 3
# subMax = 3
# sum of {3, 3} = 4
#  compare 4 to subMax = 3
#     4 >= 3 therefore assign realMax = {3, 3}
# sum of {2, 3} = subarraySum + a[2] = 4 + 1 = 5
#    compare 5 to realMax = 4
#       5 >= 4 so assign realMax = {2, 3}
# sum of {1, 3} = subarraySum + a[1] = 5 - 5 = 0
#   compare 0 to realMax = 5
#      no assign
# sum of {0, 3} = subArraySSum + a[0] = 3
#   compare 3 to realMax = 5
#      no assign
# found subArray max = 5 corresponding to {2, 3}
# at worst every step has like 6 assignments/comparisons total
#  there were j+1 total steps
#  so it's 6j + 6 total steps => O(j) whic is O(1) since j
#  is constant??
#   now do this linearly?

# n = 11
# {3, -5, 1, 4, -7, 11, 1, -5, -6, 9, 2}
# proceed from left to right
# maximum subarray of {0,0 } is 3 (1 op)
#
# Find max subarray of {0, 1} now
#    compare 3 to {1, 1} = -5 (1 op)
#       assign (1 op)
#    add 3 to {0, 1} (1 op)
#       compare 3 to -2 (1 op)
# Max subarray of {0, 1} is {0, 0} = 3
#
# Find max subarray of {0, 2} now
#   compare 3 to {2,2} (1 op)
#   add a[1] to {2, 2} (1 op)
#   compare 3 to {1,2} = -4 (1 op)
#   add a[0] to {1, 2} (1 op)
#   compare 3 to {0, 2} 1 op
# Max subarray of {0,2} is {0,0} = 3
# ===STOP===
#   The algorithm is not constant time
#   it runs at worst in like 6j steps
#   so if I have n items thats 6n^2 which is awful!!
# time to rethink algorithm 
# A maximum subarray of {i, ..., j+1} is either a  max subarray
# of {i, ..., j} or a subarray {k, ..., j+1} for i <= k <= j+1
# Can find the maximum of k, ..., j+1 in j+1 - k time easily (actually 2* (j+1 - k))
# then add one to compare it to the maximum of {i, ..., j}... BUT THATS NOT CONSTANT
# THATS 2J TIME!!
#
# Time to think...
#   Need to find the maximum sum of the subarrays 
#      {5,2, -1, -3, 4, 7}
#      FIND MAX SUM OF: 5 + 2 - 1 - 3 + 4 + 7
#                           2 - 1 - 3 + 4 + 7
#                             - 1 - 3 + 4 + 7
#                                 - 3 + 4 + 7
#                                       4 + 7
#                                         + 7
#  A maximum subarray of [i...j+1] is a maximum subarray of
#  [i...j] or a subarray [i+1...j+1]...[j-1...j+1],[j+1.,j+1].
# We know the maximum subarray [i...j]. It's some subset:
#   [i1, i2, i3, ... p], p <= j. Call this origSum
#   now we need to find the maximum of the subarrays [i+1...j+1]...[j+1,j+1]
#   So consider the original set [i...j]:
#   [i1, i2, i3, ..., p, ..., j, j+1]
#     When we're comparing the subarray sums [p+1, ..., j+1] we only need to check up to
#     p+1, since if the subarray sum [p+1, ..., j+1] > 0 then if we add  it to the
#     oldSum obviously it'll be greater than oldSum.
#     Is that constant time though? NO it's j - p which is at worst case j....
#     HMMMMMM