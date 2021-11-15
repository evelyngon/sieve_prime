#!/usr/bin/env python 

#algorithm Sieve of Eratosthenes

def inquire_number():
    number = int (input("Hey!, enter an integer number n>1? "))
    return number

def sieveprime(n):
  notprimes = []
  primes = []
  for i in range(2, n+1):
      if i not in notprimes:
         primes.append(i)
         print (i)
         for j in range(i*i, n+1, i):
             notprimes.append(j)

if __name__=="__main__":
    number = inquire_number()
    sieveprime(number)
