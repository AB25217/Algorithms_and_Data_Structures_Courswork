"""
Author: Aleksandar Bozov
Time and Date: 21:42 02/02/2024
Purpose: File that will tests the is_Palidromic function if it recognises palidromic numbers
"""
from Special_Number import Special_Number_Finders
import time

def testing_palidromic_function(number):
    """
    Tests palidromic function of the special numbers finders function
    """
    a = Special_Number_Finders()
    start_time = time.time()
    return f"Number was {number}, and it was palidromic?{a._isPalindromic(number)}. Total Running time was {time.time() - start_time}"

#Test Case 1: Numbers that are palidromic
test_case1 = [121, 4, 2, 181, 1881 , 8888, 10]
for i in test_case1:
    print(testing_palidromic_function(i))
#passed all tests
    

print("   ")

#Test Case 2: Numbers that are NOT palidromic
test_case2 = [43,98,83,1848,1412,1122]
for i in test_case2:
    print(testing_palidromic_function(i))
#passed all tests

print(" ")

#Test Case 3: time complexity with ranging number sizes
test_case3 = [1,11,111,1111,11111,1111111,1111111111111111,11111111111111111111111111111111111111111111111]
for i in test_case3:
    print(testing_palidromic_function(i))
