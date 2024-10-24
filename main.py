from libs import welcome_message, exit_program
from games import zenshin
from tools import warungmini

def options():
    user_option = int(input(f'Menu program:\n1. Games ZENSHIN\n2. Warung mini\n3. Keluar\n\nSilahkan pilih: '))

    if user_option == 1:
        zenshin.start()
    elif user_option == 2:
        warungmini.start()
    elif user_option == 3:
        exit_program()
    else:
        print('Hanya boleh pilih yang tersedia di menu!')

def main():
    welcome_message()
    options()

if __name__ == '__main__':
    main()