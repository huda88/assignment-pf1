word= 'abcdefghijklmnopqrstuvwxyz'

# print letter in every line
def f1 (word):
    for i in word:
        print (i)

#print letter in every line begin with the end 
def f2 (word):
    for i in range(len(word)-1,-1,-1):
        print (word[i])

#print a word with index
def f3b(word):
    print (word[:])

#
def f4(word):
    for i in word:
       print (i + " ",end='')

#
def f5 (word):
    for i in range(len(word)-1,-1,-1):
        print (word[i] + ",", end='')

#
def f6 (word):
    print(word[len(word)::-1])
    
    
#print reverse string using loop
def f7 (word):
    for i in range(len(word)-1,-1,-1):
        print (word[i],end='')

#most frequent character 
def f8(word):
    max_letter= []
    max = 0
    word.casefold()
    for c in word:
        if c is not " ":
            if c in max_letter:
                max_letter= max_letter
            elif word.count(c)== max:
                max_letter.append(c)
                max = word.count(c)
            elif word.count(c)> max:
                max_letter=[]
                max_letter.append(c)
                max = word.count(c)
    print ('The most frequent letter in this word:', max_letter)

def f9(word):
    word= input('Write a little sentence:')
    max_letter= []
    max = 0
    word.casefold()
    for c in word:
        if c is not " ":
            if c in max_letter:
                max_letter= max_letter
            elif word.count(c)== max:
                max_letter.append(c)
                max = word.count(c)
            elif word.count(c)> max:
                max_letter=[]
                max_letter.append(c)
                max = word.count(c)
    print ('The most frequent letter in this word:', max_letter)

def f10(word):
    word.casefold()
    v= ''
    word= input('Write a little sentence:')
    char= input('Chose a character:')
    if char in word:
        v= True
    else:
        v= False
    print ('This character is in the string. This is: ', v)

def f11(word):
    print (word[::3])

def f12():
    word= input('Write a little sentence:')
    U= word.upper()
    print (U)

def f13():
    word= input('Write a little sentence:')
    l= word.lower()
    print (l)
    
def f14 ():
    message = input('Write a little sentence:')
    newstring = ""
    for char in message:
        if char.isupper():
            newstring += char.lower()
        else:
            newstring += char.upper()
    print (newstring)

def f15(num):
    final=''
    message = input('Write a little sentence:')
    final += message[(len(message)-num):] + message[:(len(message)-num)]
    return final
    print ('This is the result:', final)
                     

f6('Ciaocomestai')
        
        
