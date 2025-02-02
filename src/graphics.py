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
        
