import random
import main

def start():
    while True:
        cave_shape = "|_|"
        empty_cave = [cave_shape] * 4

        zen_position = random.randint(1, 4)

        cave = empty_cave.copy()
        cave[zen_position - 1] = "|0_0|"

        empty_cave = '  '.join(empty_cave)
        cave = '  '.join(cave)
        
        print(f'Coba perhatikan goa dibawah ini!\n\n{empty_cave}\n')

        user_choise = int(input("Menurut kamu di goa nomor berapa ZEN berada? [1 / 2 / 3 / 4]: "))

        if user_choise == zen_position:
            print(f"\n {cave} \n\n Selamat kamu menang! Posisi ZEN ada di goa nomor {zen_position} dan pilihanmu adalah {user_choise}.")
        else:
            print(f"\n {cave} \n\n KAMU KALAH! ZEN bukan berada di situ, tapi ada di goa nomor {zen_position}. Sedangkan kamu memilih goa nomor {user_choise}.")
            
        play_again = input("\n\nApakah masih ingin melanjutkan gamenya lagi? [y/n]: ")
        if play_again == "n":
            main.options()
        elif play_again == "y":
            continue
        else:
            print("Dasar tolol!!")
            exit()
    
if __name__ == '__main__':
    start()