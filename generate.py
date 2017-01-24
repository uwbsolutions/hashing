from random import randint
numofnums = 1000000
randnums=[randint(100000000000,999999999999) for _ in range(numofnums)]
f = open ('liczby.txt','w')
for item in randnums:
  f.write("%s\n" % item)