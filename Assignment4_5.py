import functools

def main():
    arr=[]
    length=int(input("Enter the length of list: "))
    for i in range(length):
        element=int(input("Enter the element of list: "))
        arr.append(element)
    print("Enter list is: ",arr)
    
    newdata = list(filter(lambda no1 :False if (no1%i)==0 else True,arr))      
    print("After Filter Data is ",newdata)
    
    newdata1 = list(map(lambda no : (no*2),newdata))       
    print("After Map Data is ",newdata1)
    
    newdata2 = functools.reduce(lambda no1,no2 :no1 if no1>no1 else no2 ,newdata1)      
    print("After Reduce Data is ",newdata2) 
    
    
if __name__=="__main__":
    main()