### Part 1 ###
supplies = []
elfTotals=[]

with open("day1.txt") as file:
  for line in file:
    line = line.strip()
    if line.isdigit():
      supplies.append(int(line))
    else:  
      supplies.append(line)

highestAmount = 0
currentTotal = 0
for food in supplies:
  print(f"Food: {food}")
  if food == "":
    if currentTotal > highestAmount:
      highestAmount = currentTotal 
    elfTotals.append(currentTotal)
    currentTotal = 0
  else: currentTotal += food
  print(f"Current Total: {currentTotal}")
  print(f"Highest Amount: {highestAmount}")
  print()
  
### Part 2: sum the top 3 elfTotals ###
elfTotals = sorted(elfTotals)
print(f"The 3 highest totals are: {elfTotals[-3:]}")
print(f"Total for top 3: {sum(elfTotals[-3:])}")

  