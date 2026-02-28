import  random
from hangman_word import stage,word,art

live=0
print(art)
select=random.choice(word)
s_lenght=len(select)

placeholder=""
live1=6
for i in range(0,s_lenght):
    placeholder+="-"
print(placeholder)
gameover=False
correct_letters=[]
while not gameover:
  print(f"*********** {live1}/6 is life remaining **********")
  guess = input("Guess the letter: ").lower()

  if guess in correct_letters:
    print("You've already guessed that letter.")
  else:
    if guess in select:
      correct_letters.append(guess)
    else:
      live += 1
      live1 -= 1
      print(f"Your guessed '{guess}' is not in the word, you lose a life.")
      if live == 6:
        print("You lost the game")
        gameover = True

  position = ""
  for letter in select:
    if letter in correct_letters:
      position += letter
    else:
      position += "-"

  print(position)

  if "-" not in position:
    gameover = True
    print("You win the game")

  print(stage[live])

print(f" your word was {select} ")
