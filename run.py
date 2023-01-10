# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys
from random import randint


class Character:
    '''
    Creates the characters
    '''
    def __init__(self, rase, health, strength, defense):
        self.rase = rase
        self.health = health
        self.strength = strength
        self.defense = defense

    def __str__(self):
        return f'rase: {self.rase} \n health: {self.health} \n strength: {self.strength} \n defense: {self.defense}'


INTRO_STORY = 'Many years ago, warriors, mages and dark elves '\
    'lived in unity. They shared\nknowledge of their ancestors '\
    'and the way of life between each other. Until\none day '\
    'dark elves decided that warriors and mages are beneath '\
    'them. Dark\nelves migrated away from the warriors and mages '\
    'into the mountains. For many\nyears, they stick for '\
    'themselves, but their resources were running low so\nthey '\
    'started raiding villages of warriors and mages. '\
    'Stealing their food,\nwomen and man for slaves. '\
    'One day, they have crossed the line.....\n\n'

COWARD = '“I am sorry, but I can not help you”. You go back to '\
    'The Rusty Cog Inn, sit by the bar and order another rakia. '\
    'All eyes were on you and you know exactly what everyone was '\
    'thinking. You stand up and shout: “I can not save here!! Now '\
    'leave me to drink in peace!!” You sit back down, finish your '\
    'glass and order another rakia.\n\n'

F_FOREST = '”Alright. I will save the princes” you say and '\
    'head towards The Forbidden forest.\n'

PYTHON = '\nAs you step into The Forbidden forest, you feel the '\
    'sudden change on your\nskin. Air becomes heavier, colder '\
    'and you feel like someone is watching you.\nYou can see '\
    'the footprints on the path and you know these are from the '\
    'dark\nelves because of the shape of them. Only three toes '\
    'and double the size of\nyour own. You follow the footprints '\
    'and all of a sudden, something jumps on\nyou from the bushes. '\
    'You manage to fight it and toss it away from you onto\nthe '\
    'footpath. Great big eyes are staring at you with fangs as long '\
    'and sharp\nas butcher\'s knife. It is a python and you realize '\
    'you need to fight it and\nthat there will be more danger here '\
    'then just dark elves.\n'\
    '\npython\nhealth: 10\nstrength: 5\ndefense: 2\n'

DEMON = 'As you step over the python\'s dead body and continue '\
    'follow the footprints,\nyou start to notice that trees '\
    'are bare, without any leaves. Air is getting\nas thick '\
    'as ever and as cold as you never experienced before. You '\
    'remember\nthe old tales and know you are now approaching '\
    'Harskelisia, the demon that\nwill kill you by just looking '\
    'at you, but she will let you\npass if you solve here riddle.\n'\
    '“Greetings, stranger. If you wonder to far from your home,'\
    '\nyou might never go back.” cold and shaky voice says and '\
    'the figure appears\nfrom behind the fog. “Please, '\
    'Harskelisia, I am trying to catch\ndark elf Dralahi. He '\
    'took the princess Astrid.\nCan you let me pass, please?” '\
    'you ask.\n“If you want to eat meat, you need to kill the '\
    'animal.\nIf you want to drink wine, you need to squash the '\
    'grapes.\nIf you want to pass, you need to solve the riddle.”\n'


dict_of_characters = {}
warrior = Character('warrior', 200, 15, 20)
mage = Character('mage', 130, 30, 10)

dict_of_characters[warrior.rase] = warrior
dict_of_characters[mage.rase] = mage


def start_game():
    '''
    User will choose if he want's to start the game or quit
    before even trying.
    '''

    input_start = input('Type "start" to start the game or "exit" to quit:\n')
    start = input_start.lower()

    if start == 'start':
        return
    if start == 'exit':
        print('You could have at least try. Good bye!')
        sys.exit()
    elif start != 'start' or 'exit':
        print('Don\'t understand.')
        start_game()


def message(string):
    '''
    Prints the string to the terminal letter by letter with
    time delay.
    '''
    for i in string:
        print(i, end='', flush=True)
        time.sleep(0.05)


def character_choice():
    '''
    Get users choice of the character.
    Run a while loop to collect a valid input from the user
    via the terminal, which must be either warrior or mage.
    The loop will repeatedly request the input until it is valid.
    '''

    while True:
        print('Choose a rase you want to play with:\n')
        print(f'{warrior} \n')
        print(f'{mage} \n')
        user_input = input('Type warrior or mage?\n')
        user_choice = user_input.lower()

        if validate_input(user_choice):
            print('\n You have chosen:\n', dict_of_characters[user_choice])
            break

    return user_choice


def validate_input(choice):
    '''
    Inside the try, raises ValueError if input from the user
    is not one of the character they can chose from.
    '''
    try:
        if choice not in dict_of_characters:
            raise ValueError('Sorry, don\'t know who that is.')
    except ValueError as v_e:
        print(f'{v_e}, chose between warrior or mage!\n')
        return False

    return True


def chose_name():
    '''
    Collects the user's name input.
    '''
    user_name = input('\nType your name:\n')

    def input_name_check():
        '''
        User confirming that the name they typed is the one they want.
        '''
        name_check = input(f'Is {user_name} name you want? y/n\n')
        name_confirmation = name_check.lower()
        return name_confirmation

    name_confirmed = input_name_check()

    if name_confirmed == 'y':
        return user_name
    if name_confirmed == 'n':
        chose_name()
    elif name_confirmed != 'y' or 'n':
        print('Sorry, was that "y" or "n"?\n')
        input_name_check()


def start_story(char, name):
    '''
    Prints the string to the terminal letter by letter with
    time delay.
    '''

    story = f'You are sitting in the The Rusty Cog Inn, drinking your'\
        ' usual drink, rakia. It is a homemade spirit made by the Inn\'s '\
        'owner Balrus. You are chatting with Balrus over the bar when all '\
        f'of a sudden a man came rushing in yelling: "Hey, {char} {name}!! '\
        'The king needs you! You need to go quick, his daughter was taken '\
        'by the evil dark elf Dralahi and you are the only person who '\
        'dares to go against him. Go! Go! Go! Time is of essence!"'\
        '.\n.\n.\n.\n.\n.\n You quickly finish your rakia and start running '\
        'to see the king. As you are approaching the king, he starts '\
        f'running towards you and starts begging: "Please {name}, you '\
        'need to save my Astrid. I beg of you."\n "Where did he took here" '\
        'you ask.\n"Into The Forbidden forest. Astrid does\'t like that '\
        'place." says the king.\n'\
        '"No one does, my king, apart from dark elves" you say.\n'\
        'Deep down you know you still love Astrid.\n'

    for i in story:
        print(i, end='', flush=True)
        time.sleep(0.05)


def next_move(char, name):
    '''
    User chooses if he wants to go after the princes or not.
    '''
    
    save_princes = input('What will you do? A/B\nA) Save the princes\nB) Go back to The Rusty Cog Inn\n')
    choice = save_princes.lower()

    if choice == 'a':
        message(F_FOREST)
        return
    if choice == 'b':
        message(COWARD)
        print(f'You became known as {char} {name} the coward.')
        sys.exit()
    elif choice != 'a' or 'b':
        print('Sorry, didn\'t understand that.')
        next_move(char, name)


def dice_roll_input():
    '''
    Askes the user to type "roll" to run the function that
    simulates rolling the dice.
    '''
    print('Roll more then "1" to kill the python.\n')
    dice_conf = input('Type "roll" to roll the dice\n')

    if dice_conf == 'roll':
        return
    if dice_conf != 'roll':
        dice_roll_input()


def roll_dice():
    '''
    Simulates rolling the dice and returning the result.
    '''
    random_dice = randint(1,6)
    return random_dice


def kill_python(dice):
    '''
    Based on the dice roll, either python gets killed or
    it dodges the attack and user needs to roll again.
    '''
    if dice == 1:
        print(f'You rolled: {dice} \n')
        print('Python dodged your attack. Try again.\n')
    else:
        print(f'You rolled: {dice} \n')
        print('You killed the python!\n')


def attack_python():
    '''
    Function to loop through dice rolls until dice>1.
    '''
    dice = 1
    while dice == 1:
        dice_roll_input()
        dice = roll_dice()
        kill_python(dice)


def main():
    """
    Run all program functions
    """
    start_game()
    message(INTRO_STORY)
    character = character_choice()
    name = chose_name()
    start_story(character, name)
    next_move(character, name)
    message(PYTHON)
    attack_python()
    message(DEMON)
   

print('Welcome to fantasy role playing game!\n')
main()
