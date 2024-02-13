import random
from player import Player


class Bot(Player):

    def turn_player(self):
        value_one = random.randint(0, 2)
        value_two = random.randint(0, 2)
        if self.field.field_validation(value_one, value_two):
            self.field.make_step(value_one, value_two, self.symbol)
            print(f"Бот походил по координатом:\n{'=' * 20}\nY:{value_one}\nX:{value_two}\n{'=' * 20}")
            return print(self.field)
        else:
            self.field.field_validation(value_one, value_two)
            self.turn_player()