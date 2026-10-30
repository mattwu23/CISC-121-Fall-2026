# FrogJmp Solution
def solution(X, Y, D):
    distance = Y - X # start at point x, getting to point y
    jumps = distance//D # counts full jumps that fit in that distance
    if distance & D !=0: # if some distance is left over, one more jump is needed
        jumps += 1
    return jumps # return minimum number of jumps

#PermCheck Solution
def solution (A):
    n = len(A) # length of A is the highest number in the permutation
    seen_values = set() # create empty set to track what numbers have been found
    for i in A:
        if i > n or i in seen_values: # conditions where we skip adding i to seen_values
            return 0 # return 0 if not permutation
        seen_values.add (i) # if i passes the previous conditions, add to seen_values
    return 1 # return 1 if permutation

#CyclicRotation Solution
def solution (A, K):
	if len(A) == 0: # if length of A is 0, return it as is
        return A
	for i in range(K): # loop through all values of K
		last = A.pop() # set last as the last value in A using -pop
		A.insert(0, last) # insert that value in the first position of A
    return A

#PassingCars
def solution (A):
    zeros = 0 # create variable zero, increases when we see a 0 in the input
    total = 0 # create variable total, increases when we get a pair of passing cars
    for car in A:
        if car = 0:
            zeros+=1 # east moving car, remember for west moving cars
        else:
            total+=zeros # pair of east moving car with west 
            if total>1000000000: #stop early if passes the limit
                return -1
    return total # return the total amount of pairs

#FrogRiverOne
def solution(X, A):
    covered_spots = set() #empty set to track what spots have been covered
    for time in range(len(A)):
        covered_spots.add (A[time]) # add time where the spot is covered
        if len (covered_spots) = X: #if the length of covered spots is the desired length
            return time
    return -1 # return -1 if you can never cross
