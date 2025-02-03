from graphics import Window, Line, Point, Cell




def main(): 
    win = Window(800, 600)
    p1 = Point(100, 300)
    p2 = Point(300, 100)
    p3 = Point(500, 400)
    p4 = Point(600, 100)
    cell1 = Cell(p1, p2, win)
    cell2 = Cell(p3, p4, win)
    cell1.draw()
    cell2.draw()
    cell1.draw_move(cell2, undo=False)
    win.wait_for_close()  







if __name__ == '__main__':
    main()
