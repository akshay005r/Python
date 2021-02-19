def Div5(no1) :   
    if no1%5==0:
        return True
    else:
        return False
    
   

def main():
    no1=float(input("Enter the Number1: "))
    ret=Div5(no1)
    if ret==True:
        print("True")
    if ret==False:
        print("False")
    

if __name__=="__main__":
    main()