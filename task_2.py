import turtle


def perform_switch_case(state, t, turn, max_turns):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)

    if state == "INIT":
        state = "DOWN"
        t.setheading(270)  
        return state, turn

    if state == "DOWN":
        t.forward(10)
        if y <= -turn:
            state = "RIGHT"
            t.setheading(0)
        return state, turn

    if state == "RIGHT":
        t.forward(10)
        if x >= turn:
            state = "UP"
            t.setheading(90)  
        return state, turn

    if state == "UP":
        t.forward(10)
        if y >= turn:
            state = "LEFT"
            t.setheading(180)  
        return state, turn

    if state == "LEFT":
        t.forward(10)
        if x <= -turn:
            turn += 1
            if turn > max_turns:
                state = "STOP"
            else:
                state = "DOWN"
                t.setheading(270)  
        return state, turn

    return state, turn


def draw():
    curr_state = "INIT"
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)
    turn = 1
    max_turns = 5  

    while curr_state != "STOP":
        curr_state, turn = perform_switch_case(curr_state, t, turn, max_turns)

    turtle.done()


if __name__ == "__main__":
    draw()
