import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display=[]
for letter in chosen_word:
  display.append("_")

lives=6
a=True
while "_" in display:
 display_temp=display
 if lives==0:
  a=False
  print("you lose")
  break;
 guess = input("Guess a letter: ").lower()

 position=0
 for letter in chosen_word:

   if letter == guess:
     display[position]=guess
   position+=1
 
 if guess not in chosen_word:
   lives-=1
 print(f"{display} and {lives} ")
 print(stages[lives])

if a:
 print("you win")
