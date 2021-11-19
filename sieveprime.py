#!/usr/bin/env python 
#Sieve of Eratosthenes: algorithm steps for primes below a number

def inquire_input():
    while True:
        number = input("Please enter an integer number greater than 1: ")
        try:
            value = int(number)
            if value > 1:
                break
            else:
                print("Number can't be negative, try again")
        except ValueError:
            print("Input must be an integer number greater than 1, try again")

    return value

import time


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
    number = inquire_input()
    start_time = time.time()
    numbers = sieveprime(number) 
    print (numbers)

    execution_time = time.time() - start_time
    print("--- %s seconds ---" % execution_time)
