
def Sumall(no1):   
    sum =0
    for digit in str(no1):
        sum=sum+int(digit)
    return sum
    

def main():
    no=input("Enter the number: ")
    iret=Sumall(no)
    print("Sum  is: ",iret)



if __name__=="__main__":
    main()