#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 22:39
# @Author  : FywOo02
# @FileName: PaintBoard.py
# @Software: PyCharm

from PyQt5.QtWidgets import QWidget
from PyQt5.Qt import QPixmap, QPainter, QPoint, QPaintEvent, QMouseEvent, QPen, \
    QColor, QSize
from PyQt5.QtCore import Qt


class PaintBoard(QWidget):

    def __init__(self, Parent=None):
        '''
        Constructor
        '''
        super().__init__(Parent)

        self.__InitData()  # Initialize data first, then initialize the interface
        self.__InitView()

    def __InitData(self):

        self.__size = QSize(640, 480)

        # Create a new QPixmap as a drawing board with the size __size
        self.__board = QPixmap(self.__size)
        self.__board.fill(Qt.white)  # Fill the panel with white

        self.__IsEmpty = True  # Default is empty drawing board
        self.EraserMode = False  # Default is to disable eraser mode

        self.__lastPos = QPoint(0, 0)  # Last mouse position
        self.__currentPos = QPoint(0, 0)  # Current mouse position

        self.__painter = QPainter()  # New drawing tool

        self.__thickness = 20  # Default brush thickness is 10px
        self.__penColor = QColor("black")  # Set the default brush color to black
        self.__colorList = QColor.colorNames()  # Get a list of colors

    def __InitView(self):
        # Set the size of the interface to __size
        self.setFixedSize(self.__size)

    def Clear(self):
        # clear panel
        self.__board.fill(Qt.white)
        self.update()
        self.__IsEmpty = True

    def ChangePenColor(self, color="black"):
        # change the color of pen
        self.__penColor = QColor(color)

    def ChangePenThickness(self, thickness=20):
        # change the thickness of pen
        self.__thickness = thickness

    def IsEmpty(self):
        # return if panel is empty
        return self.__IsEmpty

    def GetContentAsQImage(self):
        # Get the contents of the drawing board (return QImage)
        image = self.__board.toImage()
        return image

    def paintEvent(self, paintEvent):
        # Paint events
        # An instance of QPainter must be used when drawing, in this case __painter
        # The drawing is done between the begin() function and the end() function
        # begin(param) parameter to specify the drawing device, i.e. where to draw the map
        # drawPixmap is used to draw objects of type QPixmap
        self.__painter.begin(self)
        # 0,0 are the coordinates of the starting point of the upper left corner of the drawing, __board is the
        # drawing to be drawn
        self.__painter.drawPixmap(0, 0, self.__board)
        self.__painter.end()

    def mousePressEvent(self, mouseEvent):
        # When the mouse is pressed, get the current position of the mouse and save it as the last position
        self.__currentPos = mouseEvent.pos()
        self.__lastPos = self.__currentPos

    def mouseMoveEvent(self, mouseEvent):
        # Update the current position when the mouse moves and draw a line between the previous position and the current position
        self.__currentPos = mouseEvent.pos()
        self.__painter.begin(self.__board)

        if self.EraserMode == False:
            # Non-eraser mode
            self.__painter.setPen(QPen(self.__penColor, self.__thickness))  # Set brush color, thickness
        else:
            # The brush in eraser mode is pure white with a thickness of 10
            self.__painter.setPen(QPen(Qt.white, 10))

        # draw a line
        self.__painter.drawLine(self.__lastPos, self.__currentPos)
        self.__painter.end()
        self.__lastPos = self.__currentPos

        self.update()  # Update display

    def mouseReleaseEvent(self, mouseEvent):
        self.__IsEmpty = False  # The drawing board is no longer empty

