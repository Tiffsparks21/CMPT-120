print("Hello World")
print(12)
TB="Tiffany Betancourt"
print(TB)
print(TB)
x=10
print("my name is",TB,"and I am",x,"years old" )

x=1
y=2
if y>x:
    print (y)
else:
    print("is smaller than 3")

toCheck = 0
if toCheck > 1:
    print(toCheck)
elif toCheck == 0:
    print(toCheck, "is equal 0")
else:
    print(toCheck, "is smaller than 3")


#T = Tiffany
#if T == "tiffany":
 #   print ("wrong name")
#elif T == "Tiffany":
#    print( T, "is correct")
#else:
 #   print("ur not me")

F=5
S=6
if F==S:
    print("equal")
else:
    print("not equal")

var = 4
if var > 5:
    print("too big")
elif var > 0 and var < 5:
    print("Just right!")
else:
    print("too small!")

#age = input ("how old are you? ")
#age = int(age)
#      int("24")
##age=24
##age = 24
#if age >= 21: #or if int(age) >= 21:
   # print("You can drink!")
#else:
    #print ("it's illegal for you to drink :(")

##5 and take 2 sets of 5. 1 is left over
##moduals%= take out sets of two until you can't no more.

num1 = input("enter a number to check if its even or odd")
num1 = int(num1)
if num1 % 2 == 0:
    print("even number!")
else:
    print("odd number")