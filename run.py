# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import sys


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
        return f'rase: {self.rase} \n health: {self.health} \n '\
            'strength: {self.strength} \n defense: {self.defense}'


INTRO_STORY = 'Many years ago, warriors, mages and dark elves '\
    'lived in unity. They shared knowledge of their ancestors '\
    'and the way of life between each other. Until one-day '\
    'dark elves decided that warriors and mages are beneath '\
    'them. Dark elves migrated away from the warriors and mages '\
    'into the mountains. For many years, they stick for '\
    'themselves, but their resources were running low so they '\
    'started raiding villages of warriors and mages. '\
    'Stealing their food, women and man for slaves. '\
    'One day, they have crossed the line.....\n\n'

COWARD = '“I am sorry, but I can not help you”. You go back to '\
    'The Rusty Cog Inn, sit by the bar and order another rakia. '\
    'All eyes were on you and you know exactly what everyone was '\
    'thinking. You stand up and shout: “I can not save here!! Now '\
    'leave me to drink in peace!!” You sit back down, finish your '\
    'glass and order another rakia.\n\n'

F_FOREST = '“Where did he took her?” you ask.\n'\
    '”Into the forbidden forest. Please you have to help me. '\
    'Only you can save my dear Astrid.” says the king begging\n'\
    '”Alright. I will save the princes” you say and '\
    'head towards The Forbidden forest.'

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
        print(f'Hello {user_name}. Welcome!')
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
        f'running towards you and starts begging: “Please {name}, you '\
        'need to save my Astrid. I beg of you.”\n'\
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


print('Welcome to fantasy role playing game!\n')
main()
