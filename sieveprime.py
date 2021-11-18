#!/usr/bin/env python 
#Sieve of Eratosthenes: algorithm steps for primes below a number

import time

def inquire_number():
    number = int (input("Hey!, enter an integer number n>1? "))
    return number

def sieveprime(n):
  notprimes = []
  primes = []
  for i in range(2, n+1):
      if i not in notprimes:
         primes.append(i)
      
         for j in range(i*i, n+1, i):
             notprimes.append(j)
  return primes
if __name__=="__main__":
    start_time = time.time()

    number = inquire_number()
    numbers = sieveprime(number) 
    print (numbers)

    execution_time = time.time() - start_time
    print("--- %s seconds ---" % execution_time)
