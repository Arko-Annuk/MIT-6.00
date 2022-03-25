# Problem Set 3
 # Name: Arko Annuk
 # Time: 4:30

import re

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key14 = 'zvd'

key1 = ('a')
key2 = ('atg')

#iterative approach to counting substrings

def countSubStringMatch(target,key):
    count = target.count(key)
    if key in target:
        print('found')
        print('The key count is:', count)
    else:
        print('not found')

#makes it so you can snipe the key placements in string

def subStringMatchExact(target,key):
    result = [_.start() for _ in re.finditer(key, target)] 
    print (str(result))

#derive predefined substrings straight from target

starts1 = [_.start() for _ in re.finditer(key1,target2)]
starts2 = [_.start() for _ in re.finditer(key2,target2)]


#length is the number of chars in firstMatch+1 
#mark firstMatch as key1, secondMatch as key 2

def constrainedMatchPair(firstMatch,secondMatch,length):
    n = [_.start() for _ in re.finditer(firstMatch,target2)]
    k = [_.start() for _ in re.finditer(secondMatch,target2)]
    m = (str(length))
    print (n)
    print (k)
    print (m)

    for x in k:
        for y in n:
            if x-y == 2:
                print (x)
                print (y)
            
#This compares the list values against eachother    

#I need to find all the values of "2", save them as correct value and print
##    for ans in [x-y for y in n for x in k]:
##        if (ans == 2):
##            print (k)
##            
##    test = [x-y for y in n for x in k]
##    print (test)
