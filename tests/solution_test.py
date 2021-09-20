import unittest
from solver.solution import Rectangle
import solver.solution as solution


class TestSolution(unittest.TestCase):
    def test_field_has_digit(self):
        f1 = [['2', '-'], ['-', '2']]
        f2 = [['+', '+'], ['+', '+']]
        self.assertTrue(solution.has_digit(f1))
        self.assertFalse(solution.has_digit(f2))

    def test_field_is_solved(self):
        f1 = [['+', '+'], ['+', '+']]
        f2 = [['2', '-'], ['-', '2']]
        self.assertTrue(solution.is_solved(f1))
        self.assertFalse(solution.is_solved(f2))

    def test_rectangle_is_correct(self):
        f = [['2', '2'],
                 ['-', '-']]
        r1 = Rectangle(2, 2, 1, 0, 0)
        r2 = Rectangle(2, 1, 2, 0, 0)
        self.assertTrue(solution.Rectangle.is_correct(r1,f, 0, 0))
        self.assertFalse(solution.Rectangle.is_correct(r2, f, 0, 0))

    def test_rectangle_find_correct_position(self):
        field = [['2', '2'],
                 ['-', '-']]
        pos_i = 0
        pos_j = 1
        rectangle = Rectangle(2, 2, 1, 0, 0)
        result = Rectangle.find_correct_positions(rectangle,
                                                           field,
                                                           pos_i, pos_j)
        expected_answer = [Rectangle(2, 2, 1, 0, 1)]
        self.assertEqual(expected_answer, result)

    def test_field_update(self):
        field = [['2', '2'],
                 ['-', '-']]
        rectangle = Rectangle(2, 2, 1, 0, 1)
        expected_answer = [['2', '+'],
                           ['-', '+']]
        self.assertEqual(expected_answer, solution.field_update(field,
                                                                rectangle))

    def test_get_rectangles(self):
        field = [['2', '2'],
                 ['-', '-']]
        expected_answer = {1: [Rectangle(1, 1, 1)],
                           2: [Rectangle(2, 1, 2),
                               Rectangle(2, 2, 1)],
                           4: [Rectangle(4, 2, 2)]}
        self.assertCountEqual(expected_answer, solution.get_rectangles(field))

    def test_find_one_solve(self):
        field = [['2', '2'],
                 ['-', '-']]
        stack = [(field, [])]
        rectangles = solution.get_rectangles(field)
        expected_answer = [[Rectangle(2, 2, 1, 0, 0),
                            Rectangle(2, 2, 1, 0, 1)]]
        self.assertCountEqual(expected_answer,
                              solution.find_solve(rectangles, stack))

    def test_find_many_solve(self):
        field = [['2', '-'],
                 ['-', '2']]
        stack = [(field, [])]
        rectangles = solution.get_rectangles(field)
        expected_answer = [[Rectangle(2, 2, 1, 0, 0),
                            Rectangle(2, 2, 1, 0, 1)],
                           [Rectangle(2, 1, 2, 0, 0),
                            Rectangle(2, 1, 2, 1, 0)]]
        self.assertCountEqual(expected_answer,
                              solution.find_solve(rectangles, stack))

    def test_find_no_solve(self):
        field = [['2', '2'],
                 ['-', '2']]
        stack = [(field, [])]
        rectangles = solution.get_rectangles(field)
        self.assertEqual([], solution.find_solve(rectangles, stack))

    def test_rectangles_eq(self):
        r1 = Rectangle(2, 1, 2, 0, 0)
        r2 = Rectangle(2, 2, 1, 0, 0)
        r3 = Rectangle(2, 2, 1, 0, 0)
        self.assertTrue(r2 == r3)
        self.assertFalse(r1 == r3)

    def test_rectangle2string(self):
        r = Rectangle(2,2,1,0,0)
        self.assertEqual(str(r), '2, 2, 1, 0, 0')

    def test_field_correct(self):
        f1 = [['2', '-'], ['-']]
        f2 = [['2', '-'], ['-', '-']]
        self.assertFalse(solution.field_is_correct(f1))
        self.assertTrue(solution.field_is_correct(f2))

    def test_alignment_solve(self):
        f = [['2', '2'], ['10', '1']]
        expected_ans = [[' 2', '2'], ['10', '1']]
        self.assertEqual(expected_ans, solution.alignment_solve(f))

    def test_prepare_to_print_solve(self):
        s = [Rectangle(2, 1, 2, 0, 0), Rectangle(2, 1, 2, 1, 0)]
        f = [['2', '-'],['2', '-']]
        expected_ans = '0 0\n1 1'
        s[0].id = 0
        s[1].id = 1
        self.assertEqual(expected_ans, solution.prepare_to_print_solve(f, s))

    def test_main(self):
        self.assertEqual('Field is not rectangular', solution.main('bad_field.txt'))
        self.assertEqual('File with field is not found', solution.main('1.txt'))


if __name__ == '__main__':
    unittest.main()
