from random import randrange
import random

import json
from tkinter import ALL, BOTTOM, Button, Canvas, Frame, Tk, filedialog as fd
from shapegen import Scribe

Colors = ['Red', 'Green', 'Blue']

class App:
    def __init__(self, x, y):
        self.x = x
        self.y = y


        self.root = Tk()
        self.root.geometry("500x700")
        self.root.title('DOD shape project')

        self.topFrame = Frame(self.root, height=200, bg='green',
                        highlightbackground="blue", highlightthickness=2)
        self.topFrame.pack()

        self.bsujet1 = Button(self.topFrame, text='Sujet 1', command=self.sujet1)

        self.bsujet2 = Button(self.topFrame, text='Sujet 2', command=self.sujet2)

        self.bsujet3 = Button(self.topFrame, text='Sujet 3', command=self.sujet3)
        self.bAddCircle = Button(self.topFrame, text='Add Circle', command=self.addCircle)
        self.bAddRect = Button(self.topFrame, text='Add Rect', command=self.addRectangle)
        
        self.bimportJson = Button(self.topFrame, text='Import', command=self.importJson)
        self.bexportJson = Button(self.topFrame, text='Export', command=self.exportJson)

        self.bsujet1.grid(column=0, row=1)
        self.bsujet2.grid(column=1, row=1)
        self.bsujet3.grid(column=2, row=1)

        self.bAddCircle.grid(column=0, row=2)
        self.bAddRect.grid(column=2, row=2)
        
        self.bimportJson.grid(column=0, row=3)
        self.bexportJson.grid(column=1, row=3)

        self.drawFrame = Frame(self.root, width=self.x, height=self.y, bg='lightgrey',
                        highlightbackground="blue", highlightthickness=2)
        self.drawFrame.pack(side=BOTTOM)
        self.canvas = Canvas(self.drawFrame, bg="white", height=self.x, width=self.y)
        
        self.shapes = list()
        # self.addCircle()
        # self.addCircle()
        # self.addRectangle()
        # self.addRectangle()

        self.update()

    def importJson(self):
        filename = fd.askopenfilename()
        shapes = Scribe.import_shapes_from_file(filename)
        for shape in shapes:
            print(shape)
            self.shapes.append(shape)
        self.update()

    def exportJson(self):
        print("export")

    def addCircle(self):
        circle = dict()
        circle["radius"] = randrange(10, 40)
        circle["center"] = (randrange(0, self.x), randrange(0, self.y))
        circle["color"] =  random.choice(Colors)
        self.shapes.append(circle)
        self.update()

    def addRectangle(self):
        quad = dict()
        quad["height"] = randrange(self.y)
        quad["width"] = randrange(self.x)
        quad["origin"] = (randrange(0, self.x), randrange(0, self.y))
        quad["color"] =  random.choice(Colors)
        self.shapes.append(quad)
        self.update()

    def update(self):
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
