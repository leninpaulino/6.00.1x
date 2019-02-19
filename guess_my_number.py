print('Please think of a number between 0 and 100!')
low = 0
high = 100
ans = int((low + high)/ 2)

while True:
    print('Is your secret number ' + str(ans) + '?')
    option  = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    if option == 'c':
        print('Game over. Your secret number was: ' + str(ans))
        break
    elif option == 'h':
        high = ans
        ans = int((low + high)/ 2)
    elif option == 'l':
        low = ans
        ans = int((low + high)/ 2)
    else:
        print('Sorry, I did not understand your input.')

