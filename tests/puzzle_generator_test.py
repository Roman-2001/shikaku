import unittest
import solver.solution as slt
import solver.puzzle_generator as generator


class MyTestCase(unittest.TestCase):
    def test_make_field(self):
        rectangles = [(3, 0, 0),
                      (2, 0, 1),
                      (2, 1, 1),
                      (2, 1, 2)]
        width = 3
        height = 3
        expected_answer = [['3', '2', '-'],
                           ['-', '2', '2'],
                           ['-', '-', '-']]
        self.assertEqual(generator.make_field(rectangles,
                                              height, width),
                         expected_answer)

    def test_generate_solution(self):
        h, w = 1, 1
        self.assertEqual(generator.generate_field(h, w), [(1, 0, 0)])


if __name__ == '__main__':
    unittest.main()
