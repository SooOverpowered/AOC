alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def part1(data):
  rucksacks = data.split('\n')
  result=0
  for sack in rucksacks:
    cat1= set([i for i in sack[0:len(sack)//2]])
    cat2= set([i for i in sack[len(sack)//2:]])
    common=list(cat1.intersection(cat2))
    result+=alphabet.index(common[0])+1
  return result

def part2(data):
  elves = data.split('\n')
  result=0
  for i in range(0,len(elves),3):
    elf1=set(j for j in elves[i])
    elf2=set(j for j in elves[i+1])
    elf3=set(j for j in elves[i+2])
    common = list(elf1.intersection(elf2,elf3))
    result+=alphabet.index(common[0])+1
  return result