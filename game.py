




from curses.ascii import isalpha, isdigit


class Player:
    def __init__(self, name, age, hp, score):
        self.name = name
        self.age = age
        self.hp = hp
        self.score = score


def intro():

    print("________________________________________________________________________________________________________")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("|       Hello and welcome to GAMENAMEHERE. Before we begin can you please tell me how old you are?")
    print("|                                                                                                      |")
    print("|                                                                                                      |")
    print("________________________________________________________________________________________________________")
    while True:
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
                name = input("")
                # player = Player()
            else:
                required_age = 18 - int(age)
                print("________________________________________________________________________________________________________")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("|                Unfortunately you do not meet the age requirement to play. Come back in " + str(required_age) + " years!     |")
                print("|                                                                                                      |")
                print("|                                                                                                      |")
                print("________________________________________________________________________________________________________")

            break
        else:
            
            print("________________________________________________________________________________________________________")
            print("|                                                                                                      |")
            print("|                                                                                                      |")
            print("|                                Please enter an actual number: ")
            print("|                                                                                                      |")
            print("|                                                                                                      |")
            print("________________________________________________________________________________________________________")
  


intro()