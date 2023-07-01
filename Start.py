#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 22:44
# @Author  : FywOo02
# @FileName: Start.py
# @Software: PyCharm

from MainWidget import MainWidget
from PyQt5.QtWidgets import QApplication

import sys


def main():
    app = QApplication(sys.argv)

    mainWidget = MainWidget()  # Create a new main screen
    mainWidget.show()  # Show main screen

    exit(app.exec_())  # Enter the message loop


if __name__ == '__main__':
    main()

