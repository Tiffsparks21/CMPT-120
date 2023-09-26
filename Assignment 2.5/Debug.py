
def main():

    #that's not right... how can we make sure it also includes equals 5?
    temp = 5
    if temp >= 5:
        print("temp is greater than or equal to 5")
        
    
    #enter your name here
    name = "Tiffany"
    '''in this if/elif/else, add 4 mispellings of your name for if/elif comparisons, and then have your last elif be elif name = "your properly spelled name" '''
    if name == "tiffany":
        print("That's not right!")
    elif name == "TIFFANY":
        print("That's not right!")
    else:
        print(name,"is a lovely name <3 :D")
    #etc etc, the else can be whatever you want
    
    
    #we're gonna check if a user input number is even
    #pick any number
    even = input("Enter a number to find out if its even or odd")
    even = int(even)
    #what do we replace the question marks with?
    if even % 2 == 0:
        #what would be appropriate in these print statements?
        print("  Yay your number "+ str(even) +" is even")
    else:
        print("  Your number " + str(even) + " is odd")

  
    #i'm trying to do math with the numbers 2 and 4, but it's getting 3 and 5... why?
    numbers = [1,2,3,4,5]
    print(numbers[2]-1)
    print(numbers[4]-1)
    print(numbers[4] / numbers[2])
    print(numbers[4] * numbers[2])
    
    #again, why is it getting 7 and 20, I wanted 3 and 29!
    numbers2 = [465,3,30,7,29,20,82,13,5]
    print(numbers2[3])
    print(numbers2[5])
    
    #Here's a fun one: This is a list of everyone's name. Find where yours is and print the index of your name
    students = ["Tobi", "Brad", "Tiff", "Oscar", "Tommy", "Kyra", "Matt C", "Morgan", "Haley", "Matt F", "Sydney",
                "Pedro", "Nathan", "Bryce", "Chris", "Iram", "Pat", "Maddie", "Daniel", "Tomas", "Gabriella", "Ben",
                "Lucian", "Dean", "Jack", "Natalie", "Athina"]
    print(students[3])
main()
    
    

    
