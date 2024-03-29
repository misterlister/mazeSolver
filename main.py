from graphics import Window, window_width, window_height
from maze import Maze
from controls import Controls
from tkinter import Tk


if __name__ == "__main__":
    maze_width = None
    maze_height = None
    root = Tk()
    window = Window(window_width, window_height, root)
    maze = Maze(window, root)
    controls = Controls(window, maze, root)
    window.wait_for_close()