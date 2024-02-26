from tkinter import Button, Label
from graphics import bg_col, divider, window_width

# Colours used for control buttons
button_col = '#add8e6'
highlight_col = '#8bb6c4'

# Spacing between each button
btn_spacing = 45

# Positions of the control buttons
btn_pos_1 = int(((window_width - divider) * (1/4)) + divider)
btn_pos_2 = int(((window_width - divider) * (2/4)) + divider)
btn_pos_mid = int(((window_width - divider) * (1/3)) + divider)

# Labels for the currently selected maze dimensions
height_label = "Maze Height: "
width_label = "Maze Width: "



class Controls:
    def __init__(self, window, maze, root) -> None:
        self.window = window
        self.master = root
        self.maze = maze
        self.small = 12
        self.medium = 18
        self.large = 24
        self.xlarge = 30

        self.sm_height_btn = Button(root, text = "Small", highlightbackground=bg_col, command = lambda: self.maze_height(self.small), background=button_col, activebackground=highlight_col)
        self.med_height_btn = Button(root, text = "Medium", highlightbackground=bg_col, command = lambda: self.maze_height(self.medium), background=button_col, activebackground=highlight_col)
        self.lg_height_btn = Button(root, text = "Large", highlightbackground=bg_col, command = lambda: self.maze_height(self.large), background=button_col, activebackground=highlight_col)
        self.x_lg_height_btn = Button(root, text = "X-Large", highlightbackground=bg_col, command = lambda: self.maze_height(self.xlarge), background=button_col, activebackground=highlight_col)
        
        self.sm_width_btn = Button(root, text = "Small", highlightbackground=bg_col, command = lambda: self.maze_width(self.small), background=button_col, activebackground=highlight_col)
        self.med_width_btn = Button(root, text = "Medium", highlightbackground=bg_col, command = lambda: self.maze_width(self.medium), background=button_col, activebackground=highlight_col)
        self.lg_width_btn = Button(root, text = "Large", highlightbackground=bg_col, command = lambda: self.maze_width(self.large), background=button_col, activebackground=highlight_col)
        self.x_lg_width_btn = Button(root, text = "X-Large", highlightbackground=bg_col, command = lambda: self.maze_width(self.xlarge), background=button_col, activebackground=highlight_col)

        self.draw_btn = Button(root, text = "Draw Maze", highlightbackground=bg_col, command = maze.draw, background=button_col, activebackground=highlight_col)
        self.solve_btn = Button(root, text = "Solve", highlightbackground=bg_col, command = self.solve, background=button_col, activebackground=highlight_col)
        self.clear_btn = Button(root, text = "Clear", highlightbackground=bg_col, command = maze.clear, background=button_col, activebackground=highlight_col)

        self.height_text = Label(root, text="Height:", fg="black", background=bg_col, font=('Arial', 24, 'bold'))
        self.height_text.place(x=btn_pos_mid, y=btn_spacing * 1)
        self.sm_height_btn.place(x=btn_pos_1, y=btn_spacing * 2)
        self.med_height_btn.place(x=btn_pos_2, y=btn_spacing * 2)
        self.lg_height_btn.place(x=btn_pos_1, y=btn_spacing * 3)
        self.x_lg_height_btn.place(x=btn_pos_2, y=btn_spacing * 3)

        self.width_text = Label(root, text="Width:", fg="black", background=bg_col, font=('Arial', 24, 'bold'))
        self.width_text.place(x=btn_pos_mid, y=btn_spacing * 5)
        self.sm_width_btn.place(x=btn_pos_1, y=btn_spacing * 6)
        self.med_width_btn.place(x=btn_pos_2, y=btn_spacing * 6)
        self.lg_width_btn.place(x=btn_pos_1, y=btn_spacing * 7)
        self.x_lg_width_btn.place(x=btn_pos_2, y=btn_spacing * 7)

        self.draw_btn.place(x=btn_pos_mid, y=btn_spacing * 9)
        self.solve_btn.place(x=btn_pos_mid, y=btn_spacing * 10)
        self.clear_btn.place(x=btn_pos_mid, y=btn_spacing * 11)

        
        
    def maze_height(self, size):
        self.maze.num_rows = size
        self.maze.current_height.config(text=height_label + str(size))
        
    def maze_width(self, size):
        self.maze.num_cols = size
        self.maze.current_width.config(text=width_label + str(size))

    def solve(self):
        self.maze.solve()