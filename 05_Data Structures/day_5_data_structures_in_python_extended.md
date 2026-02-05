# 📘 Day 5: Data Structures in Python (Extended – Expert Track)

This document is an **extended, production-ready version** of Day 5. It is sufficient for:
- Data analysis (EDA)
- Machine Learning
- Technical interviews
- Long-term Python expertise

---

## Table of Contents
- Lists
- Tuples
- Dictionaries
- Sets (NEW)
- Iteration Patterns
- Comprehensions (CRITICAL)
- Nested Data Structures (Data Use-Cases)
- Performance & When to Use What
- Practice Exercises (Extended)

---

## 1️⃣ Lists in Python 📋

### Key Properties
- Ordered
- Mutable
- Allows duplicates

### Iteration
```python
numbers = [1, 2, 3]
for n in numbers:
    print(n)
```

### Nested Lists
```python
matrix = [[1, 2], [3, 4]]
print(matrix[0][1])  # 2
```

### List Comprehensions (ESSENTIAL)
```python
squares = [x**2 for x in range(10) if x % 2 == 0]
```

---

## 2️⃣ Tuples in Python 🔗

### When to Use Tuples
- Fixed collections
- Function returns
- Dictionary keys

### Tuple Unpacking
```python
point = (10, 20)
x, y = point
```

---

## 3️⃣ Dictionaries in Python 📖

### Iteration Patterns
```python
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, value)
```

### Safe Access
```python
age = person.get("age", 0)
```

### Dictionary Comprehensions
```python
squares = {x: x**2 for x in range(5)}
```

---

## 4️⃣ Sets in Python ⭐ (CRITICAL & OFTEN MISSED)

### Why Sets Matter in Data Science
- Remove duplicates
- Fast membership tests
- Mathematical operations

```python
numbers = [1, 2, 2, 3]
unique = set(numbers)
```

### Operations
```python
a = {1, 2, 3}
b = {3, 4}
print(a & b)  # intersection
print(a | b)  # union
```

---

## 5️⃣ Nested Data Structures (REAL DATA CASES)

### List of Dictionaries (Dataset Pattern)
```python
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Alice", "age": 40}
]
```

### Common Operations
```python
ages = [p["age"] for p in data]
avg_age = sum(ages) / len(ages)
```

---

## 6️⃣ Performance & Choice Guide

| Use Case | Best Structure |
|-------|----------------|
| Ordered collection | List |
| Fixed data | Tuple |
| Key-value lookup | Dict |
| Uniqueness | Set |

- List lookup: O(n)
- Dict/Set lookup: O(1)

---

## 🧠 Extended Practice Exercises

1. Count occurrences of names in the dataset above
2. Extract all unique names
3. Create a dict mapping names to average age
4. Rewrite exercises using comprehensions

---

## 🌟 Final Summary

If you master:
- Lists + comprehensions
- Dicts + iteration
- Sets
- Nested structures

👉 You are **fully prepared** for Pandas, ML pipelines, and technical interviews.

This document is now a **complete data structures reference** for your journey.

