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
            5,
            5,
            25,
            25,
            window
            )
    controls = Controls(window, maze, root)

    while window.running:
        print (maze.num_cols)
        window.redraw()