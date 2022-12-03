### Part 1 ###
priorityValues = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

priorities=[]
uniqueItems=[]
rucksacks=[]

debug=False

#Get the file
if debug:
  with open("sample3.txt") as file:
    for line in file:
      rucksacks.append(line.strip()) 
  #print(rucksacks)
else:
  with open("day3.txt") as file:
    for line in file:
      rucksacks.append(line.strip()) 
  #print(rucksacks)

#Split each line in half
for sack in rucksacks:
  size = len(sack)
  #print(size)
  list1 = sack[:size//2]
  list2 = sack[size//2:]
  #print(list1)
  #print(list2)

  #Check if each character in the first half is in the second half
  found = False
  for item in list1:
    if found == False and item in list2:
      found=True
      uniqueItems.append(item)
      print(item)
      #Assign a priority number to it
      priority = priorityValues.index(item) + 1
      print(priority)
      priorities.append(priority)
  
#Sum the priorities
totalPriorities = sum(priorities)
print(f"The total is {totalPriorities}")

### Part 2 ###

priorities=[]
rucksacks=[]

#Get the file
if debug:
  with open("sample3.txt") as file:
    for line in file:
      rucksacks.append(line.strip()) 
  #print(rucksacks)
else:
  with open("day3.txt") as file:
    for line in file:
      rucksacks.append(line.strip()) 
  #print(rucksacks)

#Split into groups of 3
for i in range(0,len(rucksacks),3):
  found = False
  for character in rucksacks[i]:
    if found == False and character in rucksacks[i+1] and character in rucksacks[i+2]:
      found = True
      print(character)
      #Assign a priority number to it
      priority = priorityValues.index(character) + 1
      print(priority)
      priorities.append(priority)
      
#Sum the priorities
totalPriorities = sum(priorities)
print(f"The total is {totalPriorities}")
