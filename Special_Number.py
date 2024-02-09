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
    def _isPalindromic(self,num):
        """
        A method that will check whether a given number is an palindromic
        (reads the same from backwards)
        """
        self.isPalidromic = True # assuming that the number is already palidromic if given
        if num <=9: # if number is a single digit
            return self.isPalidromic # return that the number is indeed a palidromic
        self.digits = [i for i in str(num)] # converts num into string and stores each of its digits into an list. 
        for i in self.digits[-2::-1]: # for each digit of the number, starting from the second to second to last digit and ending at the first digit
            self.digit = i #store element digit in memory, for easier deletion 
            self.digits.remove(i) # remove digit from its initial position in the array
            self.digits.append(self.digit) # now append the digit to the tail of the list.
        self.new_number = ''.join(self.digits) # join all elements in the string to a 
        if num == int(self.new_number): # if the new inverted number is equal in value to the initial number
            return self.isPalidromic # return that the number is palidromic
        else:
            self.isPalidromic = False # the number is not palidromic
            return self.isPalidromic # return false

            
    def find_special_numbers(self,m,n):
        """
        A function that will find special numbers between n and m. Special numbers are prime numbers and
        palindromic numbers
        """
        if m >= n:
            raise ValueError("m cannot be larger than n")

        prime_numbers = [True for i in range(n)]
        prime_numbers[0] = False
        prime_numbers[1] = False

        for i in range(2, int(n**0.5)):
            if prime_numbers[i] == True:
                for j in range(int(i**2), n, i):
                    prime_numbers[j] = False
        

        self.prime_numbers_array = [i for i in range(m,n) if prime_numbers[i] == True and self._isPalindromic(i) == True]        

        return f"{m}: {self.prime_numbers_array[0:3]}, {self.prime_numbers_array[-4:-1]}" # list the first and last 3 special numbers