

def main():
    arr=[]
    length=int(input("Enter the Length of your list: "))
    for i in range(length):
        element=int(input("Enter Element{}: ".format(i)))
        arr.append(element)
    print("Entered list of elements is: ",arr)
    
    maxof = max(arr)
    print("Max of all elements is: ",maxof)




if __name__== "__main__":
    main()