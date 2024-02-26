from tkinter import Button, Label
from graphics import bg_col, divider, window_width

button_col = '#add8e6'

btn_spacing = 40
btn_pos_1 = int(((window_width - divider) * (1/4)) + divider)
btn_pos_2 = int(((window_width - divider) * (2/4)) + divider)
btn_pos_mid = int(((window_width - divider) * (1/3)) + divider)

maze_height = "Maze Height: "
maze_width = "Maze Width: "

class Controls:
    def __init__(self, window, maze, root) -> None:
        self.window = window
        self.master = root
        self.maze = maze
        self.small = 12
        self.medium = 18
        self.large = 24
        self.xlarge = 30

        self.sm_height_btn = Button(root, text = "Small", highlightbackground=bg_col, command = lambda: self.maze_height(self.small), background=button_col, activebackground='blue')
        self.med_height_btn = Button(root, text = "Medium", highlightbackground=bg_col, command = lambda: self.maze_height(self.medium), background=button_col, activebackground='blue')
        self.lg_height_btn = Button(root, text = "Large", highlightbackground=bg_col, command = lambda: self.maze_height(self.large), background=button_col, activebackground='blue')
        self.x_lg_height_btn = Button(root, text = "X-Large", highlightbackground=bg_col, command = lambda: self.maze_height(self.xlarge), background=button_col, activebackground='blue')
        
        self.sm_width_btn = Button(root, text = "Small", highlightbackground=bg_col, command = lambda: self.maze_width(self.small), background=button_col, activebackground='blue')
        self.med_width_btn = Button(root, text = "Medium", highlightbackground=bg_col, command = lambda: self.maze_width(self.medium), background=button_col, activebackground='blue')
        self.lg_width_btn = Button(root, text = "Large", highlightbackground=bg_col, command = lambda: self.maze_width(self.large), background=button_col, activebackground='blue')
        self.x_lg_width_btn = Button(root, text = "X-Large", highlightbackground=bg_col, command = lambda: self.maze_width(self.xlarge), background=button_col, activebackground='blue')

        self.draw_btn = Button(root, text = "Draw Maze", highlightbackground=bg_col, command = maze.draw, background=button_col, activebackground='blue')
        self.solve_btn = Button(root, text = "Solve", highlightbackground=bg_col, command = self.solve, background=button_col, activebackground='blue')
        self.clear_btn = Button(root, text = "Clear", highlightbackground=bg_col, command = maze.clear, background=button_col, activebackground='blue')

        self.height_text = Label(root, text="Height:", fg="black", background=bg_col, font=('Arial', 28, 'bold'))
        self.height_text.place(x=btn_pos_mid, y=btn_spacing * 1)
        self.sm_height_btn.place(x=btn_pos_1, y=btn_spacing * 2)
        self.med_height_btn.place(x=btn_pos_2, y=btn_spacing * 2)
        self.lg_height_btn.place(x=btn_pos_1, y=btn_spacing * 3)
        self.x_lg_height_btn.place(x=btn_pos_2, y=btn_spacing * 3)

        self.width_text = Label(root, text="Width:", fg="black", background=bg_col, font=('Arial', 28, 'bold'))
        self.width_text.place(x=btn_pos_mid, y=btn_spacing * 5)
        self.sm_width_btn.place(x=btn_pos_1, y=btn_spacing * 6)
        self.med_width_btn.place(x=btn_pos_2, y=btn_spacing * 6)
        self.lg_width_btn.place(x=btn_pos_1, y=btn_spacing * 7)
        self.x_lg_width_btn.place(x=btn_pos_2, y=btn_spacing * 7)

        self.draw_btn.place(x=btn_pos_mid, y=btn_spacing * 9)
        self.solve_btn.place(x=btn_pos_mid, y=btn_spacing * 10)
        self.clear_btn.place(x=btn_pos_mid, y=btn_spacing * 11)

        self.current_height = Label(root, text=maze_height + "0", fg="black", background=bg_col, font=('Arial', 22, 'bold'))
        self.current_height.place(x=btn_pos_1, y=btn_spacing * 13)

        self.current_width = Label(root, text= maze_width + "0", fg="black", background=bg_col, font=('Arial', 22, 'bold'))
        self.current_width.place(x=btn_pos_1, y=btn_spacing * 15)
        
    def maze_height(self, size):
        self.maze.num_rows = size
        self.current_height.config(text=maze_height + str(size))
        

    def maze_width(self, size):
        self.maze.num_cols = size
        self.current_width.config(text=maze_width + str(size))

    def solve(self):
        self.maze.solve()