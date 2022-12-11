monkeys=[
  [91, 66],
  [78, 97, 59],
  [57, 59, 97, 84, 72, 83, 56, 76],
  [81, 78, 70, 58, 84],
  [60],
  [57, 69, 63, 75, 62, 77, 72],
  [73, 66, 86, 79, 98, 87],
  [95, 89, 63, 67]
]

monkeyBusiness=[0,0,0,0,0,0,0,0]

for round in range(300):
  for i, monkey in enumerate(monkeys):
    #print(f"The current monkey is {i}")
    while len(monkeys[i])>0:
      for item in monkey:
        monkeyBusiness[i]+=1
        temp = item
        #Monkey 0
        if i==0:
          item = item * 13
          #item = item // 3
          if item % 19 == 0:
            monkeys[6].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[2].append(item)
            monkeys[i].remove(temp)
        #Monkey 1
        elif i==1:
          item = item + 7
          #item = item // 3
          if item % 5 == 0:
            monkeys[0].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[3].append(item)
            monkeys[i].remove(temp)
        #Monkey 2
        elif i==2:
          item = item + 6
          #item = item // 3
          if item % 11 == 0:
            monkeys[5].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[7].append(item)
            monkeys[i].remove(temp)
        #Monkey 3
        elif i==3:
          item = item + 5
          #item = item // 3
          if item % 17 == 0:
            monkeys[6].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[0].append(item)
            monkeys[i].remove(temp)
        #Monkey 4
        elif i==4:
          item = item + 8
          #item = item // 3
          if item % 7 == 0:
            monkeys[1].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[3].append(item)
            monkeys[i].remove(temp)
        #Monkey 5
        elif i==5:
          item = item * 5
          #item = item // 3
          if item % 13 == 0:
            monkeys[7].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[4].append(item)
            monkeys[i].remove(temp)
        #Monkey 6
        elif i==6:
          item = item *item
          #item = item // 3
          if item % 3 == 0:
            monkeys[5].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[2].append(item)
            monkeys[i].remove(temp)
        #Monkey 7
        elif i==7:
          item = item + 2
          #item = item // 3
          if item % 2 == 0:
            monkeys[1].append(item)
            monkeys[i].remove(temp)
          else:
            monkeys[4].append(item)
            monkeys[i].remove(temp)
      
      #print(f"Round: {round+1}: {monkeys}")
      #print(monkeyBusiness)
print(sorted(monkeyBusiness, reverse=True)[0])
print(sorted(monkeyBusiness, reverse=True)[1])