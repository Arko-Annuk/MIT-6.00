#Problem Set 4
#Name: Arko Annuk
#Time: 6:45

#Problem 1

def nestEggFixed (salary, save, growthRate, years):
    F = []
    firstYear = salary*save*0.01
    F.append(firstYear)
    while len(F) <years:
        nextYear = F[-1]*(1+0.01*growthRate)+salary*save*0.01
        F.append(nextYear)
    print (F)

#Problem 2

def nestEggVariable(salary,save,growthRates):
#growthRates parameter needs to be defined as a list
    savingsRecord=[]
    firstYear = salary*save*0.01
    savingsRecord.append(firstYear)
    del growthRates[0]
    
    for x in growthRates:
        nextYear = savingsRecord[-1]*(1+0.01*x)+salary*save*0.01
        savingsRecord.append(nextYear)
    print (savingsRecord)

#Problem 3

def postRetirement(savings, growthRates, expenses):
    savingsRecord=[]
    firstYear = savings*(1+0.01*growthRates[0])-expenses
    savingsRecord.append(firstYear)
    del growthRates[0]

    for x in growthRates:
        nextYear = savingsRecord[-1]*(1+0.01*x)-expenses
        savingsRecord.append(nextYear)
    print (savingsRecord)

#Problem 4

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):\

    preSavingsRecord=[]
    preFirstYear = salary*save*0.01
    preSavingsRecord.append(preFirstYear)
    del preRetireGrowthRates[0]

    for x in preRetireGrowthRates:
        preNextYear = preSavingsRecord[-1]*(1+0.01*x)+salary*save*0.01
        preSavingsRecord.append(preNextYear)
    print (preSavingsRecord)
    
    savings = preSavingsRecord[-1]
    print (savings)

    expenses=1000
    postSavingsRecord=[]
    for expenses in range (salary):
        postFirstYear = savings*(1+0.01*postRetireGrowthRates[0])-expenses
        postSavingsRecord.append(postFirstYear)
        for x in postRetireGrowthRates[1:]:
            postNextYear = postSavingsRecord[-1]*(1+0.01*x)-expenses
            postSavingsRecord.append(postNextYear)
        if postSavingsRecord[-1]<=epsilon:
            print (expenses)
            break
        else:
            postSavingsRecord.clear()
            expenses=+1
            
