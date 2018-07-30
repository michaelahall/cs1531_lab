answer="5"
print("Guessing game-Type 'Give up' when you want to stop guessing")
guess = input("Guess: ")
while guess != answer:
  guess = input("Guess:")
  if guess == "Give up":
     print("It was {}".format(answer))
     break
