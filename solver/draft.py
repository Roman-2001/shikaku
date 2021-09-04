import copy


def get_field(file):
    with open(file, 'r') as f:
        field = f.read().split('\n')
    return [e.split(' ') for e in field]


def get_rectangles(field_size):
    figures = {}
    for i in range(field_size):
        for j in range(field_size):
            square = (i+1)*(j+1)
            if square in figures.keys():
                figures[square].append((j+1, i+1))
            else:
                figures[square] = [(j+1, i+1)]
    return figures


def figure_is_correct(field, rectangle, i, j):
    digit = True
    width, height = rectangle
    for k in range(width):
        if k+i >= len(field) or k+i < 0:
            # print(0)
            return False
        for l in range(height):
            if l+j < 0 or l+j >= len(field):
                # print(1)
                return False
            if field[k+i][l+j] == '-':
                continue
            if field[k+i][l+j].isdigit() and digit:
                digit = False
                continue
            else:
                return False
    # print(k, l, i, j)
    return True


def find_correct_position(field, figure, i, j):
    width, height = figure
    for m in range(-width+1, 1):
        for n in range(-height+1, 1):
            if figure_is_correct(field, figure, m+i, n+j):
                # update(field, figure, m+i, n+j)
                return m, n


def update(field, figure, i, j):
    width, height = figure
    for k in range(width):
        for l in range(height):
            field[i+k][j+l] = '+'
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


if __name__ == '__main__':
    f = get_field('in.txt')
    r = get_rectangles(len(f))
    print(f)
    stack = [f]
    while stack:
        g = stack.pop(0)
        # print(g)
        if not has_digit(g):
            if is_solved(g):
                print(g)
                print(is_solved(g))
        for i in range(len(g)):
            for j in range(len(g)):
                if g[i][j].isdigit():
                    sq = int(g[i][j])
                    for e in r[sq]:
                        if find_correct_position(g, e, i, j) is not None:
                            figure_position_x, figure_position_y = find_correct_position(g, e, i, j)
                            stack.insert(0, update(copy.deepcopy(g), e, i+figure_position_x, j+figure_position_y))
                    break
                else:
                    continue
                # break
            else:
                continue
            break

        print(stack)
