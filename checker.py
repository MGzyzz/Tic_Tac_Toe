from field import Field


class Checker:

    def check_tie(self) -> bool:
        for cell in Field.FIELD:
            if "" in cell:
                return False
        else:
            print("НИЧЬЯ")
            return True

    def check_win(self, value: str) -> bool:
        if (Field.FIELD[0][0] == value and Field.FIELD[0][1] == value and Field.FIELD[0][2] == value) \
                or (Field.FIELD[1][0] == value and Field.FIELD[1][1] == value and Field.FIELD[1][2] == value)\
                or (Field.FIELD[2][0] == value and Field.FIELD[2][1] == value and Field.FIELD[2][2] == value):
            print(f"ПОБЕДИЛИ {value.upper()}")
            return True

        elif (Field.FIELD[0][0] == value and Field.FIELD[1][0] == value and Field.FIELD[2][0] == value) \
                or (Field.FIELD[0][1] == value and Field.FIELD[1][1] == value and Field.FIELD[2][1] == value)\
                or (Field.FIELD[0][2] == value and Field.FIELD[1][2] == value and Field.FIELD[2][2] == value):
            print(f"ПОБЕДИЛИ {value.upper()}")
            return True

        elif (Field.FIELD[0][0] == value and Field.FIELD[1][1] == value and Field.FIELD[2][2] == value) \
                or (Field.FIELD[0][2] == value and Field.FIELD[1][1] == value and Field.FIELD[2][0] == value):
            print(f"ПОБЕДИЛИ {value.upper()}")
            return True
        else:
            return False