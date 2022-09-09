from argparse import ArgumentError
from curses.ascii import isalpha, isdigit
from datetime import datetime
import random
import time
import sys

class Player:
    def __init__(self, name, age, hp, defense, atk, score, inv):
        self.name = name
        self.age = age
        self.hp = hp
        self.defense = defense
        self.atk = atk
        self.score = score
        self.inv = inv


class NPC:
    def __init__(self, name, hp, defense, atk, rep):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.atk = atk
        self.rep = rep

data = []

def current_date ():
    return (str(datetime.now()))

# f_csv = open("./game-log.csv", "w")
# writer = csv.writer(f_csv)

def intro():

    # data.append(current_date)
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
        data.append(f"{current_date()}: Age: {age}")
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
                data.append(f"{current_date()}: {name}")
                print("________________________________________________________________________________________________________")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|         Great! And can I also get your social security number, what banking app you use ")
                print("|                                and your mother's maiden name?")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("________________________________________________________________________________________________________")
                response_intro_one = input("(Continue or What):  ")
                data.append(f"{current_date()}: entered {response_intro_one}")
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
                    player = Player({name}, {age}, 10, 10, 10, 5, ["sword", "shield"])
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
                    player = Player({name}, {age}, 10, 10, 10, 5, ["sword", "shield"])
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
                    player = Player({name}, {age}, 10, 10, 10, 5, ["sword", "shield"])
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
    def inventory():
        for i in player.inv:
            print(f"|{str(i)}, ") 
    print(f"________________________________________________________________________________________________________")
    print(f"| Name: {str(*player.name)}                                                       SCORE: {player.score}                                                               ")
    print(f"| Age:  {str(*player.age)}                           ")
    print(f"|________________________                               ")
    print(f"|       Stats:                                                                    ")
    print(f"|   Hp: {player.hp}                                             ")
    print(f"|   Def: {player.defense} ")
    print(f"|   Atk: {player.atk}")
    print(f"|_________________________")
    print(f"| INVENTORY:")
    inventory()
    print(f"________________________________________________________________________________________________________")

def game_start():
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       You are an adventurer in a land without magic. Many mystical creatures roam the lands,")
    print("|             yet their origins remain unknown to even the most learned of scholars.")
    print("|               The only known way to combat the many monsters that populate this ")
    print("|                          world is through brute force and dumb luck...")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       Currently you are on a quest given to you by the most respected scholar in the nation,")
    print("               Archibald The Wise. You are to investigate the strange weather patterns")
    print("                  Ocurring in the Orange Mountains. You are close to your goal but...")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    time.sleep(5)
    troll = NPC("troll", 20, 4, 3, 0)
    player_window()
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       Suddenly you are accosted by a troll! He seems quite unpleasent and poised to attack...")

    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    print("Do you HIT or RUN?")
    pinput = input("")
    data.append(f"{current_date()}: {pinput}")
    time.sleep(2)
    attack_mechanics(player, troll, pinput)
    print("You gained 5 HP and 5 ATK after defeating the troll!")
    data.append(f"{current_date()}: Gained 5 HP and 5 ATK")
    time.sleep(7)
    player.score = player.score + 5
    player.hp = 15
    player.atk = 15
    player_window()
    time.sleep(2)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       You have done well to defeat the Troll. But be warned he was but a drop of water in an")
    print("|         ever flowing glass. Moving on you make your way towards the peak of the mountains")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|  You reach the summit of the mountain, gazing upon the land below. It is quite a wonderous sight...")
    print("|             However your attention is drawn to something quite peculiar, something ")
    print("|                               you can't quite describe... ")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       At the top of the mountain an impossible object stands before you. a two dimensional" )
    print("|                   'circle' of sorts. It glows a deeep shade of blue and hums")
    print("|                                       ominously....")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       And suddenly with a blinding flash, a figure emerges from the circle, clad in robes")
    print("                        of crimson. They do not appear friendly and appear to ")
    print("|                                be getting ready to attack...")    
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    cultist_one = NPC("cultist", 45, 10, 4,0)
    pinput=input("HIT or RUN?")
    attack_mechanics(player, cultist_one, pinput)
    player.score = player.score + 5
    player.hp = 20
    player.atk = 20
    print("You gained 5 HP and 5 ATK after defeating the cultist!")
    player_window()
    data.append(f"{current_date()}: Gained 5 HP and 5 ATK.")
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       The cultist strugles to keep standing as the life begins to leave his eyes. Battered and Beaten ")
    print("|              he manages to speak for the last time, his final words coarse and rough...")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|           'Struggle and fall adventurer. That is your destiny from this moment onwards. ")
    print("|              You may have defeated me, but your destiny has unwittingly become tied")
    print("|                     to the end of all things. You will not die a peaceful death, ")
    print("|                        and with my dying breath I curse you and your kin for")
    print("|                                          all eternity...'")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    time.sleep(5)
    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       And with those words the cultist falls, the icy winds of the mountain peak cutting ")
    print("|                  just a bit deeper into your skin. You now have a choice.")
    print("|                    Do you enter the circle and continue your journey,")
    print("|                 or do you return home and try to forget all you have seen?")

    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    game_warp_one()



def game_warp_one ():
    pinput = input("Continue or End: ")
   
    if pinput[0].lower() == "c":
        data.append(f"{current_date()}: Player continued to Crag Rock")
        crag_rock_start()
        # CONTINUE JOURNEY

    elif pinput[0].lower() == "e":
        data.append(f"{current_date()}: Player ended their journey. Ending One")
        # FIRST ENDING
    else:
        data.append(f"{current_date()}: Player entered {pinput} sending to Crag Rock")
        crag_rock_start()
        # CALL THE SAME FUNC FOR C


def crag_rock_start():
    print("Player has chosen Crag Rock")
    with open("game-log.log", mode="w", encoding="utf-8") as my_log:
        for i in data:
            my_log.write(f" {str(i)} |\n")

def attack_mechanics(player, monster,pinput):
    chances = 3
    has_escaped = False
    chance_flag_text = False
    player_window()

    if pinput[0].lower() == "h":
        data.append(f"{current_date()}: Began attacking {monster.name}")
        print(f"YOU ATTACK THE {monster.name} HEAD ON!!!")
    elif pinput[0].lower() == "r":
        data.append(f"{current_date()}: Attempted to run from {monster.name}")
        print(f"You begin trying to escape from the {monster.name}")
    else:
        data.append(f"{current_date()}: Entered invalid input of {pinput}, attacking {monster.name}...")
        print(f"You can't just type whatever you want {str(*player.name)} ! Defaulting to fight mechanics...")


    while monster.hp > 0:
        

        def attack_logic(player, monster, pinput):
            does_hit = random.randint(0, 10)
            if does_hit % 2 == 0:
                data.append(f"{current_date()}: Hit the {monster.name}! They have {monster.hp} hp remaining")
                monster.hp = monster.hp - player.atk
                print(f"A solid hit against the {monster.name}! They have {monster.hp} HP remaining!")
                time.sleep(2)
            else:
                data.append(f"{current_date()}: {monster.name} damaged player! They have {player.hp} hp remaining")
                player.hp = player.hp - monster.atk
                print(f"The {monster.name} lands a hit against you! You have {player.hp} HP remaining!")
                time.sleep(2)
            

        if pinput[0].lower() == "h":
          attack_logic(player,monster,pinput)
                
        elif pinput[0].lower() =="r":
           
            while chances >0:
                does_escape = random.randint(0,20)
                if does_escape >= 19:
                    data.append(f"{current_date()}: Succesfully escaped from {monster.name}!!!")
                    print("YOU SUCCEDED IN ESCAPING!")
                    has_escaped = True
                    break
                else:
                    data.append(f"{current_date()}: Could Not Get Away {str(chances)}")
                    chances= chances -1
                    print(f"You couldn't get away, you have {str(chances + 1)} chances to escape remaining...")
                    time.sleep(2)
                
                if chances <= 0:
                    break
        else:
            attack_logic(player,monster,pinput)
        
        if player.hp <= 0:
            break
        if chances <= 0:
            if chance_flag_text == False:
                data.append(f"{current_date()}: Failled to escape, begun attacking {monster.name}")
                print(f"You are unable to escape! You must face the {monster.name} head on!")
                chance_flag_text = True
                attack_logic(player,monster,pinput)
            else:
                attack_logic(player,monster,pinput)
            

        if has_escaped == True:
            break
    
    if monster.hp <= 0:
        data.append(f"{current_date()}: Succesfully killed {monster.name}")
        print(f"You have succesfully defeated the {monster.name}!")
    
    if player.hp <= 0:
        data.append(f"{current_date()}: Player lost score was {player.score}")
        print("________________________________________________________________________________________________________")
        print("|                                                                                                      |")
        print("|                                                                                                      |")
        print("|                                        YOU HAVE DIED......")
        print(f"                                       SCORE: {player.score}")
        print("|                                                                                                      |")
        print("|                                                                                                      |")
        print("________________________________________________________________________________________________________")
        # writer.writerow(data)
        # f_csv.close()
        with open("game-log.log", mode="w", encoding="utf-8") as my_log:
            for i in data:
                my_log.write(f" {str(i)} |\n")
        sys.exit("You have failed")

    


intro()