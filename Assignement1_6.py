def Number(no1) :   
    if no1 >0:
        return True
    if no1==0:
        return False
    else:
        return "N"
    
   

def main():
    no1=float(input("Enter the Number1: "))
    ret=Number(no1)
    if ret==True:
        print("Positive Number")
    if ret==False:
        print("Zero")
    if ret == "N":
        print("Negative Number")


if __name__=="__main__":
    main()