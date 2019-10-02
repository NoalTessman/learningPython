secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count <guess_limit:
    guess = int(input('Guess:'))
    guess_count +=1
    if guess == secret_number:
        print('You are winner')
        break
  #  elif guess_count == 3:
  #      print('you are lose')
  #      break
else:
    print('you are lose')
#else statement applies to while if while fails
