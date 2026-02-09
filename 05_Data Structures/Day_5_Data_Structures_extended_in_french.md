# 📘 Jour 5 : Structures de données en Python

Bienvenue au **Jour 5** du **30 Days of Data Science** 🎯  
Aujourd’hui, nous étudions les **structures de données fondamentales en Python**, indispensables pour :

- l’analyse de données
- le machine learning
- le deep learning
- la computer vision
- les tests techniques en entretien

---

## 📚 Table des matières

1. Listes (`list`)
2. Tuples (`tuple`)
3. Dictionnaires (`dict`)
4. Ensembles (`set`)
5. Compréhensions (lists / dicts / sets)
6. Structures imbriquées (datasets réels)
7. Bonnes pratiques & complexité
8. Exercices orientés Data Science
9. Résumé

---

## 1️⃣ Les listes (`list`) 📋

### Définition
Une **liste** est une collection :
- ordonnée
- mutable (modifiable)
- pouvant contenir des types variés

### Création
```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.14, True]
```

### Accès aux éléments
```python
fruits = ["apple", "banana", "cherry"]

fruits[0]     # "apple"
fruits[-1]    # "cherry"
```

### Ajouter des éléments
```python
fruits.append("orange")   # ajoute à la fin
fruits.insert(1, "kiwi")  # insère à une position précise
```

### Supprimer des éléments
```python
fruits.remove("banana")  # supprime par valeur
fruits.pop(0)            # supprime par index et retourne l’élément
```

### Découpage (slicing)
```python
numbers = [1, 2, 3, 4, 5]

numbers[:3]    # [1, 2, 3]
numbers[2:]    # [3, 4, 5]
numbers[::2]   # [1, 3, 5]
```

### Méthodes essentielles
```python
numbers.sort()       # trie la liste
numbers.reverse()    # inverse l’ordre
numbers.count(2)     # compte les occurrences
len(numbers)         # taille de la liste
```

📌 **En data science** :  
Les listes servent souvent de structures intermédiaires avant conversion en `numpy.array` ou `pandas.Series`.

---

## 2️⃣ Les tuples (`tuple`) 🔗

### Définition
Un **tuple** est :
- ordonné
- **immuable**
- idéal pour des données fixes ou structurées

### Création
```python
point = (3, 5)
rgb = (255, 0, 0)
```

### Accès
```python
point[0]  # 3
```

### Retours multiples de fonctions (très courant)
```python
def min_max(values):
    return min(values), max(values)

result = min_max([1, 4, 2, 9])
print(result)
# Output : (1, 9)
```

Décomposition automatique :
```python
minimum, maximum = min_max([1, 4, 2, 9])
```

📌 **Cas d’usage data / ML** :
- coordonnées
- statistiques (min, max, moyenne)
- dimensions d’images `(height, width, channels)`

---

## 3️⃣ Les dictionnaires (`dict`) 📖

### Définition
Un **dictionnaire** associe :
- une clé (unique, immuable)
- à une valeur (tout type)

- pas de doublons
- ordonnés

### Création
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"
}
```

### Accès
```python
person["name"]  # "Alice"
```

### Ajout / modification
```python
person["job"] = "Data Scientist"
person["age"] = 26
```

### Suppression
```python
del person["city"]      # supprime définitivement
person.pop("age")       # supprime et retourne la valeur
```

### Méthodes courantes (avec explications)
```python
person.keys()    # retourne toutes les clés
# dict_keys(['name', 'job'])

person.values()  # retourne toutes les valeurs
# dict_values(['Alice', 'Data Scientist'])

person.items()   # retourne (clé, valeur)
# dict_items([('name', 'Alice'), ('job', 'Data Scientist')])
```

📌 **Très important en data science** :
- APIs (JSON)
- annotations d’images
- résultats de modèles
- features nommées

---

## 4️⃣ Les ensembles (`set`) ⭐

### Définition
Un **set** est :
- non ordonné
- sans doublons
- extrêmement rapide pour les comparaisons

### Création
```python
labels = {1, 2, 2, 3}
print(labels)
# Output : {1, 2, 3}
```

### Opérations utiles (avec output)
```python
A = {1, 2, 3}
B = {3, 4, 5}

A | B   # union
# Output : {1, 2, 3, 4, 5}

A & B   # intersection
# Output : {3}

A - B   # différence
# Output : {1, 2}
```

### Cas d’usage data science

**1️⃣ Suppression de doublons**
```python
data = [1, 2, 2, 3, 3, 3]
unique_data = list(set(data))
# [1, 2, 3]
```

**2️⃣ Comparaison de labels (ML)**
```python
true_labels = {0, 1, 2}
predicted_labels = {1, 2, 3}

missing = true_labels - predicted_labels
# {0}
```

**3️⃣ Nettoyage de données**
```python
invalid_values = {"NA", "NULL", ""}
cleaned = [x for x in data if x not in invalid_values]
```

---

## 5️⃣ Compréhensions ⭐⭐⭐

### Pourquoi c’est important ?
Les compréhensions permettent :
- un code plus **lisible**
- plus **rapide**
- plus **pythonique**
- très apprécié en entreprise et en entretien

### List comprehension (forme générale)
```python
[expression/action for element in iterable if condition(optionnel)] # De droite à gauche 
```

### Exemple simple
```python
squares = [x**2 for x in range(10)]
```

### Avec condition
```python
even_numbers = [x for x in range(20) if x % 2 == 0] # pas de print ou return car stocker dans la variable
```

### Dict comprehension
```python
square_dict = {x: x**2 for x in range(5)}
```

### Set comprehension
```python
unique_lengths = {len(word) for word in ["cat", "dog", "mouse"]}
```

📌 **En data science** :
- feature engineering
- nettoyage
- transformation rapide de datasets

---

## 6️⃣ Structures imbriquées ⭐⭐⭐

### Exemple réaliste (mini dataset)
```python
dataset = [
    {"name": "Alice", "age": 25, "scores": [80, 90, 85]},
    {"name": "Bob", "age": 30, "scores": [70, 88, 92]}
]
```

### Accès
```python
dataset[0]["scores"][1]
# 90
```

### Calcul réel
```python
averages = [
    sum(person["scores"]) / len(person["scores"])
    for person in dataset
]
```

📌 **C’est exactement la structure avant Pandas**.

---

## 7️⃣ Bonnes pratiques & performance

| Structure | Test d’appartenance |
|---------|---------------------|
| list    | lent (O(n))         |
| set     | rapide (O(1))       |
| dict    | rapide (O(1))       |

| Use Case           | Best Structure |
|--------------------|----------------|
| Ordered collection | List           |
| Fixed data         | Tuple          |
| Key-value lookup   | Dict           |
| Uniqueness         | Set            |

---

## 🧠 Exercices orientés Data Science

1. Supprimer les doublons d’une liste de labels
2. Calculer la moyenne des scores par individu
3. Extraire noms et âges depuis un dataset imbriqué
4. Compter les occurrences d’une variable cible
5. Reproduire un `value_counts` à la main

---

## 🌟 Résumé

✔ Listes → flexibles  
✔ Tuples → données fixes & retours multiples  
✔ Dictionnaires → structure des datasets  
✔ Sets → unicité, comparaison, nettoyage  
✔ Compréhensions → Python professionnel  
✔ Structures imbriquées → données réelles  
