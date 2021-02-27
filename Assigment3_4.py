def main():
    arr=[]
    length=int(input("Enter the Length of your list: "))
    for i in range(length):
        element=int(input("Enter Element{}: ".format(i)))
        arr.append(element)
    print("Entered list of elements is: ",arr)
    
    find=int(input("Enter the element to find : "))
    
    
    frequency = arr.count(find)
    print("frequency of {} in list is {} ".format(find,frequency))



if __name__== "__main__":
    main()