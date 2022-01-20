import random

print("---------------WELCOME TO DICE ROLLING SIMULATOR---------------")
while True:
    output = random.randint(1, 6)
    print("Dice rolled: ")
    print(output)
    print("Do you want to roll again? (Y/N)\n")
    ans = input()
    if ans == 'n' or ans == 'N':
        break
print("Thanks for visiting the simulator.\n")
