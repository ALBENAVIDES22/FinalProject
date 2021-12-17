import time

def chapter5_intro():
    print('this is chapter 5 intro')
    print("*" * 67)
    print()
    print()
    print()
    print()
    print('**Warn the cops about the killer around the house**')
    print('**Find the killer yourself**')
    print('**Leave the house**')
    ch5()

    #After the detective call the cops, the cops enter the house
    #Cops asking the detective question if you need help or with your own

def Warn_the_cops_about_the_killer_around_the_house_hiding():
    move = False
    print('Player talk to the cop about killer hidden')
    print('Player trying to see whats coming next')
    print("And so on they finally found the killer and was arrested him")
    time.sleep(3)
    while move != True:
        answer = input('Will you help cops y/n')
        if answer == 'y':
            time.sleep(3)
            print('Trying to help the cops')
            print('helping... helping...')
            print('Cops arrest the killer and facing life in prison')
        else:
            print('Mission Complete')
            move = True
        return move

def Find_the_killer_yourself():
    move = False
    print('Player walk in the basement')
    print('Player found the killer to catch him')
    print('Player was stabbed by the killer')
    move = True
    time.sleep(3)
    return move

def Leave_the_house():
    move = False
    print('Player is leaving the house')
    print('Cops confront the Player but is still leaving')
    move = True
    time.sleep(3)
    return move

def ch5():
    move = False
    while move != True:
        print('*' * 70)
        print('\nyou are calling chapter5\n')
        print('*' * 70)
        print("There are three options to do after you check the victims")
        print('1. Warn_the_cops_about_killer_hiding')
        print('2. Leave the house')
        print("3. Find killer yourself")
        option = input("which one do you like to do(1-3)")

        if option == '1':
            move = Warn_the_cops_about_the_killer_around_the_house_hiding()
        elif option == '2':
            move = Leave_the_house()
        elif option == '3':
            move = Find_the_killer_yourself()
        else:
            print('invalid choice')
            move = False

        exit()

    # Chapter5finished = True
    # return Chapter5finished