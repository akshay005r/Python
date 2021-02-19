
def Star(no):
    no=no+1
    for i in range(1,no,1):
        for k in range (1,no,1):
            print(k,end="  ")
        print(" ")



def main():
    no=int(input("Enter the number: "))
    Star(no)



if __name__=="__main__":
    main()