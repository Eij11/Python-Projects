import os
import sys
import time


def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
        #time.sleep(0.001)
def header():
    print('=========================xxxxx============================')
    print("\t\t\tTomb Raider")
    print('=========================xxxxx============================')

def neym(name):
    get_name = name
    return get_name


def scenario():
    get_name = neym(name)
    header()
    print_s("Scenario: You're one of the renounced adventurer ever known.\nWith such wealth, also comes with your greediness; that would\nlater cause your downfall!.\nYour team have recently discovered the tomb of the gods.\nYou've hastily went to discover and grab all the treasures.")
    time.sleep(2)
    os.system('cls')

    header()
    print_s("Scenario: You and your team was surpirsed, seeing how easy it\nis to get in. A few hours later, you've reached the treasure area.\nThe treasures seen are far as the eye can see. But the most\nprized parts are the treasures besides the tombs.")

    print_s("\n\nWhats your move?")
    print("\n\t[1] Get the treasures")
    print("\t[2] Ignore the treasures")

    move = int(input(">> "))
    os.system('cls')
    if move == 1:
        header()
        print_s("With the wide grin on your face. You grabbed all the treasures\nbut was later on surprised on what appears before you.")
        time.sleep(1)
        os.system('cls')

    elif move == 2:
        header()
        print_s(get_name + ": Let's leave it be as a sign of respect to\nthe ones who's resting here.\n\nYou've abstained from getting all the\ntreasures. But it's different from everyone; one of your\nteam was swayed by the treasures glamour.\nAnd later, someone appears before you.")
        time.sleep(2)
        os.system('cls')

def god():
    get_name = neym(name)
    header()
    print_s("?%!: Who dares trespass and disturbs this place?\n" + get_name + ": Who are you?\n?%!: We're the Olympian gods resting on this place.\nNot only you have hoarded all the treasures, you were\ndisrespectful for getting what was on our tombs!\n?%!: If you want to live, answer 5 questions correctly,\nand you shall be spared.\n?%!: You only have 3 lives, if you've answered three questions\nuncorrectly you shall perish here, immediately!")

    print_s("\n\n\t\tQuestions Loading...")
    time.sleep(4)
    os.system('cls')

def lose():
    header()
    print_s("?%!: You guys aren't only greedy but too dumb to answer\nthese questions. I hope you're ready for the retribution\nyou guys deserve!")
    time.sleep(1)
    os.system('cls')


def win():
    header()
    print_s("?%!: Congratulations on passing the test. I hope you've\nlearned your lesson at this point. Never try to disturb nor rob\nsomeone's resting place! Leave!")
    time.sleep(1)
    os.system('cls')



#Main
header()
keys = input("\t\t[Press any keys to start]")
os.system('cls')

if keys == keys:

    header()
    name = input("Enter your adventurer name>> ")
    get_name = neym(name)
    print(get_name)
    os.system('cls')

    scenario()
    god()

points = 0
lives = 3
while True:
    header()
    print_s("1. What is the monster, who is a half-man, half-bull\nimprisoned in a labyrinth at Knossos called?")
    answer = input("\n\n>> ")
    answer = answer.lower()
    if answer == "minotaur":
        print_s("\n?%!: You've answered correctly! ")
        points +=1
    else:
        lives-=1
        print_s("\nWrong! you only have " + str(lives) + " chance/s left!")
    time.sleep(1)
    os.system('cls')

    header()
    print_s("2. He was considered the best musician and poet of all,\nand he perfected the lyre. He went to the underworld\nto save her lover")
    answer1 = input("\n\n>> ")
    answer1 = answer1.lower()
    if answer1 == "orpheus":
        print_s("\n?%!: You've answered correctly! ")
        points +=1
    else:
        lives-=1
        print_s("\nWrong! you only have " + str(lives) + " chance/s left!")
    time.sleep(1)
    os.system('cls')

    header()
    print_s("3. He was infamous for cheating death twice. He's also\nknown having an eternal punishment of forever rolling a\nboulder up a hill. Who is he?")
    answer2 = input("\n\n>> ")
    answer2 = answer2.lower()
    if answer2 == "sisyphus":
        print_s("\n?%!: You've answered correctly! ")
        points +=1
    else:
        lives-=1
        print_s("\nWrong! you only have " + str(lives) + " chance/s left!")
        if lives == 0:
            time.sleep(1)
            os.system('cls')
            break
    time.sleep(1)
    os.system('cls')

    header()
    print_s("4. A careless son, who did not heed his father's warning.\nHe died flying ambitiously near the sun.")
    answer2 = input("\n\n>> ")
    answer2 = answer2.lower()
    if answer2 == "icarus":
        print_s("\n?%!: You've answered correctly! ")
        points +=1
    else:
        lives-=1
        print_s("\nWrong! you only have " + str(lives) + " chance/s left!")    
        if lives == 0:
            time.sleep(1)
            os.system('cls')
            break
    time.sleep(1)
    os.system('cls')

    header()
    print_s("5. What walks on four feet in the morning, two in the\nafternoon and three at night?")
    answer2 = input("\n\n>> ")
    answer2 = answer2.lower()
    if answer2 == "man":
        print_s("\n?%!: You've answered correctly! ")
        points +=1
    else:
        lives-=1
        print_s("\nWrong! you only have " + str(lives) + " chance/s left!")    
        if lives > 0 or lives == 0:
            time.sleep(1)
            os.system('cls')
            break
    time.sleep(1)
    os.system('cls')
    break
        
if lives > 0:
    win()
    time.sleep(1)
    os.system('cls')

elif lives == 0:
    lose()
    time.sleep(1)
    os.system('cls')

header()
get_name = neym(name)
print_s("\t\tThank you for playing!")
print_s("\n\tName: " + get_name)
print_s("\n\tCorrect answers: " + str(points))
print_s("\n\tLives left: " + str(lives))