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
    def __init__(self, p1, p2, window):
        self.has_left_wall = True
        self.has_right_wall  = True 
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__top_left = p1
        self.__bottom_right = p2
        self.__win = window

    def draw(self):
        if self.__win is None:
            return
        
        #Calculate remaining points of square.  Top left and bottom right already passed in.
        top_right = Point(self.__bottom_right.x, self.__top_left.y)
        bottom_left = Point(self.__top_left.x, self.__bottom_right.y)

        #Draw lines for the cell
        top_line = Line(self.__top_left, top_right)
        bottom_line = Line(bottom_left, self.__bottom_right)
        left_line = Line(self.__top_left, bottom_left)
        right_line = Line(top_right, self.__bottom_right)

        #Call draw on each of the lines to draw on window.
        if self.has_top_wall:
            self.__win.draw_line(top_line)
        if self.has_bottom_wall:
            self.__win.draw_line(bottom_line)
        if self.has_left_wall:
            self.__win.draw_line(left_line)
        if self.has_right_wall:
            self.__win.draw_line(right_line)

    def draw_move(self, to_cell, undo=False):
        #Get line color based on undo flag
        if undo:
            line_color = 'red'
        else:
            line_color = 'light blue'

        #Get middle of current and to cells.
        current_middle = Point((self.__bottom_right.x + self.__top_left.x)/2, (self.__top_left.y + self.__bottom_right.y)/2)
        to_middle = Point((to_cell.__bottom_right.x + to_cell.__top_left.x)/2, (to_cell.__top_left.y + to_cell.__bottom_right.y)/2)

        #Draw the line
        move_line = Line(current_middle, to_middle)
        self.__win.draw_line(move_line, fill_color=line_color)
                
