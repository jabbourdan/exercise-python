import random as rd

class tic_tac_toe_3D():
    def prRed(self,skk): print("\033[91m {}\033[00m" .format(skk))
    def prGreen(self,skk): print("\033[92m {}\033[00m" .format(skk))
    def prPurple(self,skk): print("\033[95m {}\033[00m" .format(skk))
    def prLightPurple(self,skk): print("\033[94m {}\033[00m" .format(skk))
    def prCyan(self,skk): print("\033[96m {}\033[00m" .format(skk))
    def prYellow(self,skk): print("\033[93m {}\033[00m" .format(skk))
    def prLightGray(self,skk): print("\033[97m {}\033[00m" .format(skk))
    def prorange(self,skk): print("\033[90m {}\033[90m" .format(skk))
    '\033[43m'
    def prCyan(self,skk): print("\033[96m {}\033[00m" .format(skk))
    
    def get_player_names(self):
        self.prGreen('-' * 80)
        self.prGreen("                     ██████████████████████████████████████ ")
        self.prGreen("                     █ Welcome to our tic Tac Toe 3D game █ ")
        self.prGreen("                     █   by Gal, Lior, Hagai and Yoav    █ ")
        self.prGreen("                     ██████████████████████████████████████ ")
        self.prGreen('-' * 80)
        print()
        name1 = input(" player 1 enter your name: ")
        print('-' * 80)
        name2 = input(" player 2 enter your name: ")
        print('-' * 80)
        # print(f"{players[starter_index]['name']} is starting the game!")
        names = [name1, name2]
        return names
