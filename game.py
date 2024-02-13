from field import Field
from player import Player
from bot import Bot
from checker import Checker
import random


class Game:
    def choose_player(self):
        choose = input("\nХотите ли вы сыграть ещё? Y/N\n").lower()
        if choose == "y":
            return False
        else:
            return True

    def turn_players(self, name_one, name_two, player_one_symbol: str, player_two_symbol: str):
        while True:
            name_one(Field(), player_one_symbol).turn_player()
            if Checker().check_win(player_one_symbol) or Checker().check_tie():
                if self.choose_player():
                    exit()
                else:
                    return True

            name_two(Field(), player_two_symbol).turn_player()
            if Checker().check_win(player_two_symbol) or Checker().check_tie():
                if self.choose_player():
                    exit()
                else:
                    return True

    def player_vs_player(self, name_class_one, name_class_two):
        choose = random.choice(["ИГРОК ПОД НОМЕРОМ ОДИН", "ИГРОК ПОД НОМЕРОМ ДВА"])

        print(f"\n===== ПЕРВЫЙ ХОДИТ {choose} =====\n")
        player_one_symbol = input("Выберите символ для игры. x или o\n").lower()

        while player_one_symbol not in ['x', 'o']:
            player_one_symbol = input(f"Неверный символ! Выберите символ 'x' или 'o': ").lower()

        player_two_symbol = self.choice_of_sign(player_one_symbol)

        if "ИГРОК ПОД НОМЕРОМ ОДИН" in choose:
            print(f"\n===== ИГРОК ПОД НОМЕРОМ ДВА АВТОМАТИЧЕСКИЙ ПОЛУЧАЕТ СИМВОЛ {player_two_symbol} =====\n")
        else:
            print(f"\n===== ИГРОК ПОД НОМЕРОМ ОДИН АВТОМАТИЧЕСКИЙ ПОЛУЧАЕТ СИМВОЛ {player_two_symbol} =====\n")

        self.turn_players(name_class_one, name_class_two, player_one_symbol, player_two_symbol)


    def choice_of_sign(self, player_one):
        if player_one == "x":
            player_two = 'o'
            return player_two
        else:
            player_two = 'x'
            return player_two

    def game_with_bot(self, name_class_one, name_class_two):
        random_choice = random.choice([name_class_one, name_class_two])


        if random_choice == name_class_one:
            print("\n===== ПЕРВЫМ ХОДИТ ИГРОК =====\n")
            player_one_symbol = input("Выберите символ для игры. x или o\n")

            while player_one_symbol not in ['x', 'o']:
                player_one_symbol = input(f"Неверный символ! Выберите символ 'x' или 'o': ").lower()

            player_two_symbol = self.choice_of_sign(player_one_symbol)
            print(f"\nБОТ ПОЛУЧАЕТ СИМВОЛ {player_two_symbol}\n")
        else:
            print("\n===== ПЕРВЫМ ХОДИТ БОТ =====\n")
            player_one_symbol = random.choice(["x","o"])
            print(f"\nБОТ ПОЛУЧАЕТ СИМВОЛ {player_one_symbol}\n")

            reset = name_class_two
            name_class_two = name_class_one
            name_class_one = reset

            player_two_symbol = self.choice_of_sign(player_one_symbol)
            print(f"\nИГРОК ПОЛУЧАЕТ СИМВОЛ {player_two_symbol} \n")

        self.turn_players(name_class_one, name_class_two, player_one_symbol, player_two_symbol)


    def main(self):
        while True:
            Field().return_of_the_playing_field()
            print(Field())
            choose = input(
                "Привествую в игре КРЕСТИКИ-НОЛИКИ. В какой режим вы хотите поиграть. Выбор осуществляется с помощью индексов, так же вы можете выйти из игры написав команду exit:\n[1] Игрок против игрока\n[2] Игрок против бота\n")
            match choose:
                case "1":
                    self.player_vs_player(Player, Player)
                case "2":
                    self.game_with_bot(Player, Bot)
                case "exit":
                    exit()
                case _:
                    print("Введена неверная команда, попробуйте еще раз")


Game().main()
