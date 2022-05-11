import logging
import random

from Scribe import Scribe
from random import randrange

# algorithms import
from filters.simplified_filters import simplified_algorithm

# tkinter
from tkinter import ALL, BOTTOM,  StringVar, Tk, filedialog as fd
from tkinter import simpledialog, Button, Canvas, Frame, Label, Radiobutton
from tkinter.messagebox import askyesno

Colors = ['Red', 'Green', 'Blue', 'Grey', 'Pink']


class App:
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
        self.root.geometry("500x700")
        self.root.title('DOD shape project')

        # Top Frame

        self.topFrame = Frame(self.root, height=200,
                              highlightbackground="blue", highlightthickness=2)
        self.topFrame.pack()

        # Grid items

        self.bsujet1 = Button(
            self.topFrame, text='Sujet 1', command=self.sujet1)

        self.bsujet2 = Button(
            self.topFrame, text='Sujet 2', command=self.sujet2)

        self.bsujet3 = Button(
            self.topFrame, text='Sujet 3', command=self.sujet3)
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

        self.modes = ['pipeline', 'parelelle']
        self.modeLabels = ['Pipeline', 'Parelelle']
        self.mode = StringVar()
        self.bpipeline = Radiobutton(self.topFrame, variable=self.mode, text=self.modeLabels[0], value=self.modes[0])
        self.bparelelle = Radiobutton(self.topFrame, variable=self.mode, text=self.modeLabels[1], value=self.modes[1])
        self.bpipeline.grid(column=2, row=5)
        self.bparelelle.grid(column=3, row=5)


        self.timeText = StringVar()
        self.timeLabel = Label(self.topFrame, textvariable=self.timeText)
        self.timeText.set("Time:")
        self.timeLabel.grid(column=0, row=6)

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

            #print(self.execution_data)
            p1 = self.execution_data["point_1"]
            p2 = self.execution_data["point_2"]

            # x1, y1, x2, y2
            tl = (p1[0], p1[1])
            tr = (p2[0], p1[1])
            bl = (p1[0], p2[1])
            br = (p2[0], p2[1])

            dash = (5,2)
            lineWidth = 3

            self.canvas.create_line(tl , tr, dash=dash, width=lineWidth)
            self.canvas.create_line(tr , br, dash=dash, width=lineWidth)
            self.canvas.create_line(br , bl, dash=dash, width=lineWidth)
            self.canvas.create_line(bl , tl, dash=dash, width=lineWidth)

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
        # self.colorText.set('color: {}'.format(color))
        self.colorLabel.config(bg=color)

    def sujet1(self):
        print('sujet1')
        logging.info('Starting emission with a simplfied data structure')
        logging.info(self.shapes)
        execution_data = dict(point_1=(0, 0), point_2=(0, 0), execution_time=0)  # format des data renvoyee par simplfied algorithm
        self.execution_data = simplified_algorithm(self.shapes)
        self.timeText.set("Time: {}ms".format(self.execution_data["execution_time"]))
        self.update()
        print(self.mode.get())

    def sujet2(self):
        print('sujet2')
        print(self.mode.get())

    def sujet3(self):
        print('sujet3')
        print(self.mode.get())
