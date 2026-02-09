
'''1.1. Create a list of your favorite movies and print the last one using negative indexing.
1.2. Create a tuple of three numbers and calculate their sum.
1.3. Create a dictionary to store information about a book (title, author, year), and add the publisher's name.'''

'''2.1. Count occurrences of names in the dataset above
2.2. Extract all unique names
2.3. Create a dict mapping names to average age
2.4. Rewrite exercises using comprehensions'''

'''3.1. Supprimer les doublons d’une liste de labels
3.2. Calculer la moyenne des scores par individu
3.3. Extraire noms et âges depuis un dataset imbriqué
3.4. Compter les occurrences d’une variable cible
3.5. Reproduire un `value_counts` à la main'''

# Exercise 1.1 : list
favorite_movies = ["Shutter_island", "Inception", "Attrape-moi si tu peux", "Interstellar", "Léon", "Wasabi"]

print(favorite_movies[-1])

# Exercise 1.2 : tuple
weekly_expenses = (27, 4, 16)

print(sum(weekly_expenses))

# Exercise 1.3
book = {
  "title" : "Orgueil et Préjugés",
  "author" : "Jane Austen",
  "year" : 1813,
}

book.update({"publisher" : "T. Egerton, Whitehall"})
print(book)

# list de dict (dict imbriqué)
books = [
  {"title" : "Orgueil et Préjugés",
  "author" : "Jane Austen",
  "year" : 1813,},

  {"title" : "Northanger Abbey",
  "author" : "Jane Austen",
  "year" : 1817}]

books[0].update({"publisher": "T. Egerton, Whitehall"})   # premier livre
books,[1].update({"publisher": "John Murray"})            # second livre
print(books)

# Exercise 2 (2.1 to 2.4)
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 40}
]

#for person in data : 
  

