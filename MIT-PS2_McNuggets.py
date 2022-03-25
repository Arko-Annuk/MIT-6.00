# Problem Set 2
 # Name: Arko Annuk
 # Time: 6:30 

#exhaustive search to find the largest number of McNuggets that cannot be bought in exact quantity

n = 0
buyable_Amount=[]
while n <= 50: #Because >50 nuggets already proven to have infinite answers
    n += 1

    def is_buyable(n):
        ''' return whether amount n McNuggets is buyable at McDonalds (using 6, 9 and 20 packs) '''
        if n == 0:
            return True
        for i in (6, 9, 20):
            if n >= i and is_buyable(n - i):
                return True
        return False
    
    if is_buyable(n):
        buyable_Amount.append(n)
    else: buyable_Amount.clear()
if len(buyable_Amount)>6:
    print ((buyable_Amount[0])-1)


