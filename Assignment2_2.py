
def Star(no):
    for i in range(0,no):
        for k in range (0,no):
            print("*",end=" ")
        print(" ")



def main():
    no=int(input("Enter the number: "))
    Star(no)



if __name__=="__main__":
    main()