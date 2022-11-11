from typing import List, Generator
from pprint import pprint
from copy import deepcopy


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


class BoardNumber:
    def __init__(self, number) -> None:
        self.number = number
        self.marked = False

    def __repr__(self) -> str:
        return ("m" if self.marked else "u") + f"{self.number:02d}"

    def __bool__(self) -> bool:
        return self.marked

    def __radd__(self, other):
        if isinstance(other, int):
            return self.number + other
        return self.number + other.number

class Board:
    def __init__(self, board: List[List[int]]) -> None:
        self.board = [[BoardNumber(number) for number in row] for row in board]
        self.raw_board = board
        self.marked = []

    def __eq__(self, __o: object) -> bool:
        return self.raw_board == __o.raw_board # type: ignore

    def iterate(self) -> Generator[BoardNumber, None, None]:
        for row in self.board:
            for num in row:
                yield num

    def mark(self, number):

        for board_number in self.iterate():
            if number == board_number.number:
                board_number.marked = True
                self.marked.append(number)
                return True
        return False

    def check_win(self):

        # Check if a row is marked
        for row in self.board:
            if all(row):
                return True

        # Check if a column is marked
        for column in [[row[i] for row in self.board] for i in range(0, len(self.board[0]))]:
            if all(column):
                return True

        return False

with open("Inputs/4.txt") as f:
    lines = f.readlines()

boards: List[Board] = []
numbers = list(map(lambda x: int(x), lines[0].split(",")))
lines = list(filter(lambda x: x != "\n", lines[2:]))

for b in chunks(lines, 5):
    board = []
    for l in b:
        row = []
        for j in range(0, len(l.strip()), 3):
            row.append(int((l[j] + l[j + 1]).strip()))
        board.append(row)

    boards.append(Board(board))

boards2 = deepcopy(boards)
winner = False

for number in numbers:

    for board in boards:
        board.mark(number)
        if board.check_win():
            winner = board
            break
    if winner:
        break

assert winner

score = sum(filter(lambda x: not x.marked, winner.iterate())) * winner.marked[-1]
pprint(winner.board)
print(score)

# Part 2

winner = False
# boards2 = [
#     Board(
#         [
#             [22, 13, 17, 11, 0],
#             [8, 2, 23, 4, 24],
#             [21, 9, 14, 16, 7],
#             [6, 10, 3, 18, 5],
#             [1, 12, 20, 15, 19],
#         ]
#     ),
#     Board(
#         [
#             [3, 15, 0, 2, 22],
#             [9, 18, 13, 17, 5],
#             [19, 8, 7, 25, 23],
#             [20, 11, 10, 24, 4],
#             [14, 21, 16, 12, 6],
#         ]
#     ),
#     Board(
#         [
#             [14, 21, 17, 24, 4],
#             [10, 16, 15, 9, 19],
#             [18, 8, 23, 26, 20],
#             [22, 11, 13, 6, 5],
#             [2, 0, 12, 3, 7],
#         ]
#     ),
# ]
# numbers = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
unwon_boards = deepcopy(boards2)

for number in numbers:
    for board in boards2:
        if board.check_win(): continue
        board.mark(number)
        if board.check_win():
            if len(unwon_boards) == 1:
                winner = board
                break
            unwon_boards.remove(board)

    if winner:
        break

assert winner

score = sum(filter(lambda x: not x.marked, winner.iterate())) * winner.marked[-1]
pprint(winner.board)
print(score)
