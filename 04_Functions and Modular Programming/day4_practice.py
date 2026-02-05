'''Practice Exercises :
1. Write a function that checks if a number is odd or even.
2. Create a function that calculates the factorial of a number.
3. Develop a module with utility functions for basic arithmetic operations.
4. Explore and use the random module to generate random numbers. --> voir fichiers random

Disclaimer : exceptionnellement les import se situent au début des exercices et non pas au début du fichier 
pour plus de compréhension'''

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

# Exercise 4 : Doc random, mise en forme via un LLMs pour plus de rapidité

import random

# Exemples de base :

# 1. random() – flottant aléatoire dans [0.0, 1.0)
print("random() :", random.random())

# 2. uniform(a, b) – flottant aléatoire dans [a, b]
print("uniform(2.5, 10.0) :", random.uniform(2.5, 10.0))

# 3. expovariate(lambd) – intervalle exponentiel (λ = 1/5 → moyenne 5)
print("expovariate(1/5) :", random.expovariate(1/5))

# 4. randrange(stop) – entier de 0 à stop‑1
print("randrange(10) :", random.randrange(10))

# 5. randrange(start, stop, step) – entier avec pas
print("randrange(0,101,2) :", random.randrange(0, 101, 2))

# 6. choice(seq) – élément aléatoire d’une séquence
print("choice(['win','lose','draw']) :", random.choice(['win', 'lose', 'draw']))

# 7. shuffle(seq) – mélange in‑place d’une liste
deck = 'ace two three four'.split()
random.shuffle(deck)
print("shuffle(deck) :", deck)

# 8. sample(population, k) – k échantillons sans remise
print("sample([10,20,30,40,50], k=4) :", random.sample([10, 20, 30, 40, 50], k=4))


# Simulations :

import numpy as np

# ----------------------------------------------------------------------
# 1. Six spins of a roulette wheel (weighted sampling with replacement)
# ----------------------------------------------------------------------
roulette = random.choices(
    population=['red', 'black', 'green'],
    weights=[18, 18, 2],          # 18 red, 18 black, 2 green
    k=6
)
print("Roulette spins (6) :", roulette)

# ----------------------------------------------------------------------
# 2. Deal 20 cards without replacement from a 52‑card deck
#    and compute the proportion of ten‑value cards (10, J, Q, K)
# ----------------------------------------------------------------------
# 16 ten‑value cards, 36 other cards
deck = np.array(['tens'] * 16 + ['low cards'] * 36)
deal = np.random.choice(deck, size=20, replace=False)
prop_tens = np.count_nonzero(deal == 'tens') / 20
print("Deal (20 cards) :", deal.tolist())
print("Proportion of ten‑value cards :", prop_tens)

# ----------------------------------------------------------------------
# 3. Estimate P(≥5 heads) in 7 biased coin flips (p(head)=0.6)
# ----------------------------------------------------------------------
n_trials = 10_000
heads_counts = np.random.binomial(n=7, p=0.6, size=n_trials)
prob_ge_5 = np.mean(heads_counts >= 5)
print("Estimated P(≥5 heads in 7 flips) :", prob_ge_5)

# ----------------------------------------------------------------------
# 4. Probability that the median of 5 samples lies in the middle two quartiles
#    (i.e. between 2 500 and 7 500 for a uniform 0‑9 999 range)
# ----------------------------------------------------------------------
def trial():
    sample = random.choices(range(10_000), k=5)   # with replacement
    median = sorted(sample),[2],                    # 3ᵉ élément = médiane
    return 2_500 <= median < 7_500

n_trials = 10_000
prob_median = sum(trial() for _ in range(n_trials)) / n_trials
print("Probability median in middle two quartiles :", prob_median)

''' Exemple de *bootstrapping* statistique utilisant le ré-échantillonnage avec remise 
 pour estimer un intervalle de confiance pour la moyenne d'un échantillon :
 Estimation d’un intervalle de confiance (IC) à 90 % pour la moyenne
d’un petit échantillon, par ré‑échantillonnage avec remise.
 https://www.thoughtco.com/example-of-bootstrapping-3126155'''

from statistics import fmean as mean
from random import choices

data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]

# 10 000 ré‑échantillons (plus d’itérations → IC plus stable)
n_boot = 10_000
boot_means = sorted(mean(choices(data, k=len(data))) for _ in range(n_boot)) # tirage avec remise de la même taille

# 90 % IC = 5ᵉ et 95ᵉ percentile (0,05 et 0,95)
lower = boot_means[int(0.05 * n_boot)]
upper = boot_means[int(0.95 * n_boot)]

print(f"Échantillon original, moyenne = {mean(data):.2f}")
print(f"IC à 90 % (bootstrapping) : [{lower:.2f} , {upper:.2f}]")

# permutation_test.py
# Test non paramétrique de la différence de moyennes entre deux groupes
# par permutation (ré‑échantillonnage sans remise du groupe combiné).

from statistics import fmean as mean
from random import shuffle, seed

# Données
drug    = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]

observed_diff = mean(drug) - mean(placebo) # différence observée
combined = drug + placebo # pool de toutes les observations

n_perm = 10_000
count_ge = 0  # nombre de permutations ≥ |observed|

seed(0) # reproductibilité (facultatif)

for _ in range(n_perm):
    shuffle(combined) # mélange aléatoire du pool
    # reconstitue deux groupes de même taille que les originaux
    perm_drug = combined[:len(drug)]
    perm_placebo = combined[len(drug):]
    perm_diff = mean(perm_drug) - mean(perm_placebo)
    if abs(perm_diff) >= abs(observed_diff):
        count_ge += 1

p_value = count_ge / n_perm

print(f"Différence observée = {observed_diff:.2f}")
print(f"Valeur‑p (permutation, {n_perm} tirages) = {p_value:.4f}")