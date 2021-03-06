import copy
from typing import List, Dict, Tuple


class Rectangle:
    """Class of objects, which break up field"""
    def __init__(self, square, height, width, correct_i=0, correct_j=0):
        self.square = square
        self.height = height
        self.width = width
        self.pos_i = correct_i
        self.pos_j = correct_j
        self.id = -1

    def __str__(self) -> str:
        return f'{self.square}, {self.height}, {self.width}, ' \
               f'{self.pos_i}, {self.pos_j}'

    def __repr__(self) -> str:
        return f'{self.height},{self.width}; {self.id}' \
               f':({self.pos_i}, {self.pos_j})'

    def __eq__(self, other) -> bool:
        h_is_eq = self.height == other.height
        w_is_eq = self.width == other.width
        i_is_eq = self.pos_i == other.pos_i
        j_is_eq = self.pos_j == other.pos_j
        return h_is_eq and w_is_eq and i_is_eq and j_is_eq

    def is_correct(self, field, x, y) -> bool:
        """Check correctness of the rectangle in field
        on position (x,y)"""
        digit = True
        for i in range(self.height):
            if i + x >= len(field) or i + x < 0:
                return False
            for j in range(self.width):
                if j + y < 0 or j + y >= len(field[i]):
                    return False
                if field[i+x][j+y] == '-':
                    continue
                if field[i+x][j+y].isdigit() and digit:
                    digit = False
                    continue
                else:
                    return False
        return True

    def find_correct_positions(self, field: list, i: int, j: int):
        """find all positions, where the rectangle is correct
        and returns rectangles with correct positions"""
        result = []
        for k in range(-self.height + 1, 1):
            for m in range(-self.width + 1, 1):
                if self.is_correct(field, i+k, j+m):
                    result.append(Rectangle(self.square,
                                            self.height,
                                            self.width, k+i, m+j))
        return result


def field_is_correct(field: List[List[str]]):
    """check that the field is rectangular"""
    width = -1
    for i in range(len(field)):
        if width == -1:
            width = len(field[i])
        else:
            if width != len(field[i]):
                return False
    return True


def field_update(field: List[List[str]], rectangle: Rectangle):
    """change field`s components to '+' on all positions
    of the rectangle"""
    width, height = rectangle.width, rectangle.height
    i = rectangle.pos_i
    j = rectangle.pos_j
    for k in range(height):
        for m in range(width):
            field[i + k][j + m] = '+'
    return field


def has_digit(field):
    """check that the field has digit
    (if field has not digit then it is solved or has not solution)"""
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j].isdigit():
                return True
    return False


def is_solved(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] != '+':
                return False
    return True


def get_rectangles(field: List[List[str]])\
        -> Dict[int, List[Rectangle]]:
    """get all possible rectangles on this field"""
    rectangles = {}
    if type(field[0]) is list:
        width = len(field[0])
    else:
        width = 1
    for i in range(len(field)):
        for j in range(width):
            square = (i+1)*(j+1)
            if square in rectangles.keys():
                rectangles[square].append(Rectangle(square, i+1, j+1))
            else:
                rectangles[square] = [Rectangle(square, i+1, j+1)]
    return rectangles


def find_solve(rectangles: Dict[int, List[Rectangle]],
               stack: List[Tuple[List[List[str]], list]])\
        -> List[List[Rectangle]]:
    """use to brute-force algorithm to
    find all solutions on this field;
    stack is tuple of current field and current solve"""
    result = []
    while stack:
        g, solve = stack.pop(0)
        rectangle_id = len(solve)
        if not has_digit(g):
            if is_solved(g):
                result.append(solve)
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j].isdigit():
                    sq = int(g[i][j])
                    for e in rectangles[sq]:
                        correct_rectangles = e.find_correct_positions(g, i, j)
                        for rectangle in correct_rectangles:
                            h = copy.deepcopy(solve)
                            rectangle.id = rectangle_id
                            h.append(rectangle)
                            new_field = field_update(copy.deepcopy(g),
                                                     rectangle)
                            stack.insert(0, (new_field, h))
                    break
                else:
                    continue
            else:
                continue
            break
    return result


def prepare_to_print_solve(field: List[List[str]], solve: List[Rectangle])\
        -> str:
    """form understandable solution`s output"""
    for r in solve:
        for i in range(r.height):
            for j in range(r.width):
                field[r.pos_i + i][r.pos_j + j] = str(r.id)
    temp = alignment_solve(field)
    result = [' '.join(s) for s in temp]
    return '\n'.join(result)


def alignment_solve(tmp: List[List[str]]) -> List[List[str]]:
    """aligns understandable solution`s output"""
    for j in range(1, len(tmp[0]) + 1):
        size = len(tmp[-1][-j])
        for i in range(2, len(tmp) + 1):
            if len(tmp[-i][-j]) < size:
                tmp[-i][-j] = ' ' * (size - len(tmp[-i][-j])) + tmp[-i][-j]
    return tmp


def main(file='in.txt'):
    try:
        f = open(file, 'r')
        puzzle = [s.split(' ') for s in f.read().split('\n')]
        if not field_is_correct(puzzle):
            f.close()
            raise Warning
        figures = get_rectangles(puzzle)
        solves = find_solve(figures, [(puzzle, [])])
        result = ''
        for s in solves:
            result = result + \
                     prepare_to_print_solve(copy.deepcopy(puzzle),
                                            s) + '\n'
        if len(solves) == 0:
            return 'Field has not solve'
        f.close()
        return result
    except FileNotFoundError:
        return 'File with field is not found'
    except Warning:
        return 'Field is not rectangular'


if __name__ == '__main__':
    print(main())
