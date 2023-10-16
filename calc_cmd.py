import pyperclip


while True:
    try:
        x = str(input('Enter: ')).replace(' ', '').replace('	', '')
        x = int(x) + 250
        while x % 50 != 0:
            x += 1
        print(x)
        pyperclip.copy(x)
        if x == 250:
            break
    except ValueError:
        print("Error")
