
def main():
    arr=[]
    length=int(input("Enter the Length of your list: "))
    for i in range(length):
        element=int(input("Enter Element{}: ".format(i)))
        arr.append(element)
    print("Entered list of elements is: ",arr)
    
    minof = min(arr)
    print("Min of all elements is: ",minof)




if __name__== "__main__":
    main()