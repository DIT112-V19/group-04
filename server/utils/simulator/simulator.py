from tkinter import *
from PIL import Image, ImageTk


class Simulator:
    # routes is an array of vectors, currently limited to 5 routes
    # this is just a testing purpose software, not to be confused with something good

    def __init__(self, routes, start, goal):

        self.routes = routes
        self.scaleState = 0
        self.dotState = 0
        self.pathState = 0

        scale = 0.90

        root = Tk()
        root.title("Simulator")
        root.state("zoomed")
        f2 = Frame(root)
        f2.grid(column=0, sticky="n")
        w = Canvas(f2, width=int(root.winfo_screenwidth()*scale), height=int(root.winfo_screenheight()*scale))
        w.pack()

        img = Image.open("map.png")
        ratio = min(int(w.cget("width")) / img.size[0], int(w.cget("height")) / img.size[1])
        size = int(img.size[0] * ratio), int(img.size[1] * ratio)
        self.img_h = size[1]
        img = img.resize(size, Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img)
        w.create_image(img.size[0] / 2, img.size[1] / 2, image=img2)

        w.create_oval(start.x * ratio - 4, self.img_h - start.y * ratio - 4, start.x * ratio + 4, self.img_h - start.y * ratio + 4, fill="orange", tags="customer")
        w.create_oval(goal.x * ratio - 4, self.img_h - goal.y * ratio - 4, goal.x * ratio + 4, self.img_h - goal.y * ratio + 4, fill="purple", tags="customer")

        def draw_path(event):

            if self.pathState == 1:
                w.delete("path")
                self.pathState = 0
            else:
                i = 0
                while i < len(routes):
                    j = 1
                    route = routes[i]
                    colours = ["red", "green", "blue", "yellow", "black"]
                    w.create_oval(route[0].x * ratio - 4, self.img_h - route[0].y * ratio - 4,
                                  route[0].x * ratio + 4, self.img_h - route[0].y * ratio + 4,
                                  fill=colours[i], tags="path")
                    while j < len(route):
                        start = route[j-1]
                        end = route[j]
                        w.create_line(start.x * ratio, self.img_h - start.y * ratio,
                                      end.x * ratio, self.img_h - end.y * ratio, fill=colours[i], tags="path")
                        j += 1
                    i += 1
                self.pathState = 1

        def buttons():
            f = Frame(root)
            f.grid(column=1, sticky="n")
            b3 = Button(f, text="Path")
            b3.bind("<Button-1>", draw_path)
            b3.pack()

        buttons()
        root.mainloop()

