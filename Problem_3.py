# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:05:29 2021

@author: Aditya Ujeniya

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math
  
# A function to print all prime factors of 
# a given number n
def primeFactors(n):
      
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2),
        n = n / 2
          
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
          
        # while i divides n , print i ad divide n
        while n % i== 0:
            print(i)
            n = n / i
              
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)
          
# Driver Program to test above function
  
n = 600851475143
primeFactors(n)
        
