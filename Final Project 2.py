#This is a choose your own adventure game!
#QUESTIONS:
# How do I loop my game if the user typed in an error?
def test():
    while path == "portrait" or "balcony" or "stairs":
        if == "portrait":
            print (roulette())
def roulette():




def main():
    print("You're in Bowser's castle and you're trying to save Peach's annoying sister, Raspberry."
          "The only reason you're saving Raspberry is cause you promised Wario you would get him a "
          "date for the Boo's Wedding. Bowser wanted to go Peach but obviously Peach was going with Mario"
          "So Bowser got angry and Toadnapped Peach's sister instead. So now you have to save the bitch for"
          "desperate Wario. Plus he promised to buy you a Yoshi for you to have a faster travel in the games."
          "(Yes selling a Yoshi is illegal.'Yosh-afficking' to be exact. But you always wanted a blue Yoshi "
          "and you know you will take good care......... Anyway, back to the game."
          "You want to go see a large portrait of Peach in the left, a balcony to the right, "
          "and infront of you are stairs going down. Which do you choose?")
    path = str(input("portrait, balcony, or stairs? "))

    if == "portrait":
        print("You jump into the portrait and appeared at a small room. You see a 'Toy' gun on the table and "
              "a letter saying 'play russian roulette. spin the dial once and if you live I will give you Raspberry"
              "if you die, I get to give BOO your dead body as his wedding present. I'm always watching so don't"
              "try anything")
        spinNumber = int(input("How many times will you spin the dial? Pick a number between 1-6 "))
        while spinNumber <= 6:
            print(spinNumber)
            spinNumber = spinNumber - 1
            if spinNumber == 0:
                print ("CLICK! Nothing came out? Since you didn't die Bowser watching from afar just realized he forgot to fully reload the 'Toy' gun."
                       "But, Bowser is a Dragon(....Turle?) of his word. When he gave you Raspberry, the bitch was filling her nails while saying "
                       " 'What took you so long? Even Luigi would have been here quicker than you'....You punched her in the face for her ungrateful ass"
                       "and carried the unconscous bitch over your shoulder to the wedding. Once you arrived you tossed her towards Wario and Raspberry woke up happy in Wario's arms."
                       "You danced with Peach, Mario, and Luigi and told them the tea of how you heard Boswer's minions Gossiping on how Bowser was wearing earplugs to not ear "
                       "Raspberry bitching of not being the next princess during her stay. You got had fun at the party with your blue Yoshi. THE END")
                break

    elif == "balcony":
    elif == "stairs":
    else:
        print("wrong input. Type in only one of the following choices")
        return Path # will it return to the start of the game? Will it loop around to the start until reached final ending?

#1 for/ While Loops
#3 variables
#All INPUTS SANITIZED
#1 function
#Proper variable names
#1 global variable, used in a function

main()
