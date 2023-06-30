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

    mainWidget = MainWidget()  # 新建一个主界面
    mainWidget.show()  # 显示主界面

    exit(app.exec_())  # 进入消息循环


if __name__ == '__main__':
    main()

