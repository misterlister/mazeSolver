from tkinter import Button
from graphics import bg_col

button_col = '#add8e6'

class Controls:
    def __init__(self, window, maze, root) -> None:
        self.window = window
        self.master = root
        self.maze = maze
        self.small = 10
        self.medium = 15
        self.large = 20
        self.xlarge = 25
        self.sm_height_btn = Button(self.master, text = "Small Height", highlightbackground=bg_col, command = lambda: self.maze_height(self.small), background=button_col, activebackground='blue')
        self.sm_width_btn = Button(self.master, text = "Small Width", highlightbackground=bg_col, command = lambda: self.maze_width(self.small), background=button_col, activebackground='blue')
        self.med_height_btn = Button(self.master, text = "Medium Height", highlightbackground=bg_col, command = lambda: self.maze_height(self.medium), background=button_col, activebackground='blue')
        self.med_width_btn = Button(self.master, text = "Medium Width", highlightbackground=bg_col, command = lambda: self.maze_width(self.medium), background=button_col, activebackground='blue')
        self.draw_btn = Button(self.master, text = "Draw Maze", highlightbackground=bg_col, command = maze.draw, background=button_col, activebackground='blue')
        self.solve_btn = Button(self.master, text = "Solve", highlightbackground=bg_col, command = self.solve, background=button_col, activebackground='blue')
        self.clear_btn = Button(self.master, text = "Clear", highlightbackground=bg_col, command = maze.clear, background=button_col, activebackground='blue')
        self.sm_height_btn.place(x=1050, y=20)
        self.sm_width_btn.place(x=1050, y=60)
        self.med_height_btn.place(x=1050, y=100)
        self.med_width_btn.place(x=1050, y=140)
        self.draw_btn.place(x=1050, y=180)
        self.solve_btn.place(x=1050, y=220)
        self.clear_btn.place(x=1050, y=260)
        
        
    def maze_height(self, size):
        self.maze.num_rows = size

    def maze_width(self, size):
        self.maze.num_cols = size

    def solve(self):
        self.maze.solve()