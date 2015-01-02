##1. Write a function that accepts any number of arguments and prints out the number of arguments it has been passed.

def numberarguments(*arg):
	count=0
	if arg> 5:
		count+=1
    print ('The function pass', len(arg), 'argument:', arg)
    

#numberarguments(1,2,'a',5,6)
    
##2. Write a function that accepts any number of integer arguments and returns the sum of its arguments.

def sumarguments(*arg):
    a= sum(arg)
    return a
##3. What does this statement do:

people = { ('Traiba', 'Susi'): 'Female', ('Gobbi', 'Paolo'): 'Male', ('Tasta', 'Susan'):  'Female', ('Popi', 'Pepe'): 'Male'
    }

for last, first in people:
    print(last, first, people[last, first])

##4. Write a function, sort by length(words), which accepts a list of words and returns a list sorted by the length of the words in the list.
def sortword(a):
    if len(a) <= 1: return a
    pivot = a.pop()
    before = [x for x in a if x >= pivot]
    after = [x for x in a if x < pivot]
    return sortword(before) + [pivot] + sortword(after)
    
sortword(['papa', 'irene', 'duddiid', 'babdbage'])   

##5
def divrem(num, den):
    return (int(num/den), num % den)

##6. Lookup the definition of the zip() operation in function. Given two sequences s1 == (1,2, 3), and s2 == (’a’, ’b, ’c’), what is the result of zip(s1, s2)?

s1=(1,2,3)
s2= ('a', 'b', 'c')
a= list(zip(s1,s2)) #[(1, 'a'), (2, 'b'), (3, 'c')]

##7. Use the zip operation shown in the previous section to check if, given two sequences t1 and t2, there is an index i such that t1[i] == t2[i].
t1= (1,3,4,5)
t2= (1,4,5,3)
b = [ x== y for x, y in zip(t1, t2)]

def compare(t1,t2):
    equal=()
    for x, y in zip(t1,t2):
        if x==y:
            equal+=(x,y)
    return equal
    
