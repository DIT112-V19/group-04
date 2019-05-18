from tkinter import *
from PIL import Image, ImageTk


class Simulator:
    # currently limited to 5 cars
    # this is just a testing purpose software, not to be confused with something good

    def __init__(self, carpool):
        self.pathState = 0

        scale = 1

        root = Tk()
        root.title("Simulator")
        root.state("zoomed")
        f2 = Frame(root)
        f2.grid(column=0, sticky="n")
        w = Canvas(f2, width=int(root.winfo_screenwidth()*scale), height=int(root.winfo_screenheight()*scale))
        w.pack()

        img = Image.open("utils/mapcreator/map.png")
        ratio = min(int(w.cget("width")) / img.size[0], int(w.cget("height")) / img.size[1])
        size = int(img.size[0] * ratio), int(img.size[1] * ratio)
        self.img_h = size[1]
        img = img.resize(size, Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img)
        w.create_image(img.size[0] / 2, img.size[1] / 2, image=img2)

        def draw_path():
            w.delete("path")
            i = 0
            while i < len(carpool.cars):
                j = 1
                car = carpool.cars[i]
                colours = ["red", "green", "blue", "yellow", "black"]
                w.create_oval(car.location.x * ratio - 4, self.img_h - car.location.y * ratio - 4,
                              car.location.x * ratio + 4, self.img_h - car.location.y * ratio + 4,
                              fill=colours[i], tags="path")
                for dest in car.destinations:
                    w.create_oval(dest.x * ratio - 4, self.img_h - dest.y * ratio - 4,
                                  dest.x * ratio + 4, self.img_h - dest.y * ratio + 4,
                                  fill=colours[i], tags="path")

                while j < len(car.coordinates):
                    start = car.coordinates[j-1]
                    end = car.coordinates[j]
                    w.create_line(start.x * ratio, self.img_h - start.y * ratio,
                                  end.x * ratio, self.img_h - end.y * ratio, fill=colours[i], tags="path")
                    j += 1
                i += 1

            root.after(2500, draw_path)

        draw_path()
        root.mainloop()
