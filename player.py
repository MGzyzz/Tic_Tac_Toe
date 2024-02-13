class Player:
    def __init__(self, field, symbol):
        self.field = field
        self.symbol = symbol

    def turn_player(self):
        player_x = input('Напишите кооординаты для добавление символа\nx: ')
        player_y = input('y: ')

        if player_x == 'exit' or player_y == "exit":
            exit()
        elif player_x.isdigit() and player_y.isdigit() and int(player_x) <= 2 and int(player_y) <= 2 and self.field.field_validation(int(player_x), int(player_y)):
            print(f"Игрок походил по координатом:\n{'=' * 20}\nX:{player_x}\nY:{player_y}\n{'=' * 20}")
            self.field.make_step(int(player_x), int(player_y), self.symbol)
            print(self.field)
        else:
            self.field.error(player_x, player_y)
            print("\nПОВТОРИТЕ ЗАПРОС СНОВА\n")
            self.turn_player()