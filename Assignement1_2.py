def ChkNum(no1) :   
    if no1%2==0:
        return True
    else:
        return False
   

def main():
    no1=int(input("Enter the Number: "))
    bret=ChkNum(no1)
        
    if bret==True:
        print("Even Number")
    else:
         print("Odd Number")

if __name__=="__main__":
    main()