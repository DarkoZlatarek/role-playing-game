# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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


dict_of_characters = {}
warrior = Character('warrior', 200, 15, 20)
mage = Character('mage', 130, 30, 10)

dict_of_characters[warrior.rase] = warrior
dict_of_characters[mage.rase] = mage


def character_choice():
    '''
    Get users choice of the character.
    Run a while loop to collect a valid input from the user
    via the terminal, which must be either warrior or mage.
    The loop will repeatedly request the input until it is valid.
    '''

    while True:
        user_input = input('Choose character. Warrior or mage?\n')
        user_choice = user_input.lower()

        if validate_input(user_choice):
            print('You have chosen:\n' ,dict_of_characters[user_choice])
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


def start_game():
    '''
    User will chose if he want's to start the game or quit
    before even trying.
    '''

    input_start = input('Type "start" to start the game or "exit" to quit:\n')
    start = input_start.lower()

    if start == 'start':
        print('Let\' begin')
        return
    elif start == 'exit':
        print('See you later')
        sys.exit()
    elif start != 'start' or 'exit':
        print('Don\'understand')
        start_game()


def main():
    start_game()
    character_choice()


print('Welcome to role playing game!\n')

main()

