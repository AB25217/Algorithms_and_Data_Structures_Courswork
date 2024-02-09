"""
Author:Aleksandar Bozov
File:To test out the time and memory complexity of a trial by division primality test method
"""
import time

def trial_by_division(n):
    if n==2:
        return True
    if n%2==0:
        return False
    if n==1 or n==0:
        return False
    for i in range(3,n):
        if n%i==0:
            return False
    return True
    

def test_range_of_numbers(m,n):
    if not 0<m<n:
        raise ValueError("m and n need to be greater than 0, and m needs to be smaller than n")
    prime_numbers=[]
    for i in range(m,n):
        if trial_by_division(i)==True:
            prime_numbers.append(i)
    return prime_numbers

start_time=time.time()
print(test_range_of_numbers(1,80000))
print(time.time()-start_time)