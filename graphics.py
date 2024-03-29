from tkinter import BOTH, Canvas

# Colour used for the background of the window
bg_col = '#d9d9d9'

# Dimensions for the application window
window_width = 1200
window_height = 900

# X-position of the divider between maze window and control window
divider = window_width * (3/4)

class Window:
    def __init__(self, width_val, height_val, root) -> None:
        self.__root = root
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width_val}x{height_val}")
        self.__root.configure(background=bg_col)
        self.canvas = Canvas(self.__root)
        self.canvas.pack(fill=BOTH, expand=1)
        self.canvas.configure(background=bg_col)
        self.dividing_line()
        self.running = True
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        
    def close(self):
        self.running = False

    def draw_line(self, line, fill_colour = "black"):
        line.draw(self.canvas, fill_colour)

    def dividing_line(self):
        p1 = Point(divider, 0)
        p2 = Point(divider, window_height)
        dividing_line = Line(p1, p2)
        self.draw_line(dividing_line)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, colour):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=colour, width=2
        )
        canvas.pack()

