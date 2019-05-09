import tkinter as tk


class Simulator:
    # size is the window size
    # number_of_steps is size of the axis
    # routes is an array of vectors, currently limited to 5 routes
    # this is just a testing purpose software, not to be confused with something good

    def __init__(self, size, number_of_steps, routes):

        step_size = int(size / number_of_steps)
        half_size = size/2
        self.routes = routes

        self.scaleState = 0
        self.dotState = 0
        self.pathState = 0

        root = tk.Tk()
        root.title("Simulator")

        w = tk.Canvas(root, width=size, height=size)
        w.pack()

        def draw_scale(event):

            if self.scaleState == 1:
                w.delete("scale")
                self.scaleState -= 1

            else:
                w.create_line(0, half_size, size, half_size, tags="scale")
                w.create_line(half_size, 0, half_size, size, tags="scale")
                self.scaleState += 1

        def draw_dots(event):

            if self.dotState == 1:
                w.delete("dot")
                self.dotState -= 1
            else:
                numbers = list(range(0, size, step_size))
                for i in numbers:
                    for j in numbers:
                        w.create_oval(i-1, j-1, i+1, j+1, fill="black", tags="dot")
                self.dotState += 1

        def draw_path(event):

            if self.pathState == 1:
                w.delete("path")
                self.pathState -= 1
            else:
                i = 0
                while i < len(routes):
                    j = 1
                    route = routes[i]
                    colours = ["red", "black", "green", "blue", "yellow"]
                    while j < len(route):
                        start = route[j-1]
                        destination = route[j]
                        start_x = half_size+converter(start.x)
                        start_y = half_size-converter(start.y)
                        end_x = half_size+converter(destination.x)
                        end_y = half_size-converter(destination.y)
                        w.create_line(start_x, start_y, end_x, end_y, tags="path", fill=colours[i])
                        j += 1
                    i += 1
                self.pathState += 1

        def converter(number):
            value = number*step_size

            return value

        def buttons():
            f = tk.Frame(root)
            f.pack(side="bottom")
            b1 = tk.Button(f, text="Scale")
            b1.bind("<Button-1>", draw_scale)
            b1.pack(side="left")
            b2 = tk.Button(f, text="Dots")
            b2.bind("<Button-1>", draw_dots)
            b2.pack(side="left")
            b3 = tk.Button(f, text="Path")
            b3.bind("<Button-1>", draw_path)
            b3.pack(side="left")

        buttons()
        root.mainloop()

