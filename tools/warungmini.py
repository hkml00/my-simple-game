import main

def start():
    while True:
        print('ini warung apps!')
        play_again = input('Kembali ke menu utama? [y/n]: ')
        
        if play_again == 'y':
            main.options()
        elif play_again == 'n':
            continue
        else:
            print('Tololl!!')
            continue
    
if __name__ == '__main__':
    start()