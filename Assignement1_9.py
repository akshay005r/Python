def Even(no1) :
    count=1
    flag=0
    while True:
        if flag ==no1:
            break
        if count % 2 ==0:
            print(count, end=" ")
            flag = flag + 1
        count = count + 1
        
    
   

def main():
    no1=int(input("Enter The Number: "))
    Even(no1)
    

if __name__=="__main__":
    main()