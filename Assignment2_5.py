def Prime(no1):   
    sum=0
    for i in range (2,no1):
        if (no1%i)==0:
            return True , i
            break
            
    else:
        return  False,i

def main():
    no=int(input("Enter the number: "))
    bret,iret=Prime(no)
    if bret == True:
        print("The number {} is not a Prime as it is Divisible by {}".format(no,iret))
    else:
        print("The number {} is Prime".format(no))



if __name__=="__main__":
    main()