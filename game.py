




from argparse import ArgumentError
from curses.ascii import isalpha, isdigit


class Player:
    def __init__(self, name, age, hp, defense, atk, score):
        self.name = name
        self.age = age
        self.hp = hp
        self.defense = defense
        self.atk = atk
        self.score = score


class NPC:
    def __init__(self, name, hp, defense, atk, rep):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.atk = atk
        self.rep = rep


def intro():

    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       Hello and welcome to GAMENAMEHERE. Before we begin can you please tell me how old you are?")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    while True:
        global age
        age = input("")
        if age.isnumeric():
            if int(age) >= 18:
                print("________________________________________________________________________________________________________")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|         Thank you for that information, could you also give me your name please?   ")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("________________________________________________________________________________________________________")
                global name
                name = input("")
                print("________________________________________________________________________________________________________")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|         Great! And can I also get your social security number, what banking app you use ")
                print("|                                and your mother's maiden name?")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("________________________________________________________________________________________________________")
                response_intro_one = input("(Continue or What):  ")
                if response_intro_one[0].lower() == "w":
                    print("________________________________________________________________________________________________________")
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print(f"|         Aww come on, what's a little secure information between pals, {name}?")
                    print("|                            But in all seriousness I have what I need")
                    print("|                                           *AHEM")
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print("________________________________________________________________________________________________________")
                elif response_intro_one[0].lower() == "c":
                    print("________________________________________________________________________________________________________")
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print(f"|                 Wait seriously? I didn't take you for that much of a sucker, {name}...    ")
                    print("                             AHH forget I said that. Let's just get started...")
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print("________________________________________________________________________________________________________")

                
            else:
                required_age = 18 - int(age)
                print("________________________________________________________________________________________________________")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|                Unfortunately you do not meet the age requirement to play. Come back in " + str(required_age) + " years!     |")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("________________________________________________________________________________________________________")
                age = ""
                print(age)

            break
        else:
            
            print("________________________________________________________________________________________________________")
            print("|                                                                                                      |")
            print("|                                                                                                      |")
            print("|                                Please enter an actual number: ")
            print("|                                                                                                      |")
            print("|                                                                                                      |")
            print("________________________________________________________________________________________________________")
  

def player_window():
    print("Test")


intro()