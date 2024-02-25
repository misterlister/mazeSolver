from graphics import Point
from cell import Cell
import time
import random



class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window = None,
            seed = None
                 ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        if seed is not None:
            random.seed(seed)
        self._cells = []
        self.__drawn = False
        
    
    def _create_cells(self):
        for i in range (self.num_rows):
            self._cells.append([])
            for j in range (self.num_cols):
                p1 = Point((self.cell_size_x * j) + self.x1, (self.cell_size_y * i) + self.y1)
                p2 = Point((self.cell_size_x * (j+1)) + self.x1, (self.cell_size_y * (i+1)) + self.y1)
                self._cells[i].append(Cell(p1, p2, self.window))
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self.window is not None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.0005)

    def _break_entrance_and_exit(self):
        if len(self._cells) > 0:
            if len(self._cells[0]) > 0:
                self._cells[0][0].has_top_wall = False
                self._draw_cell(0, 0)
                self._cells[-1][-1].has_bottom_wall = False
                self._draw_cell(-1, -1)
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i-1 >= 0:
                if self._cells[i-1][j].visited != True:
                    to_visit.append((i-1,j))
            if j-1 >= 0:
                if self._cells[i][j-1].visited != True:
                    to_visit.append((i,j-1))
            if i+1 < self.num_rows:
                if self._cells[i+1][j].visited != True:
                    to_visit.append((i+1,j))
            if j+1 < self.num_cols:
                if self._cells[i][j+1].visited != True:
                    to_visit.append((i,j+1))
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            choice = random.randrange(len(to_visit))
            if to_visit[choice][0] != i:
                if to_visit[choice][0] < i:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i-1][j].has_bottom_wall = False
                else:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i+1][j].has_top_wall = False
            else:
                if to_visit[choice][1] < j:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i][j-1].has_right_wall = False
                else:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i][j+1].has_left_wall = False
            self._break_walls_r(to_visit[choice][0], to_visit[choice][1])

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        if self.__drawn:
            return self._solve_r(0,0)
        else:
            pass
    
    def _solve_r(self, i, j):
        current_cell = self._cells[i][j]
        self._animate()
        current_cell.visited = True
        if i == (self.num_rows-1) and j == (self.num_cols-1):
            return True
        if current_cell.has_top_wall is False:
            if i-1 >= 0:
                up_cell = self._cells[i-1][j]
                if up_cell.visited == False:
                    current_cell.draw_move(up_cell)
                    if self._solve_r(i-1, j):
                        return True
                    else:
                        current_cell.draw_move(up_cell, True)
        if current_cell.has_left_wall is False:
            if j-1 >= 0:
                left_cell = self._cells[i][j-1]
                if left_cell.visited == False:
                    current_cell.draw_move(left_cell)
                    if self._solve_r(i, j-1):
                        return True
                    else:
                        current_cell.draw_move(left_cell, True)
        if current_cell.has_right_wall is False:
            if j+1 < self.num_rows:
                right_cell = self._cells[i][j+1]
                if right_cell.visited == False:
                    current_cell.draw_move(right_cell)
                    if self._solve_r(i, j+1):
                        return True
                    else:
                        current_cell.draw_move(right_cell, True)
        if current_cell.has_bottom_wall is False:
            if i+1 < self.num_cols:
                down_cell = self._cells[i+1][j]
                if down_cell.visited == False:
                    current_cell.draw_move(down_cell)
                    if self._solve_r(i+1, j):
                        return True
                    else:
                        current_cell.draw_move(down_cell, True)
        return False
    
    def clear(self):
        self.__drawn = False
        pass

    def draw(self):
        self.clear()
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self.__drawn = True