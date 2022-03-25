# Problem Set 1
# Name: Arko Annuk
# Time: 2:30



primeList = []

z = int(input('Enter up to which number to generate primes '))

for x in range (2, z + 1):
    isPrime = True
    for y in range (2, x):
        if x%y==0:
            isPrime = False
            break
    if isPrime:
        primeList.append(x)
        
print (('The program generated following instances of primes:'), len(primeList))

theTotal = sum(primeList)
theRatio = (theTotal/z)
print (('The ratio between theTotal & Z:'), (theRatio))
print ('The sum of primes in a list is: ', (theTotal))
nrPrime = int(input('Enter the number of prime you wish to print '))        
print (primeList[nrPrime-1])


