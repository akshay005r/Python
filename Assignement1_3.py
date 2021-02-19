def Add(no1,no2) :   
    return no1+no2
   

def main():
    no1=int(input("Enter the Number1: "))
    no2=int(input("Enter the Number2: "))
    iret=Add(no1,no2)
    print("The sum of two numbres {} & {} is {}".format(no1,no2,iret))

if __name__=="__main__":
    main()