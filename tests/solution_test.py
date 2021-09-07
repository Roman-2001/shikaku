import unittest
import solver.solution as solution


class TestSolution(unittest.TestCase):
    def test_field_has_digit(self):
        field = [['2', '-'],
                 ['-', '2']]
        self.assertTrue(solution.has_digit(field))

    def test_field_has_not_digit(self):
        field = [['+', '+'],
                 ['+', '+']]
        self.assertFalse(solution.has_digit(field))

    def test_field_is_solved(self):
        field = [['+', '+'],
                 ['+', '+']]
        self.assertTrue(solution.is_solved(field))

    def test_field_is_not_solved(self):
        field = [['2', '-'],
                 ['-', '2']]
        self.assertFalse(solution.is_solved(field))

    def test_rectangle_is_correct(self):
        field = [['2', '2'],
                 ['-', '-']]
        rectangle = solution.Rectangle(2, 2, 1, 0, 0)
        self.assertTrue(solution.Rectangle.is_correct(rectangle, field, 0, 0))

    def test_rectangle_is_not_correct(self):
        field = [['2', '2'],
                 ['-', '-']]
        rectangle = solution.Rectangle(2, 1, 2, 0, 0)
        self.assertFalse(solution.Rectangle.is_correct(rectangle, field, 0, 0))

    def test_rectangle_find_correct_position(self):
        field = [['2', '2'],
                 ['-', '-']]
        pos_i = 0
        pos_j = 1
        rectangle = solution.Rectangle(2, 2, 1, 0, 0)
        result = solution.Rectangle.find_correct_positions(rectangle, field, pos_i, pos_j)
        expected_answer = [solution.Rectangle(2, 2, 1, 0, 1)]
        self.assertEqual(expected_answer, result)

    def test_field_update(self):
        field = [['2', '2'],
                 ['-', '-']]
        rectangle = solution.Rectangle(2, 2, 1, 0, 1)
        expected_answer = [['2', '+'],
                           ['-', '+']]
        self.assertEqual(expected_answer, solution.field_update(field, rectangle))

    def test_get_rectangles(self):
        field = [['2', '2'],
                 ['-', '-']]
        expected_answer = {1: [solution.Rectangle(1, 1, 1)],
                           2: [solution.Rectangle(2, 1, 2), solution.Rectangle(2, 2, 1)],
                           4: [solution.Rectangle(4, 2, 2)]}
        self.assertCountEqual(expected_answer, solution.get_rectangles(len(field)))

    def test_find_one_solve(self):
        field = [['2', '2'],
                 ['-', '-']]
        stack = [(field, [])]
        rectangles = solution.get_rectangles(len(field))
        expected_answer = [[solution.Rectangle(2, 2, 1, 0, 0), solution.Rectangle(2, 2, 1, 0, 1)]]
        self.assertCountEqual(expected_answer, solution.find_solve(rectangles, stack))

    def test_find_many_solve(self):
        field = [['2', '-'],
                 ['-', '2']]
        stack = [(field, [])]
        rectangles = solution.get_rectangles(len(field))
        expected_answer = [[solution.Rectangle(2, 2, 1, 0, 0), solution.Rectangle(2, 2, 1, 0, 1)],
                           [solution.Rectangle(2, 1, 2, 0, 0), solution.Rectangle(2, 1, 2, 1, 0)]]
        self.assertCountEqual(expected_answer, solution.find_solve(rectangles, stack))

    def test_find_no_solve(self):
        field = [['2', '2'],
                 ['-', '2']]
        stack = [(field, [])]
        rectangles = solution.get_rectangles(len(field))
        self.assertEqual([], solution.find_solve(rectangles, stack))


if __name__ == '__main__':
    unittest.main()
