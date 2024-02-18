from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width_val, height_val) -> None:
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width_val}x{height_val}")
        self.canvas = Canvas(self.__root, width=width_val, height=height_val)
        self.canvas.pack()
        self.running = False
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