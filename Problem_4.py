# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 22:41:59 2021

@author: Aditya Ujeniya

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
product = 0
collection = []

for i in range(999,99,-1):
    for j in range(999,99,-1):
        product = i*j
        string_product = str(product)
        if string_product == string_product[::-1]:
            collection.append(product)
            break

collection.sort()
print(collection[-1])