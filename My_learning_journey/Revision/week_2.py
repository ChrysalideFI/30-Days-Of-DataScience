# Day 1, Comprehension : list comprehension, dict comprehension, etc

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

# Day 2, extraire stats simple d'une list of dicts : mean, count (à la main)
ventes_02_2026 = [
    {"nom": "Produit A", "ventes": 120, "revenu": 2400.0},
    {"nom": "Produit B", "ventes": 85,  "revenu": 1700.0},
    {"nom": "Produit C", "ventes": 47,  "revenu":  940.0},
    {"nom": "Produit D", "ventes": 132, "revenu": 2640.0},
]

# Total des produits
count_produits = 0
for produit in ventes_02_2026 : 
  count_produits+=1
print(count_produits)

# Autre façon de fiare plus simple
count_produits=(len(ventes_02_2026))
print(count_produits)

# Moyenne des ventes
total_ventes = sum(item["ventes"] for item in ventes_02_2026)
mean_ventes = total_ventes/count_produits
print(mean_ventes)

# Day 3 
ventes_02_2026 = [
    {"nom": "Produit A", "ventes": 120, "revenu": 2400.0},
    {"nom": "Produit B", "ventes": 85,  "revenu": 1700.0},
    {"nom": "Produit C", "ventes": 47,  "revenu":  940.0},
    {"nom": "Produit D", "ventes": 132, "revenu": 2640.0},
]
  
def stats_simple(ventes):
    if not ventes:                     # protection contre liste vide
        return 0, None, None

    # somme des ventes
    total_ventes = sum(vente["ventes"] for vente in ventes)

    # moyenne
    moyenne_ventes = total_ventes / len(ventes)

    # listes des valeurs de ventes
    list_ventes = [vente["ventes"] for vente in ventes]

    # min / max
    min_ventes = min(list_ventes)
    max_ventes = max(list_ventes)

    return moyenne_ventes, min_ventes, max_ventes

print(stats_simple(ventes_02_2026))

