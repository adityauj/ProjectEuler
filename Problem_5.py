# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:49:51 2021

@author: Aditya Ujeniya

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import sys

for i in range(1, 100000000000):
    for j in range(2,21):
        if i%j != 0:
            break
        if j==20:
            print(i)
            sys.exit();