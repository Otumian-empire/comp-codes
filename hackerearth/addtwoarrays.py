# Write a program to add the corresponding elements of two arrays, each of size N and print the sums. N can be any integer between 1 and 100.
# Instructions:

#     We have defined an integer variable N for you.
#     We have provided the code to get the input for variable N.
#     We have defined integer arrays arrayNum1[N], arrayNum2[N] and arraySum[N]

#     We have provided the code to get the input for the array elements.
#     You have to write the logic to add the array elements.
#     Store the sum values in respective elements of variable arraySum
#     Print all the elements of arraySum[N]
#     with space between them
# Sample Input:
# N = 3
# arrayNum1 = 3 9 8

# arrayNum2 = 8 12 74

# Sample Output:
# 11 21 82

N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = []

# Write the logic here:
for i in range(N):
    sumArray.append(numArray1[i] + numArray2[i])

# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")
