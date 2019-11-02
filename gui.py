from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, config):

        MainWindow.setObjectName("Attractors")
        window_width = int(config.get("Settings", "resolution_width")) // 15
        window_height = int(config.get("Settings", "resolution_height")) // 6
        MainWindow.resize(window_width, window_height)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.resize(window_width, window_height)
        self.centralwidget.setSizePolicy(sizePolicy)

        self.canvas = QtWidgets.QGraphicsScene(self.centralwidget)
        self.canvas.setObjectName("canvas")
        self.graphicsView = QtWidgets.QGraphicsView()
        self.graphicsView.setScene(self.canvas)
        self.graphicsView.show()

        self.controlBox = QtWidgets.QGroupBox(self.centralwidget)
        self.controlBox.setGeometry(QtCore.QRect(0, 0, window_width, window_height))
        self.controlBox.setObjectName("controlBox")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.controlBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, window_width, window_height))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.labelGenSpeed = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelGenSpeed.setObjectName("labelGenSpeed")
        self.verticalLayout.addWidget(self.labelGenSpeed)
        self.sliderGenSpeed = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.sliderGenSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.sliderGenSpeed.setObjectName("sliderGenSpeed")
        self.verticalLayout.addWidget(self.sliderGenSpeed)

        self.labelDotCount = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelDotCount.setObjectName("labelDotCount")
        self.verticalLayout.addWidget(self.labelDotCount)
        self.sliderDotCount = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.sliderDotCount.setOrientation(QtCore.Qt.Horizontal)
        self.sliderDotCount.setObjectName("sliderDotCount")
        self.verticalLayout.addWidget(self.sliderDotCount)

        self.buttonDraw = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.buttonDraw.setObjectName("buttonDraw")
        self.verticalLayout.addWidget(self.buttonDraw)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Аттракторы"))
        self.controlBox.setTitle(_translate("MainWindow", "Настройки"))
        self.labelGenSpeed.setText(_translate("MainWindow", "Скорость генерации"))
        self.labelDotCount.setText(_translate("MainWindow", "Кол-во нач. точек"))
        self.buttonDraw.setText(_translate("MainWindow", "Отрисовать"))
        #self.graphicsView.setText(_translate("MainWindow", "Аттракторы"))

