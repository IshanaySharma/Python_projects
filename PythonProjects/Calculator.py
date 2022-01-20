import math

def options(i):
 switcher={
     1: x+y,
     2: x-y,
     3: x*y,
     4: x/y,
     5: x**y,
     6: math.sqrt(x),
 }
 return switcher.get(i,"invalid entry")

if __name__ == '__main__':
 print("-------CALCULATOR-------")
x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))

i = int(input("Choose your option\n 1:ADDITION\n 2:SUBTRACTION\n 3:MULTIPLICATION\n 4:DIVISION\n 5:EXPONENT\n 6:SQUARE ROOT\n"))
print("Your answer is:")
print(options(i))



