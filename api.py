import sys
import configparser
import os.path
from random import choice

from random import randint
from gui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from config import createConfig


class dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_pos(self, x, y):
        self.__init__(x, y)
    def get_pos(self):
        return(self.x, self.y)

def get_half_pos(a, b):
    x1, y1 = a.get_pos()
    x2, y2 = b.get_pos()
    return(x1 + (x2-x1) // 2, y1 + (y2-y1) //2)

def get_triangle_centroid_dot(dots):
    pos_x_sum = 0
    pos_y_sum = 0
    for each in dots:
        pos_x, pos_y = each.get_pos()
        pos_x_sum += pos_x
        pos_y_sum += pos_y
    pos_x_sum = pos_x_sum // 3
    pos_y_sum = pos_y_sum // 3
    return (dot(pos_x_sum, pos_y_sum))

def get_rand_dot(x_res, y_res):
    return(dot(randint(0, x_res), randint(0, y_res)))

class SetOfDots(QMainWindow, Ui_MainWindow):
    def __init__(self, config):
        super().__init__()
        self.setupUi(self, config)

    def drawDot(self, dot):
        dot_pos_x, dot_pos_y = dot.get_pos()
        self.canvas.addEllipse(dot_pos_x, dot_pos_y, 2, 2)
        self.graphicsView.update()

    def setAttractors(self):
        x_res = int(config.get("Settings", "resolution_width"))
        y_res = int(config.get("Settings", "resolution_height"))
        self.attractors = []
        for i in range(3):
            self.attractors.append(get_rand_dot(x_res, y_res))
        for dot in self.attractors:
            self.drawDot(dot)
        return(self.attractors)

    def addDots(self):
        attractors = self.setAttractors()
        startDot = get_triangle_centroid_dot(attractors)
        for i in range(10000):
            startDot.set_pos(*get_half_pos(startDot, choice(attractors)))
            self.drawDot(startDot)

def start():
    if not os.path.isfile('settings.ini'):
        createConfig('settings.ini')
    global config
    config = configparser.ConfigParser()
    config.read("settings.ini")
    app = QApplication(sys.argv)
    attractors = SetOfDots(config)
    attractors.show()
    attractors.addDots()
    sys.exit(app.exec_())

