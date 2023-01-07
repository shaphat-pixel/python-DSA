# the elements in an array consume a memory space on our RAM.
# the big O of looking for an element in an array is O(1)
# there are static(have fixed size) and dynamic arrays(have unfixed sizes)
# python uses only dynamic arrays. java and c++ use both static and dynamic.
# you can have multiple data types in python arrays. but no in java and c++.

#EXERCISE 1
expenses = [2200, 2350, 2600, 2130, 2190]

#how much did I spend in february than january
ansA1 = expenses[1] - expenses[0]
#print(ansA1)

#total in first three months
ansA2 = expenses[0]+expenses[1]+expenses[2]
#print(ansA2)

#if i spent exactly 2000 in any month
#print(2000 in expenses)


#adding that of june
expenses.insert(5, 1980) 

#or
expenses.append(1980)

# updating after a refund
refund = expenses[3]-200
expenses[3] = refund
#print(expenses)


#EXERCISE 2
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

#length of the list
#print(len(heros))

#add 'black panther' at the end.
heros.append('black panther')

#removing black panther and adding it after hulk
heros.remove('black panther')

heros.insert(3, 'black panther')


#removing hulk and thor and replacing with doc. strange.
heros.remove('hulk')
heros.remove('thor')

heros.insert(1, 'doctor strange')

#sorting in alphabetical order
heros.sort()


#EXERCISE 3
