from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, w, h):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__cnvs = Canvas(self.__root, height = h, width = w, bg='white')
        self.__cnvs.pack(fill=BOTH, expand=1)
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


