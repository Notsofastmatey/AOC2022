pairs=[]
counter1=0
counter2=0
debug=False

#Get the file
if debug:
  with open("sample4.txt") as file:
    for line in file:
      pairs.append(line.strip().split(",")) 
  print(pairs)
else:
  with open("day4.txt") as file:
    for line in file:
      pairs.append(line.strip().split(",")) 
  print(pairs)

for pair in pairs:
  print(pair)
  #Get the start of pair 0
  s0 = int(pair[0].split('-')[0])
  #Get the end of pair 0
  e0 = int(pair[0].split('-')[1])
  #Get the start of pair 1
  s1 = int(pair[1].split('-')[0])
  #Get the end of pair 1
  e1 = int(pair[1].split('-')[1])
  
  #Generate the lists and convert to sets
  pair[0]=set(list(range(s0,e0+1)))
  pair[1]=set(list(range(s1,e1+1)))
  print(pair)
  
  #Check for complete crossover (part 1)
  if pair[0].issubset(pair[1]) or pair[1].issubset(pair[0]):
    counter1+=1

  #Check for partial crossover (part 2)
  if len(pair[0].intersection(pair[1])) > 0:
      counter2+=1

  print(f"Counter 1: {counter1}")
  print(f"Counter 2: {counter2}")

print(f"Counter 1 final total: {counter1}")
print(f"Counter 2 final total: {counter2}")