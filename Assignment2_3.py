
def factor(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact
            



def main():
    no=int(input("Enter the number: "))
    iret=factor(no)
    print("Factorial is: ",iret)



if __name__=="__main__":
    main()