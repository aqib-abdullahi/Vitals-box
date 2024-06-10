#!/usr/bin/env python3
"""combo box of devices list"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QScreen
from PyQt6.QtWidgets import (QWidget,
                             QComboBox,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel,
                             QApplication,
                             QPushButton
                             )


class DevicesWindow(QWidget):
    """Window for selecting a device
    from a list of available devices
    """
    def __init__(self):
        """initializes window"""
        super().__init__()

        self.setWindowTitle("select a device")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Please select a device:")
        self.label.setStyleSheet(" font-size: 17px; qproperty-alignment: AlignCenter; font-family: Helvetica;")
        layout.addWidget(self.label)

        #buttons
        self.buttons = QHBoxLayout()
        self.setLayout(self.buttons)
        self.next_button = QPushButton("Next >")
        self.back_button = QPushButton("< Back")
        # self.buttons.addWidget(self.next_button,alignment=Qt.AlignmentFlag.AlignCenter)

        widget = QComboBox()
        # test device hardcode
        widget.addItem('device 1')
        widget.addItem('device 2')
        widget.addItem('device 3')

        # index of selected item
        widget.currentIndexChanged.connect(self.index_changed)
        # text of selected item
        widget.currentTextChanged.connect(self.text_changed)

        layout.addWidget(widget)

        layout.addWidget(self.back_button)
        layout.addWidget(self.next_button)

        # center
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())


    def index_changed(self, i):
        """i is an int"""
        print(i)

    def text_changed(self, s):
        """s is a string"""
        print(s)