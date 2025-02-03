from graphics import Window, Line, Point, Cell




def main(): 
    win = Window(800, 600)
    p1 = Point(100,100)
    p2 = Point(200, 200)
    p3 = Point(300,100)
    p4 = Point(600, 400)
    my_Line = Line(p1, p2)
    my_Line2 = Line(p3, p4)
    win.draw_line(my_Line, 'black')
    win.draw_line(my_Line2, 'red')
    cell1 = Cell(p1, p4, win)
    cell1.draw()
    cell2 = Cell(p1,p2, win)
    cell2.has_bottom_wall = False
    cell2.draw()
    win.wait_for_close()  







if __name__ == '__main__':
    main()
