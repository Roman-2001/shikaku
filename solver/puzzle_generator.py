from typing import List, Tuple
import random
import solver.solution as solution


def generate_field(height: int, width: int)\
        -> List[Tuple[int, int, int]]:
    """choose numbers and its positions randomly"""
    field = [['-' for j in range(width)] for i in range(height)]
    available_square = height*width
    all_rectangles = [solution.Rectangle((i+1)*(j+1), i+1, j+1)
                      for i in range(height) for j in range(width)]
    rectangles = {}
    for e in all_rectangles:
        if e.square in rectangles.keys():
            rectangles[e.square].append(e)
        else:
            rectangles[e.square] = [e]
    result = []
    while available_square > 0:
        current_square = random.randint(1, available_square)
        if current_square in rectangles.keys():
            i = random.randint(0, height - 1)
            j = random.randint(0, width - 1)
            index = random.randint(0, len(rectangles[current_square])-1)
            rectangle = rectangles[current_square][index]
            correct_rectangles = rectangle.find_correct_positions(field, i, j)
            if len(correct_rectangles) > 0:
                solution.field_update(field, correct_rectangles[0])
                result.append((current_square, i, j))
                available_square -= current_square
    return result


def make_field(solve: List[Tuple[int, int, int]],
               height: int, width: int) -> List[List[str]]:
    """set numbers for positions in field"""
    field = [['-' for i in range(width)] for j in range(height)]
    for t in solve:
        sq, i, j = t
        field[i][j] = str(sq)
    return field


if __name__ == '__main__':
    h, w = 1, 1
    try:
        h = int(input('Enter height: '))
        w = int(input('Enter width: '))
    except ValueError as e:
        h, w = 1, 1
        print(f'{e} is not number\nheight = 1, width = 1 on default')
    s = generate_field(h, w)
    f = make_field(s, h, w)
    print(f)
    rect = solution.get_rectangles(f)
    solves = solution.find_solve(rect, [(f, [])])
    for sol in solves:
        print(solution.prepare_to_print_solve(f, sol))
