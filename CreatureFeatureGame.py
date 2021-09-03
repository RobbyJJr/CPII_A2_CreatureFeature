# import CreatureFeatureA2
################ Creature Feature ###################
"""
This is a text based game using three classes (Orc,Fairy,Elf) to simulate characters fighting to the death
"""


# Import the orc, fairy, elf class definitions
from creature import *

# Setup the data structures

listOChars = []
charClass = ['Elf', 'Fairy', 'Orc','duck']

# Game Functions
def pickName(_char):
  name = ''
  while len(name)==0:
    name = input(f'What is the name of your {charClass[_char]}? ')
  return name
def charChoice():
  # try:
    print('Please choose a character type from the following list:')
  # except:
  #   print("Please enter a valid integer")
    for i, charType in enumerate(charClass):
        print(f'{i}: {charType}')
    #listOChars.append(int(input("")))
    return int(input('Your choice: '))


#Game Setup

print("Welcome to the Creature Feature")

print('#' * 40)

print('\n' * 2)

numChar = ''
while not numChar.isnumeric():
  numChar = input("How many characters would you like to have in the game? (integer) ")
numChar = int(numChar)

for i in range(numChar):
    char = charChoice()
    name = pickName(char)
    # do we want to implement 'points' allocation?

    # instantiate character based on char type
    listOChars.append(eval(charClass[char])(name))
    # append the character to the listOChars

######### Game Loop ##############
# Turn based 

# loops
#check if the character is dead or not  midsn46
# If the character is dead, lets remove that character from the listOchars

"""
# Mr.E to Sam and Caden 
Lets build in the character death into the attack function.  That way we can describe the death easily.
"""
#health check

# reverse order who got attacked first

# need to run a loop on all the players in listOchars (from Mr.E)