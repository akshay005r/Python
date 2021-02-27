
import MarvellousNum

def sum(brr):
    sum =0
    for i in range(len(brr)):
        sum=sum+brr[i]
    return sum

def main():
    arr=[]
    length=int(input("Enter the Length of your list: "))
    for i in range(length):
        element=int(input("Enter Element{}: ".format(i)))
        arr.append(element)
    print("Entered list of elements is: ",arr)
    
    brr=[]
    for i in range(len(arr)):
        check=MarvellousNum.CheckPrime(arr[i])

        if check==False:
            brr.append(arr[i])
    print("list of Prime Numbers is ",brr)    
    sumofprime=sum(brr)
    print("Sum of all prime numbers is: ",sumofprime)

if __name__== "__main__":
    main()