import copy


class Rectangle:
    def __init__(self, square, height, width, correct_x=0, correct_y=0):
        self.square = square
        self.height = height
        self.width = width
        self.pos_x = correct_x
        self.pos_y = correct_y

    def __str__(self):
        return f'{self.square},{self.height},{self.width}'

    def __repr__(self):
        return f'{self.height},{self.width}:({self.pos_x}, {self.pos_y})'

    def is_correct(self, field, x, y):
        digit = True
        for i in range(self.height):
            if i + x >= len(field) or i + x < 0:
                return False
            for j in range(self.width):
                if j + y < 0 or j + y >= len(field):
                    return False
                if field[i+x][j+y] == '-':
                    continue
                if field[i+x][j+y].isdigit() and digit:
                    digit = False
                    continue
                else:
                    return False
        return True

    def find_correct_positions(self, field, i, j):
        result = []
        for k in range(-self.height + 1, 1):
            for m in range(-self.width + 1, 1):
                if self.is_correct(field, i+k, j+m):
                    result.append(Rectangle(self.square,
                                            self.height,
                                            self.width, k+i, m+j))
        return result


def field_update(field, rectangle, i, j):
    width, height = rectangle.width, rectangle.height
    for k in range(height):
        for m in range(width):
            field[i + k][j + m] = '+'
    return field


def has_digit(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j].isdigit():
                return True
    return False


def is_solved(field):
    for i in range(len(field)):
        for j in range(len(field)):
            if field[i][j] != '+':
                return False
    return True


def get_rectangles(field_size):
    rectangles = {}
    for i in range(field_size):
        for j in range(field_size):
            square = (i+1)*(j+1)
            if square in rectangles.keys():
                rectangles[square].append(Rectangle(square, i+1, j+1))
            else:
                rectangles[square] = [Rectangle(square, i+1, j+1)]
    return rectangles


def find_solve(rectangles, stack):
    while stack:
        g, solve = stack.pop(0)
        if not has_digit(g):
            if is_solved(g):
                print(g)
                print(is_solved(g))
                print(solve)
        for i in range(len(g)):
            for j in range(len(g)):
                if g[i][j].isdigit():
                    sq = int(g[i][j])
                    for e in rectangles[sq]:
                        correct_rectangles = e.find_correct_positions(g, i, j)
                        if len(correct_rectangles) > 0:
                            for rectangle in correct_rectangles:
                                h = copy.deepcopy(solve)
                                h.append(rectangle)
                                new_field = field_update(copy.deepcopy(g),
                                                         rectangle,
                                                         rectangle.pos_x,
                                                         rectangle.pos_y)
                                stack.insert(0, (new_field, h))
                    break
                else:
                    continue
            else:
                continue
            break


if __name__ == '__main__':
    with open('in.txt', 'r') as file:
        puzzle = file.read().split('\n')
        puzzle = [s.split(' ') for s in puzzle]
    figures = get_rectangles(len(puzzle))
    find_solve(figures, [(puzzle, [])])
