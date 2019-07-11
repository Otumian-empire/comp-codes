# Write a program to print the sum of squares of the elements of an array of size N. N can be any integer between 1 and 100. 

N = input()

# Get the input
numArray = map(int, input().split())

sum_integer = 0
# Write the logic to add these numbers here

for i in numArray:
    sum_integer += (i ** 2)

# Print the sum
print(sum_integer)
