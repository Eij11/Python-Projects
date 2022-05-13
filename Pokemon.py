import random
import sys
import os
import time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        #time.sleep(0.04)
        time.sleep(0.001)

def header():
    print('\t\t\tPokemon')
    print('=========================xxxxx============================')


def introduction():
    header()
    print_slow('In the world which you are about to enter, you will embark\non a grand adventure with you as the hero. New paths will open to you\nby helping people in need, overcoming challenges, and solving mysteries.\nThrough your adventure, we hope that you will interact with all sorts of\npeople and achieve personal growth. That is our biggest objective.')
    time.sleep(1)
    os.system('cls')

def prof_oak():
    header()
    print_slow('???: Hello, there! Glad to meet you! Welcome to the world of Pokemon.\n???: My name is Oak.')
    print_slow('\nOak: People affectionately refer to me as the POKEMON PROFESSOR.\nThis world is inhabited far and wide by creatures called POKÉMON.\nOak: For some people, POKÉMON are pets. Others use them for battling.\nAs for myself, I study pokemons.\n\nOak: But first, tell me a little about yourself.')
    time.sleep(1)
    os.system('cls')


def gender1(choice):
    gender = ''
    if choice == 1:
        gender = 'Boy'
    if choice == 2:
        gender = 'Girl'
    return gender

def name1(name_ch):
    name = name_ch
    return name

def room():
    choice1 = 0
    header()
    print_slow('Now that everything is settled. Are you now ready to\nstart your own journey?')
    time.sleep(1)
    os.system('cls')

def room1():
    header()
    print_slow('You woke up in your room.')
    print('\n\t[1] Look at the bookshelf')
    print('\t[2] Look at the window')
    print('\t[3] Go down the stairs')
    choice1 = int(input("\nWhat's your move? "))

    if choice1 == 1:
        print_slow("Bookshelf Contents: \n1. Surf's Up, Pikachu!\n2. Meowth, The Big Mouth\n3. Raichu Shows Off\n4. Pichu's Apple Company")
        back = input("\n\n[Enter any key to go back.] ")
        if back == back:
            os.system('cls')
            room1()
    if choice1 == 2:
        print_slow("It's a sunny day, pidgey's flew by to greet you. Nidorans'\nare playing together on the grassy field; oddishes are \nsinging together under the tree's shade.")
        back = input("\n\n[Enter any key to go back.] ")
        if back == back:
            os.system('cls')
            room1()

    if choice1 == 3:
        os.system('cls')


def living_room():
    name = name1(name_ch)
    header()
    print_slow("You went downstairs...")
    print('\n\t[1] Greet your mother')
    print('\t[2] Go outside')
    choice1 = int(input("\nWhat's your move? "))
    if choice1 == 1:
        print_slow("\nYou walked towards your mother, gave her a hug, before going out.\nMom: Good morning " + name + ". Prof. Oak is waiting inside\nhis laboratory.")
        time.sleep(1)
        os.system('cls')
    if choice1 == 2:
        pass
    os.system('cls')
   
def outside():
    name = name1(name_ch)
    header()
    print_slow("As you opened the door a wide open field greets you at sight.")    
    print('\n\t[1] Go to the lab')
    print('\t[2] Go out to the wilderness')
    choice1 = int(input("\nWhat's your move? "))
    if choice1 == 1:
        print_slow("Oak: Oh, " + name + " your here! Welcome to my lab!" )
        time.sleep(1)
    if choice1 == 2:
        print_slow("Oak: Hey, " + name + " it's dangerous out there! Come\nto my lab first!" )
        time.sleep(1)
    os.system('cls')

def lab():
    name = name1(name_ch)
    header()
    print_slow("Laboratory: ")
    print('\n\t[1] Inspect object one')
    print('\t[2] Inspect object two')
    choice1 = int(input("\nWhat's your move? "))
    if choice1 == 1:
        print_slow("A big machince with lots of buttons. Better\nnot mess things around")
        time.sleep(1)
        os.system('cls')
        lab()
    if choice1 == 2:
        print_slow("Oak: Oh, these are the Pokemons that i'm giving you\nguys today")
        print_slow("\n???: Gramps where are you?\nOak: " + name + " this is your rival since you guys were kids.")

def lab1(rival_name):
    name_r = rival_name
    return name_r

def lab2():
    header()
    name = name1(name_ch)
    name_r = lab1(rival_name)
    print_slow(name_r + ": I didn't think you'd be here already!\nGramps let's get this over with already. I still have\nan adventure to accomplish!\nOak: " + name + " when travelling you should always be accompanied\nby a Pokemon. We never know if the journey will be perilous.")
    time.sleep(2)
    os.system('cls')

def i_choose_you():
    header()
    print_slow("Oak: Now, choose one of the starter Pokemons: ")
    print('\n\t[1] Bulbasaur  [2] Squirtle   [3] Charmander ')


def i_choose_you1(ch_pokemon):
    name_r = lab1(rival_name)
    player_pokemon = ""
    rival_pokemon = ""
    if ch_pokemon == 1:
        print_slow("Bulbasaur is a Grass/Poison type Pokémon. It is known as the Seed Pokémon.")
        print_slow("\n" + name_r + ": Then I'll choose this one: Charmander")
        print_slow("\n\nYou obtained Bulbasaur!")
        time.sleep(1)
        player_pokemon = "Bulbasaur"
        rival_pokemon = "Charmander"
        os.system('cls')

    if ch_pokemon == 2:
        print_slow("Squirtle is a Water type Pokémon. It is known as the Tiny Turtle Pokémon ")

        print_slow("\n" + name_r + ": Then I'll choose this one: Bulbasaur")
        print_slow("\n\nYou obtained Squirtle!")
        time.sleep(1)
        player_pokemon = "Squirtle"
        rival_pokemon = "Bulbasaur"
        os.system('cls')

    if ch_pokemon == 3:
        print_slow("Charmander is a Fire type Pokémon. It is known as the Lizard Pokémon .")
        print_slow("\n" + name_r + ": Then I'll choose this one: Squirtle")
        print_slow("\n\nYou obtained Charmander!")
        time.sleep(1)
        player_pokemon = "Charmander"
        rival_pokemon = "Squirtle"
        os.system('cls')

    return player_pokemon, rival_pokemon

def i_choose_you2(ch_pokemon):
    player_pokemon = ""
    rival_pokemon = ""

    if ch_pokemon == 1:
        player_pokemon = "Bulbasaur"
        rival_pokemon = "Charmander"
    if ch_pokemon == 2:
        player_pokemon = "Squirtle"
        rival_pokemon = "Bulbasaur"
    if ch_pokemon == 3:
        player_pokemon = "Charmander"
        rival_pokemon = "Squirtle"

    return player_pokemon, rival_pokemon

def challenge():
    name_r = lab1(rival_name)
    header()
    print_slow("As you procceed to exit the lab, someone stopped you.")
    print_slow("\n" + name_r + ": Hey, wanna battle to have a little bit\nof experience before heading outside?")

    print_slow("\n\n\t\tBattle area loading...")
    time.sleep(1)
    os.system('cls')

def credits():
    player_pokemon, rival_pokemon = i_choose_you2(ch_pokemon)
    name_p = name1(name_ch)
    genderx = gender1(choice)
    header()
    print_slow("Thank you for playing this show text game!\nIts inspired by the game Pokemon: Fire Red")
    print("\n\tPlayer: " + name_p)
    print("\tGender: " + genderx)
    print("\tPokemon: " + player_pokemon)
    time.sleep(3)
#MAIN

print('\t\t\tPokemon')
print('=========================xxxxx============================')
print('\t\t\t[1] Start')
start = int(input('>> '))
os.system('cls')
if start == 1: 
    introduction()
    prof_oak()

    header()
    print('Are you a boy or a girl?')
    print('\t[1] Boy')
    print('\t[2] Girl')
    choice = int(input('\n>> '))
    gender1(choice)
    
    name_ch = input("Oak: What's your name? ")
    os.system('cls')
    #print(name1(name_ch))

    room()
    room1()
    living_room()

    outside()

    lab()
    rival_name = input("\nOak: What was his name again? ")
    os.system('cls')
    lab2()

    i_choose_you()
    ch_pokemon = int(input("\nWho do you choose? "))
    i_choose_you1(ch_pokemon)
    #print(i_choose_you2(ch_pokemon))

    challenge()

    #print(i_choose_you1(ch_pokemon))

    player_pokemon, rival_pokemon = i_choose_you2(ch_pokemon)

    name_p = name1(name_ch)
    name_r = lab1(rival_name)
    print('\t\tPokemon: Fire Red')
    print_slow("\n" + name_p + ": Go " + player_pokemon + "!")
    print_slow("\n"+ name_r + ": Go " + rival_pokemon + "!")

    p_pokemon_hp = 200
    p_pokemon_atk_scrath = random.randint(25, 30)
    p_pokemon_atk_tackle = random.randint(20, 25)
    r_pokemon_hp = 200
    r_pokemon_atk_tackle = random.randint(25, 30)
    r_pokemon_atk_qckatk = random.randint(20, 25)

    player_pokemon, rival_pokemon = i_choose_you2(ch_pokemon)
    while True:
        print('\n=========================xxxxx============================')
        print("||   [1] Scracth                  [2] Tackle             ||")
        print("||                                                       ||")
        print("||   -----------                  ----------             ||")
        print("||                                                       ||")
        print('=========================xxxxx============================')

        move = int(input("Deploy Move >> "))
        if move == 1:
            r_pokemon_hp -= p_pokemon_atk_scrath
            print_slow("\n" + player_pokemon + " used Scratch!")
            print_slow("\n" + rival_pokemon + " HP: " + str(r_pokemon_hp))
            print_slow("\n" + name_r + "'s turn!")
            time.sleep(1)

        elif move == 2:
            r_pokemon_hp -= p_pokemon_atk_tackle
            print_slow("\n" + player_pokemon + " used Tackle!")
            print_slow("\n" + rival_pokemon + " HP: " + str(r_pokemon_hp))
            print_slow("\n" + name_r + "'s turn!")
            time.sleep(1)

        r_move = random.randint(1,3)
        print("\n")
        if r_move == 1:
            print_slow("\n" + rival_pokemon + " missed!")
            print_slow("\n" + name_p + "'s turn!")
            time.sleep(1)
        elif r_move == 2:
            p_pokemon_hp -= r_pokemon_atk_tackle
            print_slow("\n" + rival_pokemon + " used Tackle!")
            print_slow("\n" + player_pokemon + " HP: " + str(p_pokemon_hp))
            print_slow("\n" + name_p + "'s turn!")
            time.sleep(1)
        elif r_move == 3:
            p_pokemon_hp -= r_pokemon_atk_qckatk
            print_slow("\n" + rival_pokemon + " used Quick Attack!")
            print_slow("\n" + player_pokemon + " HP: " + str(p_pokemon_hp))
            print_slow("\n" + name_p + "'s turn!")
            time.sleep(1)
        os.system('cls')

        if p_pokemon_hp <= 0 or r_pokemon_hp <= 0:
            break

if p_pokemon_hp > r_pokemon_hp:
    header()
    print_slow(name_r + ": Congrats on winning your very first battle!")
    time.sleep(1)
    os.system('cls')

else:
    header()
    print_slow(name_r + ": Looks like I won, see yah loser!")
    time.sleep(1)
    os.system('cls')

credits()
