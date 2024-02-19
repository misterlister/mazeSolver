import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "Maze creation error: rows"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
            "Maze creation error: columns"
        )
        
    
    def test_maze_zero_cols(self):
        num_rows = 0
        num_cols = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "Maze with zero rows error"
        )

    def test_maze_zero_rows(self):
        num_rows = 1
        num_cols = 0
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "Maze with zero columns: row error"
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
            "Maze with zero columns: column error"
        )

        

    def test_maze_zero_size(self):
        num_rows = 10
        num_cols = 10
        m1 = Maze(0, 0, num_rows, num_cols, 0, 0)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "Maze with size of zero: row error"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
            "Maze with size of zero: column error"
        )
        
    def test_maze_big(self):
        num_rows = 999
        num_cols = 999
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "Maze 999x999: row error"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
            "Maze 999x999: column error"
        )
        

    def test_maze_offset(self):
        num_rows = 5
        num_cols = 5
        m1 = Maze(999, 999, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
            "Maze with 999 offset: row error"
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
            "Maze with 999 offset: column error"
        )


    def test_maze_entrance(self):
        num_rows = 5
        num_cols = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1._cells[0][0].has_top_wall,
            "Maze 5x5 entrance test error"
        )

    def test_maze_entrance(self):
        num_rows = 1
        num_cols = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1._cells[0][0].has_top_wall,
            "Maze 1x1 entrance test error"
        )

    def test_maze_entrance(self):
        num_rows = 5
        num_cols = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1._cells[4][4].has_bottom_wall,
            "Maze 5x5 exit test error"
        )

    def test_maze_entrance(self):
        num_rows = 1
        num_cols = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(
            m1._cells[0][0].has_bottom_wall,
            "Maze 1x1 exit test error"
        )
        
    def reset_visited_test(self):
        num_rows = 5
        num_cols = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0)
        m1._reset_cells_visited()
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertFalse(
                    m1._cells[i][j].visited,
                    f"Maze 5x5 reset visited error: row {i}, column {j}"
        )
        


if __name__ == "__main__":
    unittest.main()