#instructions: Something about these if statements aren't giving the desired effect. Look at them and see how to fix them. (Run them yourself and see what the output is!)
#also, we have some input practice!

def main():
    
    #this is a nice solid working one!
    name = input("your name is? ")
    print("Hello, ", name)

    #this isn't printing anything :( so sad. what's wrong with her? Why she not printing out?
    color = input("what's your favorite color? ")
    print(color," is a cool color :D !")
    
    #I thought i did this right :( can you fix it for me?
    age = input("how old are you? ")
    age = int(age)
    print("You are " + str(age) + " years old")
	
    #Start with this one! We have a compilation error :(
    #Side note: you can put these statements in parentheses or not. it's up to you.
    if (5 > 3):
        print("5 is greater than 3")
    else:
        print("Wrong")
    
    #There are multiple correct answers and adjustments to this one 
    Five = 5
    if Five > 5:
        print("Five is greater than 5")
    elif Five == 5:
        print("Five is equal to 5")
    else:
        print("Five is less than 5")

    #more multiple correct answers. Similar to the first. Adjust as perceived 
    toCheck = 4
    if toCheck > 5:
        print(toCheck, "is greater than 5.")
    elif toCheck > 3:
	    print(toCheck)
    else:
        print(toCheck, "is 3")

    #Is it really printing the BEST option though? Rearrange these as you see fit
    toCheck = 5
    if toCheck == 5:
        print("toCheck is 5")
    elif toCheck > 7:
        print("toCheck is greater than 7")
    elif toCheck < 6:
        print("toCheck is less than 6")
    else:
        print("toCheck is invalid")
    
    
    
    
main()
