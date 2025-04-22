'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
a = 200
b = 33
c = 500
if a > b or a > c:   #and or not
   print("At least one of the conditionns is Ture)


x = 41 

if x >10:
    print("above ten,")
    if x >20:
      print("and also above 20!")
  
day =int(input("please num 1-7:"))
match day:
    case 1 | 2 | 3 | 4 | 5 :
      print("today is a weekday")
    case 6 | 7:
      print ("I love weekends!")
      

fruits = ["apple", "banana", "cherry"]

for fruit in  fruits:
    print(fruit)
prtint("-----------------------")
for i in range(0,3):
    print(fruit[i])
