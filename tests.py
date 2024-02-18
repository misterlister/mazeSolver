import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Maze Create Fail Cols"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
            "Maze Create Fail Rows"
        )
    
    def test_maze_zero_cols(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Maze Zero Cells Fail Cols"
        )

    def test_maze_zero_rows(self):
        num_cols = 1
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Maze Zero Rows Fail Cols"
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
            "Maze Zero Rows Fail"
        )


    def test_maze_zero_size(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 0, 0)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Maze Zero Size Fail Cols"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
            "Maze Zero Size Fail Rows"
        )

    def test_maze_big(self):
        num_cols = 1000
        num_rows = 1000
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Maze Big Fail Cols"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
            "Maze Big Fail Rows"
        )

    def test_maze_offset(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(1000, 1000, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
            "Maze Offset Fail Cols"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
            "Maze Offset Fail Rows"
        )


if __name__ == "__main__":
    unittest.main()