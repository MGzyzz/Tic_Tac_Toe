class Field:
    __SIZE = 3
    FIELD = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]

    def make_step(self, x: int, y: int, mark: str):
        self.FIELD[y][x] = mark

    def print_header(self):
        result = ' '

        for i in range(self.__SIZE):
            result += f'{i:>4}'

        return result

    def print_body(self):
        result = ''
        for idx, row in enumerate(self.FIELD):
            row_as_list = map(lambda x: f'{x:^3}', row.copy())

            row_as_str = '|'.join(row_as_list)
            row_as_str = f'{idx:<3}{row_as_str}\n'

            if not idx == self.__SIZE - 1:
                row_as_str += f'{" " * 3}{"-" * (self.__SIZE * 4 - 1)}\n'

            result += row_as_str

        return result

    def __str__(self) -> str:
        header = self.print_header()
        body = self.print_body()
        return f'{header}\n{body}'

    def field_validation(self, a, b):
        if self.FIELD[b][a] == '':
            return True

    def error(self, a: int, b: int):
        try:
            if (isinstance(a, str) or isinstance(b, str)) or a > 2 or b > 2 or self.FIELD[b][a] != '':
                raise ValueError("Клетка занята или не существует")
        except ValueError as e:
            print(e)

    def return_of_the_playing_field(self):
        for i in self.FIELD:
            if not ("" in i) or "" in i:
                for j in range(len(self.FIELD)):
                    for k in range(len(self.FIELD[j])):
                        self.FIELD[j][k] = ''
