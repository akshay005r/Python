
def Add(arr):
    sum = 0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum


def main():
    arr=[]
    length=int(input("Enter the Length of your list: "))
    for i in range(length):
        element=int(input("Enter Element{}: ".format(i)))
        arr.append(element)
    print("Entered list of elements is: ",arr)
    
    sumofelements=Add(arr)
    print("Sum of all elements is: ",sumofelements)




if __name__== "__main__":
    main()