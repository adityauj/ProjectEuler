"""
Created on Sat Apr 24 21:42:28 2021

@author: Aditya Ujeniya

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

f1=1
f2=2
flag=0
numbers=[f1, f2]
count=0

for i in range(1, 32):
     if flag==0:
         f3=f1+f2
         numbers.append(f3)
         f1=f3
         flag=1
         continue
     if flag==1:
         f3=f1+f2
         numbers.append(f3)
         f2=f3
         flag=0
         continue
     
for i in numbers:
    if i%2==0:
        print(i)
        count += i
        
print(count)