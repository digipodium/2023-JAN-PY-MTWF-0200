import os

while True:
    os.system('cls') # clear screen
    print("Calculator")
    print('1. ➕')
    print('2. ➖')
    print('3. ❌')
    print('4. Exit')
    ch = input('Select a number >>>')
    if ch == '1':
        a = int(input("Enter value 1:"))
        b = int(input('Enter value 2:'))
        print(f'{a}+{b}={a + b}')
    elif ch == '2':
        pass
    elif ch == '3':
        pass
    elif ch == '4':
        print('Bye!')
        break
    else:
        print('invalid input')
    input('continue')