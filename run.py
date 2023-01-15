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


DRA_HP = 75
DRA_STR = 40
DRA_DEF = 5

dralahi_dict = {
    'name': 'Dralahi',
    'health': DRA_HP,
    'strength': DRA_STR,
    'defense': DRA_DEF
    }

DRALAHI = '\n'.join(f'{key}: {value}' for key, value in dralahi_dict.items())

WAR_HP = 200
WAR_STR = 20
WAR_DEF = 20

MAG_HP = 130
MAG_STR = 30
MAG_DEF = 10


dict_of_characters = {}
warrior = Character('warrior', WAR_HP, WAR_STR, WAR_DEF)
mage = Character('mage', MAG_HP, MAG_STR, MAG_DEF)

dict_of_characters[warrior.rase] = warrior
dict_of_characters[mage.rase] = mage


def start_game():
    '''
    User will choose if he want's to start the game, read
    the rules or quit before even trying.
    '''

    input_start = input('Type "start" to start the game, "rules" to see rules or "exit" to quit:\n')
    input_start = input_start.lower()

    if input_start == 'start':
        return
    if input_start == 'exit':
        print('You could have at least try. Good bye!')
        sys.exit()
    elif input_start == 'rules':
        print(story.RULES)
        start_or_exit()
    else:
        print('Don\'t understand.')
        start_game()


def start_or_exit():
    '''
    User will choose if he want's to start the game
    or quit before even trying.
    '''
    start = input('Type "start" to start the game or "exit" to quit:\n')
    start = start.lower()
    if start == 'start':
        return
    elif start == 'exit':
        print('You could have at least try. Good bye!')
        sys.exit()
    else:
        print('Don\'t understand.')
        start_or_exit()


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
            print('\n You have chosen:\n\n', dict_of_characters[user_choice])
            break

    return user_choice


def validate_input(choice):
    '''
    Inside the try, raises ValueError if input from the user
    is not one of the character they can chose from.
    '''
    try:
        if choice not in dict_of_characters:
            raise ValueError('\nSorry, don\'t know who that is.')
    except ValueError as err:
        print(f'{err} Chose between warrior or mage!\n')
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
        name_check = input(f'\nIs {user_name} name you want? (Y/N)\n')
        name_confirmation = name_check.lower()
        return name_confirmation

    name_confirmed = input_name_check()

    if name_confirmed == 'y':
        return user_name
    elif name_confirmed == 'n':
        chose_name()
    else:
        print('Sorry, was that "y" or "n"?\n')
        input_name_check()


def start_story(char, name):
    '''
    Prints the string to the terminal letter by letter with
    time delay.
    '''

    s_story = f'\nYou are sitting in the The Rusty Cog Inn, drinking your'\
        ' usual, rakia.\nIt is a homemade spirit made by the Inn\'s '\
        'owner Balrus. You are\nchatting with Balrus over the bar when all '\
        f'of a sudden a man came\nrushing in yelling: "Hey, {char} {name}!! '\
        'The king needs you! You need\nto go quick, his daughter was taken '\
        'by the evil dark elf Dralahi\nand you are the only person who '\
        'dares to go after him.\nGo! Go! Go! Time is of essence!"'\
        '.\n.\n.\n.\n.\n.\nYou quickly finish your rakia and start running '\
        'to see the king. As you are\napproaching the king, he starts '\
        f'running towards you and starts begging:\n"Please {name}, you '\
        'need to save my Astrid. I beg of you."\n"Where did he took here" '\
        'you ask.\n"Into The Forbidden forest. Astrid does\'t like that '\
        'place." says the king.\n'\
        '"No one does, my king, apart from dark elves." you say.\n'

    for i in s_story:
        print(i, end='', flush=True)
        time.sleep(0.05)


def next_move(char, name):
    '''
    User chooses if he wants to go after the princes or not.
    '''
    
    save_princes = input('\nWhat will you do?\nA) Save the princes\nB) Go back to The Rusty Cog Inn\n')
    choice = save_princes.lower()

    if choice == 'a':
        message(story.F_FOREST)
        return
    elif choice == 'b':
        message(story.COWARD)
        print(f'You became known as {char} {name} the coward.')
        sys.exit()
    else:
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
    else:
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
        play_again()


def warrior_vs_dralahi():
    '''
    User tipes in "roll" to roll the dice. Based on the dice roll
    User will either hit Dralahi or Dralahi will dodge the attack.
    '''
    global DRA_HP
    while DRA_HP > 0 and WAR_HP != 0:
        dice_roll_input()
        dice = roll_dice()
        print(f'You rolled: {dice}\n')

        if dice >= 3:
            print('You succesfully hit Dralahi!\n')
            DRA_HP = DRA_HP - (WAR_STR - DRA_DEF)
            dralahi_dict['health'] = DRA_HP
            d_dralahi = '\n'.join(f'{key}: {value}' for key, value in dralahi_dict.items())
            print(f'{d_dralahi}\n')
        else:
            print('Dralahi dodged the attack!\n')

        if DRA_HP <= 0:
            print('\nYou have defeated Dralahi!\n')
        else:
            message(story.DRALAHI_ATTACK)
            dralahi_vs_warrior()


def mage_vs_dralahi():
    '''
    User tipes in "roll" to roll the dice. Based on the dice roll
    User will either hit Dralahi or Dralahi will dodge the attack.
    '''
    global DRA_HP
    while DRA_HP > 0 and MAG_HP != 0:
        dice_roll_input()
        dice = roll_dice()
        print(f'You rolled: {dice}\n')

        if dice >= 3:
            print('You succesfully hit Dralahi!\n')
            DRA_HP = DRA_HP - (MAG_STR - DRA_DEF)
            dralahi_dict['health'] = DRA_HP
            d_dralahi = '\n'.join(f'{key}: {value}' for key, value in dralahi_dict.items())
            print(f'{d_dralahi}\n')
        else:
            print('Dralahi dodged the attack!\n')

        if DRA_HP <= 0:
            print('\nYou have defeated Dralahi!\n')
        else:
            message(story.DRALAHI_ATTACK)
            dralahi_vs_mage()


def dralahi_vs_warrior():
    '''
    Dralahi (computer) will roll the dice. Based on
    the roll outcome Dralahi will either attack the
    warrior or warrior will dodge the attack.
    '''
    global WAR_HP
    while WAR_HP > 0 and DRA_HP != 0:
        dice = roll_dice()
        print(f'Dralahi rolled: {dice}')

        if dice > 4:
            print('\nDralahi succesfully hit you!')
            WAR_HP = WAR_HP - (DRA_STR - WAR_DEF)
            w_warrior = Character('warrior', WAR_HP, WAR_STR, WAR_DEF)
            print(f'\n{w_warrior}\n')
        else:
            print('\nYou successfully dodged the attack!\n')

        if WAR_HP <= 0:
            print('Dralahi have defeated you!\n')
        else:
            warrior_vs_dralahi()


def dralahi_vs_mage():
    '''
    Dralahi (computer) will roll the dice. Based on
    the roll outcome Dralahi will either attack the
    mage or mage will dodge the attack.
    '''
    global MAG_HP
    while MAG_HP > 0 and DRA_HP != 0:
        dice = roll_dice()
        print(f'Dralahi rolled: {dice}')

        if dice > 4:
            print('\nDralahi succesfully hit you!')
            MAG_HP = MAG_HP - (DRA_STR - MAG_DEF)
            m_mage = Character('mage', MAG_HP, MAG_STR, MAG_DEF)
            print(f'\n{m_mage}\n')
        else:
            print('\nYou successfully dodged the attack!\n')

        if MAG_HP <= 0:
            print('Dralahi have defeated you!\n')
            continue
        else:
            mage_vs_dralahi()


def battle(char):
    '''
    Based on the user's choice of the character
    appropriate functions will run.
    '''
    if char == "warrior":
        if WAR_HP > 0 and DRA_HP != 0:
            warrior_vs_dralahi()

        if DRA_HP > 0 and WAR_HP != 0:
            dralahi_vs_warrior()

    else:
        if MAG_HP > 0 and DRA_HP != 0:
            mage_vs_dralahi()

        if DRA_HP > 0 and MAG_HP != 0:
            dralahi_vs_mage()


def dralahi_battle_result(char, name):
    '''
    This function runs dralah_defeated_story if Dralahi gets defeated!
    '''
    if DRA_HP <= 0:
        dralahi_defeated_story(char, name)
    else:
        message(story.DRALAHI_VICTORIOUS)


def dralahi_defeated_story(char, name):
    '''
    Prints the string to the terminal letter by letter with
    time delay.
    '''

    s_story = f'You run towards the princes to untie her. She is '\
        'unconscious. You check if she\nis still alive and she is. You '\
        'lift her up and start your way back where\nyou came from. On '\
        'the way, you came across another python, but you easily '\
        'fight\nhim off. Princes is still unconscious as you approach '\
        'the end of The Forbidden\nForest. Stepping out of The Forbidden '\
        'Forest, you see the king and the queen\nnervously waiting not '\
        'far away and looking at where you came out. They start\nrunning '\
        'towards you. “Get the medic, quick! She is alive, but barely.” '\
        'You\nyell. You take the princes into the palace where you find '\
        'the medic. You place\nprinces on the table and the medic examines '\
        f'her. “She will live!” says\nthe medic.\n“Thank you {char} {name}! '\
        'How can we ever repay you?” asks the king.\n“Dralahi will bother '\
        'us no more. You can open a tab for me in The Rusty Cog Inn.\nThat'\
        f' would be nice.” you say.\n“Consider it done, {char} {name}! '\
        'Thank you again!” says the king.\n\nYou make your way to The '\
        'Rusty Cog Inn\n.\n.\n.\n.\n.\n.\nWord will spread and you will '\
        f'become known as The Hero {char} {name}!\n\n'

    for i in s_story:
        print(i, end='', flush=True)
        time.sleep(0.05)


def play_again():
    '''
    Placeholder.
    '''
    global WAR_HP
    global DRA_HP
    global MAG_HP
    while True:
        try_again = input('Would you like to play again? (Y/N)\n')
        try_again = try_again.lower()
        if try_again not in ('y', 'n'):
            print('Don\'t understand.\n')
            play_again()
        if try_again == 'y':
            WAR_HP = 200
            DRA_HP = 75
            MAG_HP = 130
            main()
        else:
            print('Next time then!')
            sys.exit()


def main():
    """
    Run all program functions
    """
    # print(story.INITIAL)
    # start_game()
    # message(story.INTRO_STORY)
    character = character_choice()
    name = chose_name()
    # start_story(character, name)
    # next_move(character, name)
    # message(story.PYTHON)
    # attack_python()
    # message(story.DEMON)
    # want_a_riddle()
    # message(story.FINAL_FIGHT)
    # print(DRALAHI)
    battle(character)
    dralahi_battle_result(character, name)
    print('Thank you for playing!\n')


main()
play_again()
