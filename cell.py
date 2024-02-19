from graphics import Point, Line

background_colour = "#d9d9d9"

class Cell:
    def __init__(self, p1, p2, window = None) -> None:
        self._topleft = Point(p1.x, p1.y)
        self._topright = Point(p2.x, p1.y)
        self._bottomleft = Point(p1.x, p2.y)
        self._bottomright = Point(p2.x, p2.y)
        self._centre = Point((p1.x+p2.x)/2, (p1.y+p2.y)/2)
        self._window = window
        self.has_top_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.visited = False

    
    def draw(self):
        colour = background_colour
        if self.has_top_wall:
            colour = "black"
        self._window.draw_line(Line(self._topleft, self._topright), colour)
        colour = background_colour
        if self.has_left_wall:
            colour = "black"
        self._window.draw_line(Line(self._topleft, self._bottomleft), colour)
        colour = background_colour
        if self.has_right_wall:
            colour = "black"
        self._window.draw_line(Line(self._topright, self._bottomright), colour)
        colour = background_colour
        if self.has_bottom_wall:
            colour = "black"
        self._window.draw_line(Line(self._bottomleft, self._bottomright), colour)
        
    def draw_move(self, to_cell, undo=False):
        if not undo:
            colour = "red"
        else:
            colour = "grey"
        self._window.draw_line(Line(self._centre, to_cell._centre), colour)
