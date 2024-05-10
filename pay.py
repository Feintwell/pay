def main ():
    name = getname ()
    hourlywage = gethourlywage ()
    totalhours = gettotalhours ()
    overtimehours = calovertimehours (totalhours)
    overtimepay = calovertimepay (overtimehours, hourlywage)
    weeklypay = calweeklypay (hourlywage, overtimepay)
    deduct = caldeduct (weeklypay)
    after = calweeklydeduct (weeklypay, deduct)
    contributed = calcontri (after)
    total = caltotalcon (after, contributed)

    displayname (name)
    displaydeduct (deduct)
    displaycontribution (contributed)
    displayweeklypay (total)


#get the name
def getname ():
    name = input("Please enter your name: ")
    return name 

#get the hourly wage
def gethourlywage ():
    hourlywage = int(input("Please enter your hourly wage: "))
    return hourlywage

#get the total hours
def gettotalhours ():
    totalhours = int(input("Please enter your total hours: "))
    return totalhours

#Calculate the overtime hours
def calovertimehours (totalhours):
    if totalhours >= 40:
        overtimehours = totalhours - 40
    else:
        overtimehours = 0
    return overtimehours

#Calculate overtime pay
def calovertimepay (overtimehours, hourlywage) :
    credit = hourlywage * 1.5
    overtimepay = overtimehours * credit
    return overtimepay

#Calculate weekly pay
def calweeklypay (hourlywage, overtimepay) :
    credit = 40 + overtimepay
    weeklypay = hourlywage * credit
    return weeklypay

'''
#Calculate deductions
def caldeduct (weeklypay) :
    deduct = weeklypay * (5/100)
    return deduct

#Calculate deductions
def caldeducti (after) :
    afterde = after * (10/100)
    return afterde

'''


#Calculate deductions
def caldeduct (weeklypay) :
    deduct = weeklypay * (15/100)
    return deduct

#Calculate weekly deduction
def calweeklydeduct (weeklypay, deduct) :
    after = weeklypay - deduct
    return after

# Calculate he contribution'
def calcontri (after) :
    contributed = after * (10/100)
    return contributed

def caltotalcon (after, contributed) :
    total = after + contributed
    return total

#output name
def displayname (name) :
    print(f"Hello {name}")
    
#output deduction
def displaydeduct (deduct):
    print (f"Your total deduction is ${deduct}")

#output contribution
def displaycontribution (contributed) :
    print (f"The employer contribution is ${contributed}")

#output weekly pay
def displayweeklypay (total) :
    print (f"Your total weekly pay is ${total}")


main ()
