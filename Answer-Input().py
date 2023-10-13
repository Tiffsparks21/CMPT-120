def main():
    Path= input("You're in the woods and you need to get out and survive. Choose a road infront of you: left or right or backwards ")

    if Path == "right":
        Path = input("You found a pond. Do you drink it? (yes/no)")
        if Path == "yes":
            print ("You drank fish pee congratulations :D, WHICH was poisonous. You DIED")
        elif Path == "no":
            print ("The pond looks sus anyway. You kept walking forward until you made it out of the woods")
        else:
            print("Wrong answer. With zero time left an eagle attacked you thinking you're a little bitch. You died")

    elif Path == "left":
        Path= input("You found a bear in your path and you tried to out run it but you tripped. Do you defend yourself? (yes/no) ")
        if Path == "yes":
            print ("You got a stick which did nothing. You died") 
        elif Path == "no":
            print ("You crawled into a hole near by and escaped from the bear. You waited until there was no noise and walked safely leaving the woods")
        else:
            print("Wrong answer. With zero time left an eagle attacked you thinking you're a little bitch. You died")

    elif Path == "backwards":
        Path = input("You hit a tree, Now your nose is bleeding. Without realising you stepped in a trap and a rope pulled on your leg and hung you upside down. After a few hours, a teenage boy found you in his trap and set you free. Then you left with him to go back to the city")

    else:
        print("Wrong answer. With zero time left an eagle attacked you thinking you're a little bitch. You died")

main()