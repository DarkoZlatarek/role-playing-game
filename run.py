# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


class Character:
    def __init__(self, rase, health, strength, defense):
        self.rase = rase
        self.health = health
        self.strength = strength
        self.defense = defense

    def __str__(self):
        return f"rase: {self.rase} \n health: {self.health} \n strength: {self.strength} \n defense: {self.defense}"


dict_of_characters = {}
warrior = Character('warrior', 200, 15, 20)
mage = Character('mage', 130, 30, 10)

dict_of_characters[warrior.rase] = warrior
dict_of_characters[mage.rase] = mage


character_choice = input("Choose charactert. warrior or mage?\n")
if character_choice in dict_of_characters:
    print("Your character is:\n" ,dict_of_characters[character_choice])
else:
    print(f"Sorry I could not find {character_choice} in records")
