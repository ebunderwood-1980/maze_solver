from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, w, h):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, height = h, width = w, bg='white')
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False 
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window Closed")

    def close(self): 
        self.__running = False 

    def draw_line(self, line, fill_color='black'):
        line.draw(self.__canvas, fill_color)
 

class Point(): 
    def __init__(self, x, y):
        self.x = x 
        self.y = y 


class Line():
    def __init__(self, beginning_point, end_point):
        self.p1 = beginning_point
        self.p2 = end_point

    def draw(self, canvas, color='black'): 
        canvas.create_line(self.p1.x, 
                           self.p1.y, 
                           self.p2.x, 
                           self.p2.y, 
                           fill=color, width=2)


class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall  = True 
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y1 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        #Call draw on each of the lines to draw on window.
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_left_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        #Get line color based on undo flag
        if undo:
            line_color = 'red'
        else:
            line_color = 'light green'

        #Get middle of current and to cells.
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self._win.draw_line(line, fill_color=line_color)
                
