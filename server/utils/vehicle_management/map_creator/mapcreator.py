from tkinter import *
import math
import pickle
from PIL import ImageTk, Image
from utils.vehicle_management.map_creator import map
from utils import coordinate


class MapCreator:

    def __init__(self):

        self.n1 = []
        self.n2 = []
        self.img_h = 0
        self.map = map.Map()
        root = Tk()
        root.state("zoomed")
        scale = 0.7
        f1 = Frame(root)
        f1.pack()
        w = Canvas(f1, width=int(root.winfo_screenwidth()*scale), height=int(root.winfo_screenheight()*scale))
        w.pack()
        img = Image.open("map.png")
        ratio = min(int(w.cget("width"))/img.size[0], int(w.cget("height"))/img.size[1])
        size = int(img.size[0]*ratio), int(img.size[1]*ratio)
        self.img_h = size[1]
        img = img.resize(size, Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img)
        w.create_image(img.size[0]/2, img.size[1]/2, image=img2)
        v1 = StringVar()
        v2 = StringVar()

        def add_node(eventorigin):
            global x, y
            x = eventorigin.x
            y = eventorigin.y
            w.create_oval(x - 4, y - 4, x + 4, y + 4, fill="black", tags="node")

        def create_node(event):
            if len(self.n1) != 0 and len(self.n2) != 0:
                w.create_line(self.n1[0], self.img_h-self.n1[1], self.n2[0], self.img_h-self.n2[1], fill="black")
                node1 = coordinate.Coordinate(self.n1[0], self.n1[1])
                node2 = coordinate.Coordinate(self.n2[0], self.n2[1])
                self.map.add_node(node1, node2)
                self.n1 = []
                self.n2 = []
                v1.set("")
                v2.set("")

        def clear_nodes(event):
            self.n1 = []
            self.n2 = []
            v1.set("")
            v2.set("")

        def exit_program(event):
            with open('map.txt', 'wb') as outfile:
                pickle.dump(self.map.nodes, outfile)
            outfile.close()
            root.quit()

        def load_map():
            with open('map.txt', 'rb') as infile:
                data = pickle.load(infile)
            infile.close()
            self.map.nodes = data
            for key, value in self.map.nodes.items():
                for key2, value2 in value.items():
                    w.create_line(key.x, self.img_h - key.y, key2.x, self.img_h - key2.y, fill="black")
                w.create_oval(key.x - 4, self.img_h - key.y - 4, key.x + 4, self.img_h - key.y + 4,
                              fill="black", tags="node")

        def buttons():
            f = Frame(root)
            f.pack(side="bottom")
            b1 = Button(f, text="add nodes")
            b1.bind("<Button-1>", create_node)
            b1.pack(side="left")
            b2 = Button(f, text="clear nodes")
            b2.bind("<Button-1>", clear_nodes)
            b2.pack(side="left")
            b3 = Button(f, text="save and quit")
            b3.bind("<Button-1>", exit_program)
            b3.pack(side="left")
            w.tag_bind('node', '<Button-3>', on_object_click)
            w.bind('<Button-1>', add_node)

        def on_object_click(event):
            item = w.find_closest(event.x, event.y)
            if 'node' in w.gettags(item):
                n = w.coords(item)
                o = int((n[0] + n[2]) / 2), int(math.fabs((n[1] + n[3]) / 2 - self.img_h))
                print(o)
                if len(self.n1) == 0:
                    self.n1 = o
                    v1.set(str(self.n1))
                elif len(self.n2) == 0 and o != self.n1:
                    self.n2 = o
                    v2.set(str(self.n2))

        def labels():
            f3 = Frame(root)
            f3.pack(side="bottom")
            entry_n1 = Label(f3, textvariable=v1)
            entry_n2 = Label(f3, textvariable=v2)
            label1 = Label(f3, text="Node 1: ")
            label2 = Label(f3, text="Node 2: ")
            label1.pack(side="left")
            entry_n1.pack(side="left")
            label2.pack(side="left")
            entry_n2.pack(side="left")

        buttons()
        labels()
        load_map()
        root.mainloop()


if __name__ == "__main__":
    m = MapCreator()




