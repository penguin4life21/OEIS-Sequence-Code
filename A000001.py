import math as m

n = 11



def factors(number):
    output = []
    for i in range(1 , number + 1):
        if number % i == 0:
            output.append(i)
    return(output)

def isprime(number):
    factorslist = factors(number)
    if (len(factorslist) == 2):
        if factorslist[0] == 1 and factorslist[1] == number:
            return(True)
        else:
            return(False)
    else:
        return(False)

def A000001(num):
    if (num == 0):
        return(0)
    elif (num == 1):
        return(1)
    elif (num == 16):
        return(14)
    elif (isprime(num) == True):
        return(1)
    elif (m.sqrt(num) == round(m.sqrt(num))):
        if isprime(round(m.sqrt(num))):
            return(2)
    elif (num ** (1/3) == round(num ** (1/3))):
        if (isprime(round(num ** (1/3)))):
            return(5)

for i in range(1,15):
    print(str(i) + "____" + str(A000001(i)))


    