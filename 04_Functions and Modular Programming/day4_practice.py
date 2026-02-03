'''Practice Exercises :
1. Write a function that checks if a number is odd or even.
2. Create a function that calculates the factorial of a number.
3. Develop a module with utility functions for basic arithmetic operations.
4. Explore and use the random module to generate random numbers.'''

# Exercise 1

def nbr_odd_even (number):
  if number % 2 == 0 : 
    result = "This number is even"
  else : 
    result = "This number is odd"
  return result

print(nbr_odd_even(42))

# Exercise 2

def factorial(number):
  result = 1
  for i in range (1,number+1):
    result *= i 
  return result

print(factorial(4))

# Exercise 3

from .math_utils import exponentiation # . Signifie que le fichier est dans le même dossier

result = exponentiation(2, 4)
print (result)

# Autre possibilité, si je veux utiliser beaucoup de fonctions du module sans toute les cités dans l'import : 
from . import math_utils

result = math_utils.exponentiation(2, 4)
print (result)

