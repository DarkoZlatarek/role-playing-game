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
        return f'rase: {self.rase} \n health: {self.health} \n strength: {self.strength} \n defense: {self.defense}'


INTRO_STORY = 'Many years ago, warriors, mages and dark elves '\
    'lived in unity. They shared knowledge of their ancestors '\
    'and the way of life between each other. Until one-day '\
    'dark elves decided that warriors and mages are beneath '\
    'them. Dark elves migrated away from the warriors and mages '\
    'into the mountains. For many years, they stick for '\
    'themselves, but their resources were running low so they '\
    'started raiding villages of warriors and mages. '\
    'Stealing their food, women and man for slaves. '\
    'One day, they have crossed the line.....\n \n'


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
        User confirming that the name they typed is the one they want
        '''
        name_check = input(f'Is {user_name} name you want? Y/N\n')
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


def main():
    """
    Run all program functions
    """
    start_game()
    message(INTRO_STORY)
    character_choice()
    chose_name()


print('Welcome to fantasy role playing game!\n')
main()
