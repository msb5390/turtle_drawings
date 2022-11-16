from math import sin, cos, pi

def square(t, side=100):
    """Draw a square with turtle.

    Inputs:
         t: the turtle
         side: the length of the sides (defaults to 100)
    """
    for i in range(4):
        t.fd(side)
        t.rt(90)

def pinwheel(t, size, n):
    """Draw a 'pinwheel,' consisting of a series of squares drawn at
    different angles.

    Inputs:
         t: the turtle
         size: the size of the squares
         n: the number of squares used to create the pinwheel
    """
    for i in range(n):
        square(t, size)
        t.rt(360/n)             # rotate to complete pinwheel in n steps

def ellipse(t, x, y, multicolor=False):
    """Draw an ellipse using parametric equations. Note: The ellipse will by
    *centered* on the turtle's current position.

    Inputs:
         t: the turtle
         x: the semi-major (or minor) axis
         y: the semi-minor (or major) axis
         multicolor: Set to False (default) for solid color ellipse, or True 
                     for multicolored ellipse.
    """
    x0, y0 = t.pos()            # get current position for reference
    t.penup()                   # lift pen before moving to edge of ellipse
    t.goto(x0 + x, y0)          # send turtle to edge of ellipse
    t.pendown()                 # get read to draw!
    steps = max(x, y) * 4       # use enough steps to make a smooth ellipse
    for i in range(steps):
        if multicolor:
            t.pencolor(color_function(i, steps))
        t.goto(x*cos(i/steps * 2*pi) + x0, y*sin(i/steps * 2*pi) + y0)
    t.penup()
    t.goto(x0, y0)              # move turtle back to where it started
    t.pendown()

def flower(t, x, y, n, color='black'):
    """Draw a 'flower' consisting of multiple rotated ellipses.

    Inputs:
         t: the turtle
         x: the semi-major (or minor) axis of the ellipses
         y: the semi-minor (or major) axis of the ellipses
         n: the number of ellipses to use to draw the flower
         color: the color string to use for flower color. Defaults to black.
    """
    original_color = t.pencolor() # store original color for resetting after
    t.pencolor(color)             # set new pencolor
    for i in range(n):            # draw the flower
        oval(t, x, y)
        t.rt(360/n)
    t.pencolor(original_color)    # reset the pencolor


def parametric(t, x, y, x_freq, y_freq, multicolor=True):
    """A function to draw Lissajous curves.

    Inputs:
         t: the turtle
         x: the extent of the pattern in the x direction
         y: the extent of the pattern in the y direction
         x_freq: how many oscillations to make in the x direction
         y_freq: how many oscillations to make in the y direction
         multicolor: Vary the color during drawing? (Default True)
    """
    steps = max(x*x_freq, y*y_freq) * 4 # choose step number wisely (smoothing)
    x0, y0 = t.pos()                    # store original position of turtle
    t.penup()
    t.goto(x + x0, y0)                  # go to outer edge of figure to start
    t.pendown()                         # get ready to draw!
    for i in range(steps+1):
        t.pencolor(color_function(i, steps))
        t.goto(x*cos(2*pi*x_freq*i/steps) + x0, y*sin(2*pi*y_freq*i/steps)+y0)
    t.penup()
    t.goto(x0, y0)
    t.pendown()

def color_function(i, steps):
    """Function to smoothly vary colors from red to blue.

    Inputs:
         i: current step in the blending process
         steps: total steps in the blending process

    Outputs:
         (r, g, b): a tuple of rgb values between 0 and 1 inclusive.
                    Note: this assumes a default colormode of 1 for the screen.
    """
    step_size = 2 / steps       # Blending consists of 2 parts, so double step
    r = g = b = 0
    if i < steps//2:            # Part 1: decreasing red, increasing green
        r = 1 - i * step_size
        g = i * step_size
    else:                       # Part 2: decreasing green, increasing blue
        g = 1 - (i - steps//2) * step_size
        b = (i - steps//2) * step_size
    return r, g, b
