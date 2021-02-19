def star(no1) :   
    for i in range(no1):
        print("*",end=" ")
    
   

def main():
    no1=int(input("Enter The Number: "))
    star(no1)
    

if __name__=="__main__":
    main()