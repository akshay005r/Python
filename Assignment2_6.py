def Star(no):
    for i in range(no,0,-1):
        for k in range (i,0,-1):
            print("*",end=" ")
        print(" ")



def main():
    no=int(input("Enter the number: "))
    Star(no)



if __name__=="__main__":
    main()