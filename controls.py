from tkinter import Button


class Controls:
    def __init__(self, window, maze, root) -> None:
        self.window = window
        self.master = root
        self.maze = maze
        self.small = 10
        self.medium = 15
        self.large = 20
        self.xlarge = 25
        #sm_maze_height_btn = Button(self.master, text = "Small Height", command = self.small_height)
        #sm_maze_width_btn = Button(self.master, text = "Small Width", command = self.small_width)
        solve_btn = Button(self.master, text = "Solve", borderless = 1, command = self.solve)

        solve_btn.place(x=1100, y=200)
        
    def small_height(self):
        self.maze.num_rows = self.small

    def small_width(self):
        self.maze.num_cols = self.small

    def solve(self):
        self.maze.solve()