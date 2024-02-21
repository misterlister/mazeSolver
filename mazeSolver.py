from graphics import Window
from maze import Maze
from controls import Controls
from tkinter import Tk


if __name__ == "__main__":
    maze_width = None
    maze_height = None
    root = Tk()
    window = Window(1200, 900, root)
    maze = Maze(
            5,
            5,
            15,
            15,
            25,
            25,
            window
            )
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    controls = Controls(window, maze, root)
    #maze.solve()
    window.wait_for_close()