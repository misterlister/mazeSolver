from graphics import Point
from cell import Cell
import time



class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window = None
                 ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._cells = []
        self._create_cells()
    
    def _create_cells(self):
        for i in range (self.num_cols):
            self._cells.append([])
            for j in range (self.num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        p1 = Point((self.cell_size_x * j) + self.x1, (self.cell_size_y * i) + self.y1)
        p2 = Point((self.cell_size_x * (j+1)) + self.x1, (self.cell_size_y * (i+1)) + self.y1)
        self._cells[i].append(Cell(p1, p2, self.window))
        if self.window is not None:
            self._cells[i][j].draw()
            self._animate()
    def _animate(self):
        self.window.redraw()
        time.sleep(0.02)