def CheckPrime(no1):   
    for i in range (2,no1):
        if (no1%i)==0:
            return True
            break
            
    else:
        return  False