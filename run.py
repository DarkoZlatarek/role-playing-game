# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint
import sys
import time
import story


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


dra_hp = 75
dra_str = 40
dra_def = 5

dralahi_dict = {
    'name': 'Dralahi',
    'health': dra_hp,
    'strength': dra_str,
    'defense': dra_def
    }

dralahi = '\n'.join(f'{key}: {value}' for key, value in dralahi_dict.items())

war_hp = 200
war_str = 20
war_def = 20

mag_hp = 130
mag_str = 30
mag_def = 10


dict_of_characters = {}
warrior = Character('warrior', war_hp, war_str, war_def)
mage = Character('mage', mag_hp, mag_str, mag_def)

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
    except ValueError as err:
        print(f'{err}, chose between warrior or mage!\n')
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

    s_story = f'You are sitting in the The Rusty Cog Inn, drinking your'\
        ' usual, rakia.\nIt is a homemade spirit made by the Inn\'s '\
        'owner Balrus. You are\nchatting with Balrus over the bar when all '\
        f'of a sudden a man came\nrushing in yelling: "Hey, {char} {name}!! '\
        'The king needs you! You need\nto go quick, his daughter was taken '\
        'by the evil dark elf Dralahi\nand you are the only person who '\
        'dares to go against him.\nGo! Go! Go! Time is of essence!"'\
        '.\n.\n.\n.\n.\n.\n You quickly finish your rakia and start running '\
        'to see the king. As you are\napproaching the king, he starts '\
        f'running towards you andstarts begging:\n"Please {name}, you '\
        'need to save my Astrid. I beg of you."\n"Where did he took here" '\
        'you ask.\n"Into The Forbidden forest. Astrid does\'t like that '\
        'place." says the king.\n'\
        '"No one does, my king, apart from dark elves" you say.\n'\
        'Deep down you know you still love Astrid.\n'

    for i in s_story:
        print(i, end='', flush=True)
        time.sleep(0.05)


def next_move(char, name):
    '''
    User chooses if he wants to go after the princes or not.
    '''
    
    save_princes = input('What will you do? A/B\nA) Save the princes\nB) Go back to The Rusty Cog Inn\n')
    choice = save_princes.lower()

    if choice == 'a':
        message(story.F_FOREST)
        return
    if choice == 'b':
        message(story.COWARD)
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
    dice_conf = input('Type "roll" to roll the dice\n')

    if dice_conf == 'roll':
        roll_dice()
        return
    if dice_conf != 'roll':
        dice_roll_input()


def roll_dice():
    '''
    Simulates rolling the dice and returning the result.
    '''
    random_dice = randint(1, 6)
    return random_dice


def kill_python(dice):
    '''
    Based on the dice roll, either python gets killed or
    it dodges the attack and user needs to roll again.
    '''
    if dice <= 2:
        print(f'You rolled: {dice} \n')
        print('Python dodged your attack. Try again.\n')
    else:
        print(f'You rolled: {dice} \n')
        print('You killed the python!\n')


def attack_python():
    '''
    Function to loop through dice rolls until dice>1.
    '''
    print('Roll more then "2" to kill the python.\n')
    dice = 2
    while dice <= 2:
        dice_roll_input()
        dice = roll_dice()
        kill_python(dice)


def want_a_riddle():
    '''
    User will chose weather the want the riddle question.
    If answer is "no" they will "die" and the game will be over.
    '''
    message(story.WANT_A_RIDDLE_QUESTION)
    solve_the_riddle = input('')
    riddle = solve_the_riddle.lower()

    if riddle == 'y':
        message(story.GET_READY)
        solve_riddle()
    elif riddle == 'n':
        message(story.SHAME)
        sys.exit()
    elif riddle != 'y' or 'n':
        message(story.WASTE_TIME)
        want_a_riddle()


def solve_riddle():
    '''
    The user will answer the riddle question and based on
    the answer they will go forward or the game will end.
    '''
    message(story.RIDDLE_QUESTION)
    riddle_input = input('')
    riddle_answer = riddle_input.lower()

    if riddle_answer == 'mushroom':
        message(story.CORRECT_RIDDLE_ANSWER)
    if riddle_answer != 'mushroom':
        message(story.WRONG_RIDDLE_ANSWER)
        print('Game over. Thank you for playing!')
        sys.exit()


def warrior_vs_dralahi():
    '''
    Placeholder
    '''
    global dra_hp
    while dra_hp > 0 and war_hp != 0:
        dice_roll_input()
        dice = roll_dice()
        print(f'You rolled: {dice}\n')

        if dice >= 1:
            dra_hp = dra_hp - (war_str - dra_def)
            dralahi_dict['health'] = dra_hp
            d_dralahi = '\n'.join(f'{key}: {value}' for key, value in dralahi_dict.items())
            print(f'{d_dralahi}\n')
        else:
            print('Dralahi dodged the attack\n')

        if dra_hp <= 0:
            print('Good Game1')
            break
        else:
            message(story.DRALAHI_ATTACK)
            dralahi_vs_warrior()


def dralahi_vs_warrior():
    '''
    Placeholder
    '''
    global war_hp
    while war_hp > 0 and dra_hp != 0:
        dice = roll_dice()
        print(f'Dralahi rolled: {dice}\n')

        if dice >= 1:
            war_hp = war_hp - (dra_str - war_def)
            w_warrior = Character('warrior', war_hp, war_str, war_def)
            print(f'\n{w_warrior}\n')
        else:
            print('You successfully dodged the attack')

        if war_hp <= 0:
            print('Good Game2')
            break
        else:
            warrior_vs_dralahi()


def battle():
    '''
    Placeholder
    '''
    if war_hp > 0:
        warrior_vs_dralahi()

    if dra_hp > 0:
        dralahi_vs_warrior()

'''
def play_again():
    
    Placeholder.
    
    while True:
        try_again = input('Would you like to play again? (Y/N)\n')
        again = try_again.lower()
        if again not in ('y', 'n'):
            print("Invalid input.")
            play_again()
        if again == 'y':
            main()
        else:
            print("Goodbye")
            sys.exit()
            '''


def main():
    """
    Run all program functions
    """
    # start_game()
    # message(story.INTRO_STORY)
    # character = character_choice()
    # name = chose_name()
    # start_story(character, name)
    # next_move(character, name)
    # message(story.PYTHON)
    # attack_python()
    # message(story.DEMON)
    # want_a_riddle()
    # message(story.FINAL_FIGHT)
    # print(dralahi)
    battle()


print('Welcome to fantasy role playing game!\n')
main()
