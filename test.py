import string
import math
tabsize = 15

randnums = []
inp = open ("liczby.txt","r")
for line in inp.readlines():
        randnums.append(int(line))


table_linkedlist = [[] for _ in range(tabsize)]

table_linear = [0] * tabsize

def hashing_fun(x): return x%tabsize

def hashing_fun_2(x): 
	n = 1000000
	a = (sqrt(5)-1)/2
	return int(n*fmod(x*a,1))

def insert(value): 
	table_linkedlist[hashing_fun(value)].append(value)

def delete(value): 
	table_linkedlist[hashing_fun(value)].remove(value)

def search(value):
	print('liczba ', value, 'jest na pozycji: ', table_linkedlist[hashing_fun(value)].index(value)+1 , 'w kolumnie: ', hashing_fun(value)+1 )


#umieszczanie liczb do tabliczy 
for i in range(len(randnums)):
	insert(randnums[i])
#umieszczanie liczb do tabliczy

#maksymalna dlugosc listy
max = 0
listslen = 0
numoflists = 0
numofcollisions = 0
for j in range(tabsize):
	if(len(table_linkedlist[j])>0):
		listslen += len(table_linkedlist[j])
		numoflists+=1
		if(len(table_linkedlist[j])>1):
			numofcollisions += len(table_linkedlist[j])-1


	if(max<len(table_linkedlist[j])):
		max=len(table_linkedlist[j])
#maksymalna dlugosc listy


#print('Srednia dlugosc listow:', float(listslen/numoflists))
#print('Ilosc kolizji:', numofcollisions)
#print('Skutecznosc miesznia:',int((1-numofcollisions/numoflists)*100),'%')
def insert_linear(value):
	index=hashing_fun(value) 
	if(table_linear[index]==0):
		table_linear[index]=value
	else:
		while True:
			if(index!=0):
				index-=1
			else:
				index = tabsize-1
			if(table_linear[index]==0):
				table_linear[index]=value
				break


insert_linear(123456)
insert_linear(123457)
insert_linear(123455)
insert_linear(123454)
insert_linear(123453)
insert_linear(123452)
insert_linear(123451)
insert_linear(123450)
insert_linear(123450)
insert_linear(123450)
insert_linear(123451)
print(table_linear)