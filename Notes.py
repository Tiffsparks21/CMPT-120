class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.length

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


def main():
    square1 = Square(2)
    print(square1.perimeter())


main()

# name="Tiffany"
# for x in range(5):
#     print(name)
#
# print("  ")
# name="Kate"
# animals= ["dog","cat","horse"]
# for x in animals:
#     print (name)
# print("")
# #loops going for the amount of letters in the name
# for x in "Marist":
#     print (x)
# print("  ")
#
# name= "Alex"
# for x in name:
#     print(x)
#
# name= ["T","i","Ff","F","A","N","Y"]
# for x in name:
#     print(x)
#
# i=0
# while i<6:
#     print (i)
#     i=i+1#if I don't have this it will cause an infinite loop
#
# c=0
# while c<= 10:
#     print(c)
#     c=c+1
# # != not equal
# # <= less than or equal
# # >= more than or not equal
# # == equals
# # = assign to
# P = "Nick"
# x= 0
# while x < 5:
#     print(P)
#     x = x + 1
