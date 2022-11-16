from math import sin, cos, pi

def square(t, side=100):
    for i in range(4):
        t.fd(side)
        t.rt(90)

def tilted_square(t, side=100, tilt=0):
    square(t, side)
    t.rt(tilt)

def pinwheel(t, size, n):
    for i in range(n):
        tilted_square(t, size, 360/n)

def oval(t, x, y):
    x0, y0 = t.pos()
    t.penup()
    t.goto(x0 + x, y0)
    t.pendown()
    steps = max(x, y) * 4
    for i in range(steps):
        t.pencolor(color_function(i, steps))
        t.goto(x*cos(i/steps * 2*pi) + x0, y*sin(i/steps * 2*pi) + y0)
    t.penup()
    t.goto(x0, y0)
    t.pendown()

def flower(t, x, y, n, color='black'):
    original_color = t.pencolor()
    t.pencolor(color)
    for i in range(n):
        oval(t, x, y)
        t.rt(360/n)
    t.pencolor(original_color)


def parametric(t, x, y, x_freq, y_freq):
    steps = max(x*x_freq, y*y_freq) * 4
    x0, y0 = t.pos()
    t.penup()
    t.goto(x + x0, y0)
    t.pendown()
    for i in range(steps):
        t.pencolor(color_function(i, steps))
        t.goto(x*cos(2*pi*x_freq*i/steps) + x0, y*sin(2*pi*y_freq*i/steps)+y0)
    t.penup()
    t.goto(x0, y0)
    t.pendown()

def color_function(i, steps):
    step_size = 2 / steps
    r = g = b = 0
    if i < steps//2:
        r = 1 - i * step_size
        g = i * step_size
    else:
        g = 1 - i * step_size/2
        b = i * step_size/2
    return r, g, b
