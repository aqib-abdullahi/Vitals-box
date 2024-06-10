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
        devices = QComboBox()
        # test device hardcode
        devices.addItem('---')
        devices.addItem('device 1')
        devices.addItem('device 2')

        # combobox style (dropdown list styling)
        devices.setStyleSheet(" font-size: 17px; font-weight: bold; "
                             "qproperty-alignment: AlignCenter; font-family: Arial;")

        # adds devices list to widget
        layout.addWidget(devices, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        devices.setFixedSize(500, 25)

        #buttons (backward and forward)
        nav_buttons = QHBoxLayout()
        nav_buttons.addStretch(3)
        next_button = QPushButton("Next >")
        next_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                           "qproperty-alignment: AlignLeft; font-family: Arial;")
        nav_buttons.addWidget(next_button)
        layout.addLayout(nav_buttons)

        # forward button action
        next_button.clicked.connect(self.next_window)

        # center
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        # index of selected item
        devices.currentIndexChanged.connect(self.index_changed)
        # text of selected item
        devices.currentTextChanged.connect(self.text_changed)

        self.device_name = ""

    def index_changed(self, i):
        """i is an int"""
        print(i)

    def text_changed(self, s):
        """s is a string"""
        self.device_name = s
        print(s)

    def next_window(self):
        """shows name window when next is clicked
        """
        from app.ui.widgets.fullname import FullName
        name_window = FullName()
        if not name_window.isVisible():
            self.hide()
            name_window.show()