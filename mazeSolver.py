from graphics import Window
from maze import Maze


if __name__ == "__main__":
    window = Window(800, 600)
    maze = Maze(
            10,
            10,
            30,
            20,
            20,
            20,
            window)
    window.wait_for_close()