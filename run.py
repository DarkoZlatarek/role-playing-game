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


MSG = 'Many years ago, warriors, mages and dark elves '\
    'lived in unity. They shared knowledge of their ancestors '\
    'and the way of life between each other. Until one-day '\
    'dark elves decided that warriors and mages are beneath '\
    'them. Dark elves migrated away from the warriors and mages '\
    'into the mountains. For many years, they stick for '\
    'themselves, but their resources were running low so they '\
    'started raiding villages of warriors and mages. '\
    'Stealing their food, women and man for slaves. '\
    'One day, they have crossed the line.....'


dict_of_characters = {}
warrior = Character('warrior', 200, 15, 20)
mage = Character('mage', 130, 30, 10)

dict_of_characters[warrior.rase] = warrior
dict_of_characters[mage.rase] = mage


def start_game():
    '''
    User will chose if he want's to start the game or quit
    before even trying.
    '''

    input_start = input('Type "start" to start the game or "exit" to quit:\n')
    start = input_start.lower()

    if start == 'start':
        return
    elif start == 'exit':
        print('You could have at least try. Good bye!')
        sys.exit()
    elif start != 'start' or 'exit':
        print('Don\'t understand.')
        start_game()


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
    except ValueError as e:
        print(f'{e}, chose between warrior or mage!\n')
        return False
    
    return True


def message(string):
   
    for i in string:
       
        # printing each character of the message
        print(i, end='')
         
        # adding time delay of half second
        time.sleep(0.5)


message(MSG)


def main():
    start_game()
    character_choice()


print('Welcome to role playing game!\n')
main()


