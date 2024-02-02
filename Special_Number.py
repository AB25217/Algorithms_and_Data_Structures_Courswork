"""
Author: Aleksandar Bozov

Time and Date: 17:56 02/02/2024

Purpose: A file containing the code that will find special numbers from a specified range
"""

class Special_Number_Finders:
    def __init__(self) -> None:
        """
        A class that will find out special numbers from an range specified
        """
        pass

    def _isPrime(self, num):
        """
        A method that will find whether a number is a Prime or not
        """
        self.prime_number = True # num is assumed to be prime unless proven otherwise
        for i in range(2, num): # for every number in range of the number provided, except 0 and 1
            if num % i == 0: # if num can be divided with no remainded
                self.prime_number = False # num cannot be prime
                return self.prime_number # return False
        return self.prime_number # if num is not disproven to be a prime number, return that it is
    


            


