def Display(no1) :   
    for i in range(no1,0,-1):
        print(i,end="  ")
   

def main():
    no1=int(input("Enter the Number1: "))
    Display(no1)


if __name__=="__main__":
    main()