from raylibpy import *

init_window(800, 400, "Hello")
while not window_should_close():
    begin_drawing()
    clear_background(BLUE)
    draw_circle(400, 200, 80, BLACK)
    draw_text("Sup", 355, 180, 50, ORANGE)
    end_drawing()
close_window()