import logging
import random

from App.src.tools.tools import Scribe
from random import randrange

# algorithms import

# pipelines algos
from App.src.filters.simplified_filters import simplified_algorithm
from App.src.filters.typed_filters import typed_algorithm
from App.src.filters.generic_filters import generic_algorithm

# parallel algos
from App.src.filters.simplified_filters_parallel import simplified_algorithm_parallel
from App.src.filters.generic_filters_parallel import generic_algorithm_parallel
from App.src.filters.typed_filters_parallel import typed_algorithm_parallel
# tkinter
from tkinter import ALL, BOTTOM, StringVar, Tk, filedialog as fd
from tkinter import simpledialog, Button, Canvas, Frame, Label, Radiobutton, ttk
from tkinter.messagebox import askyesno

Colors = ['Red', 'Green', 'Blue', 'Grey', 'Pink']


class ShapeApp:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.fileTypes = [('JSON File', '*.json'), ('JSON File', '*.JSON')]

        self.mouse_x = None
        self.mouse_y = None
        self.execution_data = None
        self.color = "Blue"
        # Root

        self.root = Tk()
        self.root.geometry("600x700")
        self.root.title('DOD shape project')

        # Top Frame

        self.topFrame = Frame(self.root, height=200,
                              highlightbackground="blue", highlightthickness=2)
        self.topFrame.pack()

        # Grid items

        self.bsujet1 = Button(
            self.topFrame, text='Simplified', command=self.simplified_button)

        self.bsujet2 = Button(
            self.topFrame, text='Generic', command=self.generic_button)

        self.bsujet3 = Button(
            self.topFrame, text='Typed', command=self.typed_button)

        self.bAddCircle = Button(
            self.topFrame, text='Add Circle', command=self.addCircle)
        self.bAddRandCircle = Button(
            self.topFrame, text='Add Circle Rand', command=self.addCircleRand)
        self.bAddRect = Button(
            self.topFrame, text='Add Rect', command=self.addRectangle)
        self.bAddRandRect = Button(
            self.topFrame, text='Add Rect Rand', command=self.addRectangleRand)

        self.bimportJson = Button(
            self.topFrame, text='Import', command=self.importJson)
        self.bexportJson = Button(
            self.topFrame, text='Export', command=self.exportJson)
        self.bclear = Button(self.topFrame, text='Clear', command=self.clear)

        self.mouseText = StringVar()
        self.mouseLabel = Label(self.topFrame, textvariable=self.mouseText)

        self.colorText = StringVar()
        self.colorLabel = Label(self.topFrame, textvariable=self.colorText)
        self.colorText.set("     ")
        self.colorLabel.config(bg=self.color)

        self.colorButtons = []
        self.colorButtons.append(Button(
            self.topFrame, text=Colors[0], command=lambda: self.setColor(Colors[0]), background=Colors[0]))
        self.colorButtons.append(Button(
            self.topFrame, text=Colors[1], command=lambda: self.setColor(Colors[1]), background=Colors[1]))
        self.colorButtons.append(Button(
            self.topFrame, text=Colors[2], command=lambda: self.setColor(Colors[2]), background=Colors[2]))
        self.colorButtons.append(Button(
            self.topFrame, text=Colors[3], command=lambda: self.setColor(Colors[3]), background=Colors[3]))
        self.colorButtons.append(Button(
            self.topFrame, text=Colors[4], command=lambda: self.setColor(Colors[4]), background=Colors[4]))
        self.threadSelect = ttk.Combobox(self.topFrame, state="readonly", values=[1, 2, 3, 4])
        self.threadSelect.current(0)
        self.threadText = StringVar()
        self.threadLabel = Label(self.topFrame, textvariable=self.threadText)
        self.threadText.set("Thread n??:")

        # Grid
        self.bsujet1.grid(column=0, row=1)
        self.bsujet2.grid(column=1, row=1)
        self.bsujet3.grid(column=2, row=1)

        self.bAddCircle.grid(column=0, row=2)
        self.bAddRandCircle.grid(column=1, row=2)
        self.bAddRect.grid(column=2, row=2)
        self.bAddRandRect.grid(column=3, row=2)

        self.bimportJson.grid(column=0, row=3)
        self.bexportJson.grid(column=1, row=3)
        self.bclear.grid(column=2, row=3)

        for colorButton in self.colorButtons:
            colorButton.grid(
                column=self.colorButtons.index(colorButton), row=4)

        self.colorLabel.grid(column=0, row=5)
        self.mouseLabel.grid(column=1, row=5)

        self.modes = ['pipeline', 'parallel']
        self.modeLabels = ['Pipeline', 'Parallel']
        self.mode = StringVar()
        self.mode.set(self.modes[0])

        self.bpipeline = Radiobutton(self.topFrame, variable=self.mode, text=self.modeLabels[0], value=self.modes[0])
        self.bparallel = Radiobutton(self.topFrame, variable=self.mode, text=self.modeLabels[1], value=self.modes[1])
        self.bpipeline.grid(column=2, row=5)
        self.bparallel.grid(column=3, row=5)

        self.timeText = StringVar()
        self.timeLabel = Label(self.topFrame, textvariable=self.timeText)
        self.timeText.set("Time:")
        self.timeLabel.grid(column=0, row=6)

        self.threadSelect.grid(column=3, row=6)
        self.threadLabel.grid(column=2, row=6)

        # drawing area
        self.drawFrame = Frame(self.root, width=self.x, height=self.y, bg='lightgrey',
                               highlightbackground="blue", highlightthickness=2)
        self.canvas = Canvas(self.drawFrame, bg="white",
                             height=self.x, width=self.y)

        self.canvas.bind('<Motion>', self.setMotion)

        self.shapes = list()
        self.update()

    def setMotion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        self.mouseText.set('x: {}, y: {}'.format(self.mouse_x, self.mouse_y))

    def importJson(self):
        filename = fd.askopenfilename(filetypes=self.fileTypes)
        shapes = Scribe.import_shapes_from_file(filename)
        for shape in shapes:
            self.shapes.append(shape)
        self.update()

    def exportJson(self):
        filename = fd.asksaveasfilename(
            filetypes=self.fileTypes, defaultextension=self.fileTypes[0], title="Save As")
        Scribe.export_shapes_to_file(self.shapes, filename)

    def addCircle(self):

        radius = simpledialog.askinteger("Add circle", 'Circle radius value [{}, {}]'.format(
            10, self.x / 2), parent=self.root, minvalue=10, maxvalue=self.x / 2)
        if radius is None:
            return
        x = simpledialog.askinteger('Add circle', 'Circle x value [{}, {}]'.format(
            radius, self.x - radius), parent=self.root, minvalue=radius, maxvalue=self.x - radius)
        if x is None:
            return

        y = simpledialog.askinteger('Add circle', 'Circle y value [{}, {}]'.format(
            radius, self.y - radius), parent=self.root, minvalue=radius, maxvalue=self.y - radius)
        if y is None:
            return

        circle = dict()
        circle["radius"] = radius
        circle["origin"] = (x, y)
        circle["color"] = self.color
        self.shapes.append(circle)
        self.update()

    def addCircleRand(self):
        circle = dict()
        circle["radius"] = randrange(10, self.x / 2)
        circle["origin"] = (randrange(circle["radius"], self.x - circle["radius"]),
                            randrange(circle["radius"], self.y - circle["radius"]))
        circle["color"] = random.choice(Colors)
        self.shapes.append(circle)
        self.update()

    def drawResultRect(self):

        if self.execution_data is not None:
            p1 = self.execution_data["point_1"]
            p2 = self.execution_data["point_2"]

            # x1, y1, x2, y2
            tl = (p1[0], p1[1])
            tr = (p2[0], p1[1])
            bl = (p1[0], p2[1])
            br = (p2[0], p2[1])

            dash = (5, 2)
            lineWidth = 3

            self.canvas.create_line(tl, tr, dash=dash, width=lineWidth)
            self.canvas.create_line(tr, br, dash=dash, width=lineWidth)
            self.canvas.create_line(br, bl, dash=dash, width=lineWidth)
            self.canvas.create_line(bl, tl, dash=dash, width=lineWidth)

    def addRectangle(self):

        x = simpledialog.askinteger('Add quad', 'Quad x value [{}, {}]'.format(
            0, self.x), parent=self.root, minvalue=0, maxvalue=self.x)
        if x is None:
            return
        y = simpledialog.askinteger('Add quad', 'Quad y value [{}, {}]'.format(
            0, self.y), parent=self.root, minvalue=0, maxvalue=self.y)
        if y is None:
            return

        width = simpledialog.askinteger('Add quad', 'Quad width value [{}, {}]'.format(
            0, self.x - x), parent=self.root, minvalue=0, maxvalue=self.x - x)
        if width is None:
            return
        height = simpledialog.askinteger('Add quad', 'Quad height value [{}, {}]'.format(
            0, self.y - y), parent=self.root, minvalue=0, maxvalue=self.y - y)
        if height is None:
            return

        quad = dict()
        quad["height"] = height
        quad["width"] = width
        quad["origin"] = (x, y)
        quad["color"] = self.color
        self.shapes.append(quad)
        self.update()

    def addRectangleRand(self):
        quad = dict()
        quad["origin"] = (randrange(10, self.x), randrange(10, self.y))
        quad["height"] = randrange(self.y - quad["origin"][1])
        quad["width"] = randrange(self.x - quad["origin"][0])
        quad["color"] = random.choice(Colors)
        self.shapes.append(quad)
        self.update()

    def clear(self):
        doClear = askyesno(
            "Clear canvas", "Do you really want to clear the canvas?")
        if doClear:
            self.shapes = []
            self.update()

    def update(self):
        self.drawFrame.pack(side=BOTTOM)
        self.canvas.delete(ALL)
        self.drawShapes()

    def drawShapes(self):
        for shape in self.shapes:
            if shape.get("radius"):
                self.canvas.create_oval(shape["origin"][0] - shape["radius"], shape["origin"][1] - shape["radius"],
                                        shape["origin"][0] + shape["radius"], shape["origin"][1] + shape["radius"],
                                        fill=shape["color"])
            else:
                self.canvas.create_rectangle(shape["origin"][0], shape["origin"][1], shape["origin"]
                [0] + shape["width"], shape["origin"][1] + shape["height"], fill=shape["color"])
        self.drawResultRect()

    def run(self):
        self.canvas.pack()
        self.root.mainloop()

    def setColor(self, color):
        self.color = color
        self.colorLabel.config(bg=color)

    def simplified_button(self):
        if self.mode.get() == self.modes[1]:
            self.execution_data = simplified_algorithm_parallel(self.shapes, int(self.threadSelect.get()))
        else:
            self.execution_data = simplified_algorithm(self.shapes)

        self.timeText.set("Time: {}ms".format(self.execution_data["execution_time"]))
        self.update()

    def generic_button(self):
        if self.mode.get() == self.modes[1]:
            self.execution_data = generic_algorithm_parallel(self.shapes, int(self.threadSelect.get()))
        else:
            self.execution_data = generic_algorithm(self.shapes)

        logging.error(self.execution_data)
        self.timeText.set("Time: {}ms".format(self.execution_data["execution_time"]))
        self.update()

        print(self.threadSelect.get())

    def typed_button(self):
        if self.mode.get() == self.modes[1]:
            self.execution_data = typed_algorithm_parallel(self.shapes, int(self.threadSelect.get()))
        else:
            self.execution_data = typed_algorithm(self.shapes)

        self.execution_data = typed_algorithm(self.shapes)
        self.timeText.set("Time: {}ms".format(self.execution_data["execution_time"]))
        self.update()
