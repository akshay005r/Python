def Sumall(no1):   
    sum=0
    for i in range (1,no1,1):
        if no1%i==0:
            sum = sum+i
    return sum

def main():
    no=int(input("Enter the number: "))
    iret=Sumall(no)
    print("Sum  is: ",iret)



if __name__=="__main__":
    main()