import string
import math
tabsize = 1500000


randnums = []
inp = open ("liczby.txt","r")
for line in inp.readlines():
        randnums.append(int(line))


table_chain_hash1 = [[] for _ in range(tabsize)]

table_chain_hash2 = [[] for _ in range(tabsize)]

table_linear_hash1 = [0] * tabsize

table_linear_hash2 = [0] * tabsize

def hashing_fun(x): return x%tabsize

def hashing_fun_2(x): 
	a = 0.000000000002
	return int(tabsize*((x*a)%1))

def insert(value,hash,table): 
	table[hash(value)].append(value)

def delete(value,hash,table): 
	table[hash(value)].remove(value)

def search(value,hash,table):
	print('liczba ', value, 'jest na pozycji: ', table[hash(value)].index(value)+1 , 'w kolumnie: ', hash(value)+1 )

def insert_linear(value,hash,table):
	index=hash(value) 
	if(table[index]==0):
		table[index]=value
	else:
		while True:
			if(index!=0):
				index-=1
			else:
				index = tabsize-1
			if(table[index]==0):
				table[index]=value
				break

def search_linear(value,hash,table):
	index=hash(value) 
	if(table[index]==value):
		print(value, 'znajduje sie w komurce:', index)
	else:
		while True:
			if(table[index]!=value):
				index-=1
			else:
				index = tabsize-1
			if(table[index]==value):
				print(value, 'znajduje sie w komurce:', index)
				break				

print('Trwa umieszczenie liczb do tablic \n')
		
#umieszczanie liczb do tabliczy 
for i in range(len(randnums)):
	insert(randnums[i],hashing_fun,table_chain_hash1)
	insert(randnums[i],hashing_fun_2,table_chain_hash2)
	insert_linear(randnums[i],hashing_fun,table_linear_hash1)
	insert_linear(randnums[i],hashing_fun,table_linear_hash2)
#umieszczanie liczb do tabliczy

print('Trwa obliczanie efektywnosci 1 funkcji haszujacej \n')

#maksymalna dlugosc listy
max = 0
listslen = 0
numoflists = 0
numofcollisions = 0
for j in range(tabsize):
	if(len(table_chain_hash1[j])>0):
		listslen += len(table_chain_hash1[j])
		numoflists+=1
		if(len(table_chain_hash1[j])>1):
			numofcollisions += len(table_chain_hash1[j])-1


	if(max<len(table_chain_hash1[j])):
		max=len(table_chain_hash1[j])
#maksymalna dlugosc listy
search(133034235868,hashing_fun,table_chain_hash1)

print('Maksymalna dlugosc listy przy haszowaniu 1 metoda:', max)
print("Srednia dlugosc listow przy haszowaniu 1 metoda: {0:.2f}".format(listslen/numoflists))
print('Ilosc kolizji: przy haszowaniu 1 metoda', numofcollisions)
print('Skutecznosc miesznia przy haszowaniu 1 metoda:',int((1-numofcollisions/numoflists)*100),'%\n')

print('Trwa obliczanie efektywnosci 2 funkcji haszujacej \n')

max = 0
listslen = 0
numoflists = 0
numofcollisions = 0
for j in range(tabsize):
	if(len(table_chain_hash2[j])>0):
		listslen += len(table_chain_hash2[j])
		numoflists+=1
		if(len(table_chain_hash2[j])>1):
			numofcollisions += len(table_chain_hash2[j])-1


	if(max<len(table_chain_hash2[j])):
		max=len(table_chain_hash2[j])

print('Maksymalna dlugosc listy przy haszowaniu 2 metoda:', max)
print("Srednia dlugosc listow przy haszowaniu 2 metoda: {0:.2f}".format(listslen/numoflists))
print('Ilosc kolizji: przy haszowaniu 2 metoda', numofcollisions)
print('Skutecznosc miesznia przy haszowaniu 2 metoda:',int((1-numofcollisions/numoflists)*100),'%')
