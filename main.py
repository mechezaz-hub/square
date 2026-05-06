def on_button_pressed_a():
    turtle.pen(TurtlePenMode.DOWN)
    turtle.forward(1)
    turtle.turn_right()
    turtle.forward(1)
    turtle.turn_right()
    turtle.forward(1)
    turtle.turn_right()
    turtle.forward(1)
    turtle.turn_right()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
