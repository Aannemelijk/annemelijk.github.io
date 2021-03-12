'''
Script: Dice Roller
Developer: Ashton H
Date: 1/10/2020
'''

import random;  
count = 1;  

def welcMod():
    global count
    count += 1;
    print("Welcome to my dice roller!"
          + "\nFirst input how many dice you want to roll"
          + "\nThen how many sides the dice has.\n");

def promptMod():
    while True:
        try:
            numDice = int(input("How many dice: "));
            sideDice = int(input("How many sides: "));
            break
        except:
            print("Please enter a whole number.");
    return numDice, sideDice;

def arrayStorageMod():
    global diceRolls;
    diceRolls = [];

def rollMod(numDice, sideDice):
    for r in range(0,numDice):
        roll = random.randint(1,sideDice);
        diceRolls.append(roll)

def displayMod():
    for c in range(0, len(diceRolls) - 1):
        print(diceRolls[c], end = " + ");
    print(diceRolls[c + 1]);
    print("\n\nFor a total of " + str(sum(diceRolls)));

def returnMod():
    choice = input("\n\nDo you want to roll again? (Y or N) ");
    if choice.lower() == "y":
        print("\n\n");
        coreMod();
    elif choice.lower() == "n":
        input("\nThanks for rolling!\nMade by Ashton H.\n\n(Press the return key to exit)");
    else:
        for i in range(0,3):
            print("Invalid character, you have " + str(3 - i) + " tries left");
            choice = input("\nDo you want to roll again? (Y or N) ");
            if choice.lower() == "y":
                print("\n\n");
                coreMod();
            elif choice.lower() == "n":
                input("\nThanks for rolling!\nMade by Ashton H.\n\n(Press the return key to exit)");
        if i == 2:
            input("\nThanks for rolling!\nMade by Ashton H.\n\n(Press the return key to exit)");

def coreMod():
    if count == 1:
        welcMod();
        coreMod();
    else:
        numDice, sideDice = promptMod();
        arrayStorageMod();
        rollMod(numDice, sideDice);
        displayMod();
        returnMod();

coreMod();
