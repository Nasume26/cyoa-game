from argparse import ArgumentError
from curses.ascii import isalpha, isdigit
import time


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
                    global player
                    player = Player({name}, {age}, 10, 10, 10, 5)
                    game_start()



                elif response_intro_one[0].lower() == "c":
                    print("________________________________________________________________________________________________________")
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print(f"|                 Wait seriously? I didn't take you for that much of a sucker, {name}...    ")
                    print("                             AHH forget I said that. Let's just get started...")
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print("________________________________________________________________________________________________________")
                    player = Player({name}, {age}, 10, 10, 10, 5)
                    game_start()
                else:
                    print("________________________________________________________________________________________________________")
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print(f"|         ... What? Listen I'm not the most advanced program out there. This isn't")
                    print(f"                     Skyrim your playing here {name}. Try to stick to the given")
                    print(f"                           responses. What even is a {response_intro_one}??")
                    print("                          Nevermind let's just get started...")
                  
                    print("|                                                                                                      |")
                    print("|                                                                                                      |")
                    print("________________________________________________________________________________________________________")
                    player = Player({name}, {age}, 10, 10, 10, 5)
                    game_start()

                
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
        print(f"________________________________________________________________________________________________________")
        print(f"| Name: {str(*player.name)}                                                       SCORE: {player.score}                                                               ")
        print(f"| Age:  {str(*player.age)}                           ")
        print(f"|________________________                               ")
        print(f"|       Stats:                                                                    ")
        print(f"|   Hp: {player.hp}                                             ")
        print(f"|   Def: {player.defense} ")
        print(f"|   Atk: {player.atk}")
        print(f"________________________________________________________________________________________________________")

def game_start():
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       You are an adventurer in a land without magic. Many mystical creatures roam the lands,")
    print("             yet their origins remain unknown to even the most learned of scholars.")
    print("               The only known way to combat the many monsters that populate this ")
    print("                          world is through brute force and dumb luck...")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")

intro()