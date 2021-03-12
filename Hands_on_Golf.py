"""
Script: Hands on Golf
Developer: Ashton Hash
Date: 12/18/2020
Purpose: To make a golfing game
"""
import random;  #This creates the illusion of random

def introMod(): #This module introduces the players to the game.
  print("""  Welcome to Golfing Crazy!
Here the rules are simple;
Put your names down and the lowest score wins!""");
  pName1 = input("To start us off, who is:\nPLAYER ONE: ");
  pName2 = input("PLAYER TWO: ");
  return pName1, pName2;

def arrayMod(): #This module stores my arrays
  global pSwings1;
  global pSwings2;
  pSwings1 = [];
  pSwings2 = [];

def gameMod():  #This module decides how each round should go
  for round in range(0,18):
    pSwings1.append(random.randint(1,4));
    pSwings2.append(random.randint(1,4));

def scoreMod(): #This module simplifies the scores
  pScore1 = sum(pSwings1);
  pScore2 = sum(pSwings2);
  return pScore1, pScore2;

def calcMod(pScore1, pScore2): #This module decides who wins
  if pScore1 < pScore2:
    winner = 1;
    margin = pScore2 - pScore1;
  elif pScore1 > pScore2:
    winner = 2;
    margin = pScore1 - pScore2;
  else:
    winner = 0;
    margin = pScore2 - pScore1;
  return winner, margin;

def outputMod(winner, margin, pName1, pName2, pScore1, pScore2): #This module says everything to the players
  if winner == 1:
    if margin == 1:
      print("\nPlayer " + str(pName1).upper() + " wins by " + str(margin) + " point!");
    else:
      print("\nPlayer " + str(pName1).upper() + " wins by " + str(margin) + " points!");
  elif winner == 2:
    if margin == 1:
      print("\nPlayer " + str(pName2).upper() + " wins by " + str(margin) + " point!");
    else:
      print("\nPlayer " + str(pName2).upper() + " wins by " + str(margin) + " points!");
  else:
    print("\nNeither player wins, the game was a draw!");
  print("\nHere are the final scores:");
  for hole in range(0,20):
    if hole == 0:
      print("Hole number, " + str(pName1).upper() + "'s score, " + str(pName2).upper() + "'s score")
    elif hole > 0 and hole < 10:
      print("Hole 0" + str(hole) + ": " + str(pSwings1[int(hole) - 1]) + ", " + str(pSwings2[int(hole) - 1]));
    elif hole >= 10 and hole < 19:
      print("Hole " + str(hole) + ": " + str(pSwings1[int(hole) - 1]) + ", " + str(pSwings2[int(hole) - 1]));
    else:
      print("Final totals: " + str(pName1).upper() + " swung " + str(pScore1) + " times, and " + str(pName2).upper() + " swung " + str(pScore2) + " times");

def coreMod(): #This module carries every other module as the hub
  pName1, pName2 = introMod();
  arrayMod();
  gameMod();
  pScore1, pScore2 = scoreMod();
  winner, margin = calcMod(pScore1, pScore2);
  outputMod(winner, margin, pName1, pName2, pScore1, pScore2);

coreMod(); #This summons the main module
