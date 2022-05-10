from random import randrange
import random

import json
from tkinter import ALL, BOTTOM, Button, Canvas, Frame, Label, StringVar, Tk, filedialog as fd, messagebox, simpledialog
from shapegen import Scribe

Colors = ['Red', 'Green', 'Blue']

class App:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.fileTypes =  [('JSON File', '*.json')]

        self.mousex = None
        self.mousey = None

        # Root

        self.root = Tk()
        self.root.geometry("500x700")
        self.root.title('DOD shape project')

        # Top Frame

        self.topFrame = Frame(self.root, height=200,
                        highlightbackground="blue", highlightthickness=2)
        self.topFrame.pack()

        # Grid items

        self.bsujet1 = Button(self.topFrame, text='Sujet 1', command=self.sujet1)

        self.bsujet2 = Button(self.topFrame, text='Sujet 2', command=self.sujet2)

        self.bsujet3 = Button(self.topFrame, text='Sujet 3', command=self.sujet3)
        self.bAddCircle = Button(self.topFrame, text='Add Circle', command=self.addCircle)
        self.bAddRect = Button(self.topFrame, text='Add Rect', command=self.addRectangle)
        
        self.bimportJson = Button(self.topFrame, text='Import', command=self.importJson)
        self.bexportJson = Button(self.topFrame, text='Export', command=self.exportJson)
        self.bclear = Button(self.topFrame, text='Clear', command=self.clear)
       
        self.mouseText = StringVar()
        self.mouseLabel = Label(self.topFrame, textvariable=self.mouseText)
        

        # Grid
        self.bsujet1.grid(column=0, row=1)
        self.bsujet2.grid(column=1, row=1)
        self.bsujet3.grid(column=2, row=1)

        self.bAddCircle.grid(column=0, row=2)
        self.bAddRect.grid(column=2, row=2)
        
        self.bimportJson.grid(column=0, row=3)
        self.bexportJson.grid(column=1, row=3)
        self.bclear.grid(column=2, row=3)

        self.mouseLabel.grid(column=1, row=4)


        self.drawFrame = Frame(self.root, width=self.x, height=self.y, bg='lightgrey',
                        highlightbackground="blue", highlightthickness=2)
        self.canvas = Canvas(self.drawFrame, bg="white", height=self.x, width=self.y)
        
        self.canvas.bind('<Motion>', self.setMotion)

        self.shapes = list()

        # self.addCircle()
        # self.addCircle()
        # self.addRectangle()
        # self.addRectangle()

        self.update()

    def setMotion(self, event):
        self.mousex = event.x
        self.mousey = event.y
        self.mouseText.set('x: {}, y: {}'.format(self.mousex, self.mousey)) #= 'x: {}, y: {}'.format(self.mousex, self.mousey)

    def importJson(self):
        filename = fd.askopenfilename(filetypes=self.fileTypes)
        shapes = Scribe.import_shapes_from_file(filename)
        for shape in shapes:
            self.shapes.append(shape)
        self.update()

    def exportJson(self):
        filename = fd.asksaveasfilename(filetypes = self.fileTypes, defaultextension = self.fileTypes, title="Save As")
        Scribe.export_shapes_to_file(self.shapes,filename)

    def addCircle(self):

        radius = simpledialog.askinteger("Add circle", 'Circle radius value [{}, {}]'.format(10, self.x/2), parent=self.root, minvalue=10, maxvalue=self.x/2)
        if radius == None:
            return
        x = simpledialog.askinteger('Add circle', 'Circle x value [{}, {}]'.format(radius, self.x-radius), parent=self.root, minvalue=radius, maxvalue=self.x-radius)
        if x == None:
            return

        y = simpledialog.askinteger('Add circle', 'Circle y value [{}, {}]'.format(radius, self.y-radius), parent=self.root, minvalue=radius, maxvalue=self.y-radius)
        if y == None:
            return

        circle = dict()
        circle["radius"] = radius
        circle["center"] = (x,y)
        circle["color"] =  random.choice(Colors)
        self.shapes.append(circle)
        self.update()

    def addRectangle(self):

        x = simpledialog.askinteger('Add quad', 'Quad x value [{}, {}]'.format(0, self.x), parent=self.root, minvalue=0, maxvalue=self.x)
        if (x == None):
            return
        y = simpledialog.askinteger('Add quad', 'Quad y value [{}, {}]'.format(0, self.y), parent=self.root, minvalue=0, maxvalue=self.y)
        if (y == None):
            return

        width = simpledialog.askinteger('Add quad', 'Quad width value [{}, {}]'.format(0, self.x - x), parent=self.root, minvalue=0, maxvalue=self.x - x)
        if (width == None):
            return
        height = simpledialog.askinteger('Add quad', 'Quad height value [{}, {}]'.format(0, self.y - y), parent=self.root, minvalue=0, maxvalue=self.y - y)
        if (height == None):
            return

        quad = dict()
        quad["height"] = height
        quad["width"] = width
        quad["origin"] = (x, y)
        quad["color"] =  random.choice(Colors)
        self.shapes.append(quad)
        self.update()

    def addRectangleRand(self):
        quad = dict()
        quad["origin"] = (randrange(0, self.x), randrange(0, self.y))
        quad["height"] = randrange(self.y - quad["origin"][1])
        quad["width"] = randrange(self.x - quad["origin"][0])
        quad["color"] =  random.choice(Colors)
        self.shapes.append(quad)
        self.update()
    
    def clear(self):
        self.shapes = []
        self.update()


    def update(self):
        self.drawFrame.pack(side=BOTTOM)
        self.canvas.delete(ALL)
        self.drawShapes()

    def drawShapes(self):
        for shape in self.shapes:
            if(shape.get("radius")):
                self.canvas.create_oval(shape["center"][0] - shape["radius"], shape["center"][1] - shape["radius"], shape["center"][0] + shape["radius"], shape["center"][1] + shape["radius"], fill=shape["color"])
            else:
                self.canvas.create_rectangle(shape["origin"][0], shape["origin"][1], shape["origin"][0] + shape["width"], shape["origin"][1] + shape["height"], fill=shape["color"])

    def run(self):
        self.canvas.pack()
        self.root.mainloop()
        
    def sujet1(self):
        print('sujet1')

    def sujet2(self):
        print('sujet2')

    def sujet3(self):
        print('sujet3')

def main(): 
    app = App(500,500)
    app.run()
    


if __name__ == '__main__':
    main()
