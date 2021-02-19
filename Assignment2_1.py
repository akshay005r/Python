import Arithmetic

def main():
    no1=int(input("Enter First Number: "))
    no2=int(input("Enter First Number: "))
    
    isub=Arithmetic.Add(no1,no2)
    print("Addition of number is ",isub)
    
    isub=Arithmetic.Subtract(no1,no2)
    print("Substraction of number is ",isub)
    
    imul=Arithmetic.multiplay(no1,no2)
    print("Multiplication of number is ",imul)

    idiv=Arithmetic.divide(no1,no2)
    print("Division of number is ",idiv)
    
if __name__=="__main__":
    main()