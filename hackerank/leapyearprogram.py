# We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we
# add it to the shortest month of the year, February.
# In the Gregorian calendar three criteria must be taken into account to identify leap years:
#     The year can be evenly divided by 4, is a leap year, unless:
#         The year can be evenly divided by 100, it is NOT a leap year, unless:
#             The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200,
# 2300 and 2500 are NOT leap years.Source
# Task
# You are given the year, and you have to write a function to check if the year is leap or not.
# Note that you have to complete the function and remaining code is given as template.
# Input Format
# Read y, the year that needs to be checked.
# Constraints 1900 <= y <= 10**5
# Output Format
# Output is taken care of by the template. Your function must return a boolean value (True/False)
# Sample Input 0
# 1990
# Sample Output 0
# False
# Explanation 0
# 1990 is not a multiple of 4 hence it's not a leap year. 
# def leapyear():
#     for i in range(1900, 10**5 + 1):
#         if (i % 4 == 0 or i % 400 == 0) and i % 100 != 0:
#             print(str(i) + " : " + str(True))
#         # else:
#         #     print(str(i) + " : " + str(False))


# print(leapyear())

# def IsYearLeap(year):
#     # if (year % 4 == 0):
#     #     if (year % 100 == 0):
#     #         if (year % 400 == 0):
#     #            return True     
#     if (year % 4 == 0 and year % 400 == 0) or year % 100 != 0:
#         return True

# IsYearLeap(2000)


# #
# # put your code here
 
# testdata = [1900, 2000, 2016, 1987]
# testresults = [False, True, True, False]
# for i in range(len(testdata)):
#     yr = testdata[i]
#     print(yr,"->",end="")
#     result = IsYearLeap(yr)
#     print(i)
#    # print(result)
    
#     if result == testresults[i]:
#            print("OK")
#     else:
#         print("Failed")

# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if (year % 4 == 0 and year % 100 != 0) or year % 4 == 0:
#         leap = True
#     # elif year % 100 != 0:
#     #     leap = False
    
#     return leap

# year = int(input("enter year: "))

# print(is_leap(year))




# def is_leap(year):
#     leap = False
    
#     # Write your logic here
#     if year % 400 == 0:
#         if year % 4 == 0:
#             leap = True
#         elif year % 100 == 0:
#             leap = False
    
#     return leap

# passn = 0
# sumn = 0
# years = []
# for i in range(1900, 10**5 + 1):
#     sumn += 1
#     if is_leap(i) == True:
#         passn += 1
#         years.append(i)

# print(str(passn) + "/" + str(sumn) + " test case passed")
# print(years, end ='', sep = ',')


def is_leap(year):
    
    # Write your logic here
   if year % 4 == 0:
      if year % 100 == 0:
         if year % 400 == 0:
            return True
         else:
             return False
      else:
           return True
   else:
        return False  
            

year = int(input("enter year: "))

print(is_leap(year))
