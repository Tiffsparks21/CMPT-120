
def printHello():
    print("Hello")
    
def printName(x):
    print(x)

def addition(x, y):
    #add x and y together and return them
    return (x+y)

def smaller(i, j):
    if i < j:
        return i
    elif j < i:
        return j
    elif j % 2 == 0 and i % 2 == 0:
        return 0
    else:
        print ("This is wrong")

def main():
    printHello()
    #call the printHello function here
    printName("Tiffany")
    #call printName and give it the parameter of your name
    
    var1= 10
    var2= 20
    #What do we put in here to make it work?
    print(addition(var1,var2))
    
    num1 = int(input("Enter number 1"))
    num2 = int(input("Enter number 2"))
    #what go here?
    print(smaller(num1,num2))



main()
