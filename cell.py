from graphics import Point, Line

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

    
    def draw(self):
        if self.has_top_wall:
            self._window.draw_line(Line(self._topleft, self._topright))
        if self.has_left_wall:
            self._window.draw_line(Line(self._topleft, self._bottomleft))
        if self.has_right_wall:
            self._window.draw_line(Line(self._topright, self._bottomright))
        if self.has_bottom_wall:
            self._window.draw_line(Line(self._bottomleft, self._bottomright))
        
    def draw_move(self, to_cell, undo=False):
        if not undo:
            colour = "red"
        else:
            colour = "grey"
        self._window.draw_line(Line(self._centre, to_cell._centre), colour)
