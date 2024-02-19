from graphics import Window
from maze import Maze


if __name__ == "__main__":
    window = Window(1000, 800)
    maze = Maze(
            5,
            5,
            25,
            25,
            25,
            25,
            window
            )
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    maze.solve()
    window.wait_for_close()