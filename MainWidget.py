#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 22:39
# @Author  : FywOo02
# @FileName: MainWidget.py
# @Software: PyCharm

from PyQt5.Qt import QWidget, QColor, QPixmap, QIcon, QSize, QCheckBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QSplitter, \
    QComboBox, QLabel, QSpinBox, QFileDialog
from PaintBoard import PaintBoard

import tensorflow as tf
import numpy as np
try:
    import tensorflow.python.keras as keras
except:
    import tensorflow.keras as keras


class MainWidget(QWidget):

    def __init__(self, Parent=None):
        '''
        Constructor
        '''
        super().__init__(Parent)

        self.__InitData()  # init data
        self.__InitView()  # init view

    def __InitData(self):
        '''
                  init members
        '''
        self.__paintBoard = PaintBoard(self)
        # get the color list
        self.__colorList = QColor.colorNames()

    def __InitView(self):
        '''
                  init view
        '''
        self.setFixedSize(640, 480)
        self.setWindowTitle("Handwritten Digit Recognition")

        # Create a new horizontal layout as the main layout of this form
        main_layout = QHBoxLayout(self)

        # Set the main layout inner margin and control spacing to 10px
        main_layout.setSpacing(10)

        # Place the drawing board on the left side of the main screen
        main_layout.addWidget(self.__paintBoard)

        # Create a new vertical sublayout for placing keys
        sub_layout = QVBoxLayout()

        # Set the spacing between this child layout and the internal controls to 5px
        sub_layout.setContentsMargins(5, 5, 5, 5)

        splitter = QSplitter(self)
        sub_layout.addWidget(splitter)

        self.__btn_Recognize = QPushButton("Start Recognition")
        self.__btn_Recognize.setParent(self)
        self.__btn_Recognize.clicked.connect(self.on_btn_Recognize_Clicked)
        sub_layout.addWidget(self.__btn_Recognize)

        self.__btn_Clear = QPushButton("Clear")
        self.__btn_Clear.setParent(self)  # Set the parent object as the interface

        # Associating key press signals with the drawing board clear function
        self.__btn_Clear.clicked.connect(self.__paintBoard.Clear)
        sub_layout.addWidget(self.__btn_Clear)

        self.__btn_Quit = QPushButton("Quit")
        self.__btn_Quit.setParent(self)  # Set the parent object as the interface
        self.__btn_Quit.clicked.connect(self.Quit)
        sub_layout.addWidget(self.__btn_Quit)

        self.__btn_Save = QPushButton("Save")
        self.__btn_Save.setParent(self)
        self.__btn_Save.clicked.connect(self.on_btn_Save_Clicked)
        sub_layout.addWidget(self.__btn_Save)

        self.__cbtn_Eraser = QCheckBox("Eraser")
        self.__cbtn_Eraser.setParent(self)
        self.__cbtn_Eraser.clicked.connect(self.on_cbtn_Eraser_clicked)
        sub_layout.addWidget(self.__cbtn_Eraser)

        self.__label_penThickness = QLabel(self)
        self.__label_penThickness.setText("Thickness")
        self.__label_penThickness.setFixedHeight(20)
        sub_layout.addWidget(self.__label_penThickness)

        self.__spinBox_penThickness = QSpinBox(self)
        self.__spinBox_penThickness.setMaximum(20)
        self.__spinBox_penThickness.setMinimum(10)
        self.__spinBox_penThickness.setValue(20)  # Default thickness is 10
        self.__spinBox_penThickness.setSingleStep(5)  # Minimum change value of 2
        self.__spinBox_penThickness.valueChanged.connect(
            self.on_PenThicknessChange)  # Associated spinBox value change signal and function on_PenThicknessChange
        sub_layout.addWidget(self.__spinBox_penThickness)

        self.__label_penColor = QLabel(self)
        self.__label_penColor.setText("Color")
        self.__label_penColor.setFixedHeight(20)
        sub_layout.addWidget(self.__label_penColor)

        self.__comboBox_penColor = QComboBox(self)
        self.__fillColorList(self.__comboBox_penColor)  # Fill the drop-down list with various colors
        self.__comboBox_penColor.currentIndexChanged.connect(
            self.on_PenColorChange)  # Associating the current index change signal of the drop-down list with the function on_PenColorChange
        sub_layout.addWidget(self.__comboBox_penColor)

        main_layout.addLayout(sub_layout)  # Adding child layouts to the main layout

    def __fillColorList(self, comboBox):

        index_black = 0
        index = 0
        for color in self.__colorList:
            if color == "black":
                index_black = index
            index += 1
            pix = QPixmap(70, 20)
            pix.fill(QColor(color))
            comboBox.addItem(QIcon(pix), None)
            comboBox.setIconSize(QSize(70, 20))
            comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        comboBox.setCurrentIndex(index_black)

    def on_PenColorChange(self):
        color_index = self.__comboBox_penColor.currentIndex()
        color_str = self.__colorList[color_index]
        self.__paintBoard.ChangePenColor(color_str)

    def on_PenThicknessChange(self):
        penThickness = self.__spinBox_penThickness.value()
        self.__paintBoard.ChangePenThickness(penThickness)

    def on_btn_Save_Clicked(self):
        savePath = QFileDialog.getSaveFileName(self, 'Save Your Paint', '.\\', '*.png')
        print(savePath)
        if savePath[0] == "":
            print("Save cancel")
            return
        image = self.__paintBoard.GetContentAsQImage()
        image.save(savePath[0])
        print(savePath[0])

    def on_cbtn_Eraser_clicked(self):
        if self.__cbtn_Eraser.isChecked():
            self.__paintBoard.EraserMode = True  # Enter eraser mode
        else:
            self.__paintBoard.EraserMode = False  # Exit eraser mode


    def on_btn_Recognize_Clicked(self):
        savePath = "./PNG/text.png"
        image = self.__paintBoard.GetContentAsQImage()
        image.save(savePath)
        print(savePath)
        # load graph
        img = tf.keras.preprocessing.image.load_img(savePath, target_size=(28, 28))
        img = img.convert('L')
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = abs(255 - x)
        # x = x.reshape(28,28)
        x = np.expand_dims(x, axis=0)
        x = x / 255.0
        new_model = keras.models.load_model("./model.h5")
        prediction = new_model.predict(x)
        output = np.argmax(prediction, axis=1)
        print("Handwritten numeric recognition as：" + str(output[0]))


    def Quit(self):
        self.close()
