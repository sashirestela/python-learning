from canvas import Canvas
from shapes import Rectangle, Square

canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input("Enter canvas height: "))

colors = {'white': (255, 255, 255), 'black': (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

canvas = Canvas(canvas_width, canvas_height, colors[canvas_color])

while True:
    shape_type = input("Enter shape type (r=rectangle, s=square, q=quit): ")
    if shape_type == 'q':
        break

    if shape_type == 'r':
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        red = int(input("Enter red color value (0-255): "))
        green = int(input("Enter green color value (0-255): "))
        blue = int(input("Enter blue color value (0-255): "))
        rectangle = Rectangle(x, y, width, height, (red, green, blue))
        rectangle.draw(canvas)

    elif shape_type == 's':
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        size = int(input("Enter size: "))
        red = int(input("Enter red color value (0-255): "))
        green = int(input("Enter green color value (0-255): "))
        blue = int(input("Enter blue color value (0-255): "))
        square = Square(x, y, size, (red, green, blue))
        square.draw(canvas)

    else:
        print("Invalid shape type. Please try again.")

canvas.make('canvas.png')