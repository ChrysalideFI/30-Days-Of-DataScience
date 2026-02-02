'''If-Else Statements
1. Write a program that checks if a number is positive, negative, or zero.
2. Create a grade classifier using the if-elif-else structure.

Loops
3. Write a program that prints all even numbers from 1 to 50 using a for loop.
4. Create a program that sums the numbers from 1 to 100 using a while loop.
5. Use break and continue in a loop to demonstrate their functionality.'''

# 1. Say if the number is positive, negative or equal to zero

number = int(input("Write your number: "))
def sign_number(number) : 
  if number > 0 :
    sign_number = "This number is positive"
  elif number < 0 :
    sign_number = "This number is negative"
  else : 
    sign_number = "This number is equal to zero"
  return sign_number
print(sign_number(number))

# 2. Grade classifier
grades = [16, 20, 4, 6, 14, 11, 7, 19, 17, 0]
def grade_classifier(grades):
  grades_result=[]
  for grade in grades : 
    if grade >= 16 : # on aurait pu utiliser un match case
      result="A"
    elif (grade >= 12 and grade < 16) : 
      result="B"
    elif (grade >= 8 and grade < 12) : 
      result="C"
    elif (grade >= 4 and grade < 8) : 
      result="D"
    elif (grade > 0 and grade < 4) : 
      result="E"
    else: 
      result="F"
    grades_result.append(result)
  return grades_result
print (grade_classifier(grades))

# 3. prints all even numbers from 1 to 50 using a for loop. 
for i in range (1, 50): 
  if (i%2==0) :
    print(i)
  
# Better version : 

for i in range (2, 50, 2): 
  print(i)


# 4. Sums the numbers from 1 to 100 using a while loop
number = 1
sum=0
while number != 101 : 
  sum+=number
  number+=1
print(sum)


# 5. Use break and continue
numbers = [3, -1, 7, 12, -5, 42, 9, 15] 

for n in numbers: 
  if n < 0: 
    continue # on ignore les nombres négatifs 
  print("Nombre analysé :", n) 
  if n == 42: 
    print("Nombre spécial trouvé ! On arrête la recherche.") 
    break # on arrête complètement la boucle

