#A  X  Rock (1)
#B  Y  Paper (2)
#C  Z  Scissors (3)

# Win 6
# Draw 3
# Lose 0

### Part 1 ###
totalScore = 0
with open("day2.txt") as file:
  guide = [line.split() for line in file]
  
for game in guide:
  print(game)
  #Ties
  if game[0] == "A" and game[1] == "X":
     outcomeScore = 3 
  elif game[0] == "B" and game[1] == "Y":
    outcomeScore = 3
  elif game[0] == "C" and game[1] == "Z":
    outcomeScore = 3
  #Put all the player wins here
  elif game[0] == "A" and game[1] == "Y":
    outcomeScore = 6
  elif game[0] == "B" and game[1] == "Z":
    outcomeScore = 6
  elif game[0] == "C" and game[1] == "X":
    outcomeScore = 6
  #Add else for opponent wins
  else:
    outcomeScore = 0
  #Now allocate points for player choice
  if game[1] == "X":
    choiceScore = 1
  elif game[1] == "Y":
    choiceScore = 2
  else:
    choiceScore = 3
  roundScore = choiceScore + outcomeScore
  print(f"Choice Score {choiceScore}")
  print(f"Outcome Score {outcomeScore}")
  print(f"Round Score {roundScore}")
  totalScore = totalScore + roundScore
  print(f"Total score {totalScore}")

print(f"Total score {totalScore}")

### Part 2 ###
totalScore = 0
with open("day2.txt") as file:
  guide = [line.split() for line in file]
  
for game in guide:
  print(game)
  #Work out what the outcome needs to be
  if game[1] == "X":
    #I need to lose
    outcomeScore = 0
    #Now work out what the shape needs to be
    if game[0] == "A":
      #I need to play scissors
      shapeScore = 3
    elif game[0] == "B":
      #I need to play rock
      shapeScore = 1
    else:
      shapeScore = 2
  elif game[1] == "Y":
    #I need to draw
    outcomeScore = 3
     #Now work out what the shape needs to be
    if game[0] == "A":
      #I need to play rock
      shapeScore = 1
    elif game[0] == "B":
      #I need to play paper
      shapeScore = 2
    else:
      shapeScore = 3
  else:
    #I need to win
    outcomeScore = 6
     #Now work out what the shape needs to be
    if game[0] == "A":
      #I need to play paper
      shapeScore = 2
    elif game[0] == "B":
      #I need to play scissors
      shapeScore = 3
    else:
      shapeScore = 1
    

  roundScore = shapeScore + outcomeScore
  print(f"Shape Score {shapeScore}")
  print(f"Outcome Score {outcomeScore}")
  print(f"Round Score {roundScore}")
  totalScore = totalScore + roundScore
  print(f"Total score {totalScore}")

print(f"Total score at the end is: {totalScore}")