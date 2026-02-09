# Comprehension : list comprehension, dict comprehension, etc

# faire 3 list comprehensions 1 dict comprehension 1 nettoyage de données (sans regarder le cours)

## List comprehension
# Multiplie par 2 les nombres impairs
nbr_impair_multi2 = [x * 2 for x in range(25) if x%2!=0]
print(nbr_impair_multi2)

# Garde seulement les fruits commençant par "p"
fruits = ["pomme", "mangue", "poire"]
fruits_en_p = [fruit for fruit in fruits if fruit[0][0]=="p"]
print(fruits_en_p)

# Enleve les fruits du panier de course
fruits = ["pomme", "mangue", "poire"] 
panier = ["fromage", "jus", "pomme", "carottes"]
panier_sans_fruits = [element for element in panier if element not in fruits]
print(panier_sans_fruits)

## Dict comprehension
# Nombre pair de 1 jusqu'à 100 inclus mis dans un dict
nbr_pair = {x:x for x in range (1, 101) if x%2==0}
print(nbr_pair)
 
nbr_pair_phytonique = {x:x for x in range (1, 101, 2)}
print(nbr_pair)

nbr_pair_index = {x:x for x in range (1, 101) if x%2==0}
print(nbr_pair)

pairs = range(2, 101, 2) # # Génère les nombres pairs de 2 à 100       
nbr_pair_avec_bon_index = {i: v for i, v in enumerate(pairs, start=1)} # Crée le dictionnaire : clé = index (1, 2, 3, etc), valeur = nombre pair
print(nbr_pair)

## Nettoyage de données
# Enlève les mails en doublons
mail = ["exemple@hotmail.fr", "ex@hotmail.fr", "exemple@hotmail.fr"]
cleaned_data_mail = list(set(mail))
print(cleaned_data_mail)

