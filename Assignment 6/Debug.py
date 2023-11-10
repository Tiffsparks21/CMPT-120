class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def getModel(self):
        return (self.model)
    #create your own function! what do you want it to do?
    
   
def main():
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog("Mellow", 9)
    print(dog1.name, dog1.age)
    
    #and what about a new employee
    newEmployee = Employee("Dave", 35, 120)
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name,newEmployee.department, newEmployee.idNumber)
    
    #now create and print out a cake you make
    cake1 = Cake("strawberry", "raspberry")
    print(cake1.frosting, cake1.flavor)

    cake2 = Cake("coco", "buttermilk")
    print(cake2.frosting, cake2.flavor)
    #and now create another cake and print it out
    
    
    
    #create a cat!
    cat1 = Cat("Mushi", 5, "long")
    #create another cat!
    cat2 = Cat("Max", 4, "short")
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    car1 = Car("Toyota", 2016, "red")
    print(car1.getModel())
    #Now print out the function you made for car :)

main()
