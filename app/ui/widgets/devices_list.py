#!/usr/bin/env python3
"""combo box of devices list"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
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

        # window specs
        self.setWindowTitle("Select a device")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # styling dropdown label
        self.label = QLabel("Please select a device:")
        self.label.setStyleSheet(" font-size: 17px; font-weight: bold; "
                                 "qproperty-alignment: AlignCenter; font-family: Arial;")

        # adds label to layout
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        # dropdown list of devices
        self.devices = QComboBox()
        # test device hardcode
        self.devices.addItem('---')
        self.devices.addItem('device 1')
        self.devices.addItem('device 2')

        # combobox style (dropdown list styling)
        self.devices.setStyleSheet(" font-size: 17px; font-weight: bold; "
                             "qproperty-alignment: AlignCenter; font-family: Arial;")

        # adds devices list to widget
        layout.addWidget(self.devices, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.devices.setFixedSize(500, 25)

        #buttons (backward and forward)
        self.nav_buttons = QHBoxLayout()
        self.nav_buttons.addStretch(3)
        self.next_button = QPushButton("Next >")
        self.next_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                           "qproperty-alignment: AlignLeft; font-family: Arial;")
        self.nav_buttons.addWidget(self.next_button)
        layout.addLayout(self.nav_buttons)


        # center
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        self.device_name = ""
        self.next_win = None

    def index_changed(self):
        """i is an int"""
        print("Device index: ", self.devices.currentIndex())

    def text_changed(self):
        """s is a string"""
        print("Device name: ",self.devices.currentText())
        self.device_name = self.devices.currentText()

    def set_name_next_window(self, next_win):
        """set name window when
        """
        self.next_win = next_win
        self.next_button.clicked.connect(self.show_name_next_window)

    def show_name_next_window(self):
        """shows the next window"""
        self.close()
        self.next_win.show()
        self.index_changed()
        self.text_changed()