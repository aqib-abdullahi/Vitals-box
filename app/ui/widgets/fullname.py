#!/usr/bin/env python3
"""full name window"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QScreen
from PyQt6.QtWidgets import (QWidget,
                             QLineEdit,
                             QComboBox,
                             QVBoxLayout,
                             QHBoxLayout,
                             QLabel,
                             QApplication,
                             QPushButton
                             )


class FullName(QWidget):
    """full name space to fill
    """
    def __init__(self):
        """initializes the window"""
        super().__init__()

        self.setWindowTitle("Enter full name")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.name = QLineEdit()
        self.name.setPlaceholderText("Fullname")
        self.name.setStyleSheet(" font-size: 17px; font-weight: bold; "
                              "qproperty-alignment: AlignLeft; font-family: Arial;")
        self.name.setFixedSize(370, 40)

        # adds name edit to layout
        layout.addWidget(self.name, alignment=Qt.AlignmentFlag.AlignCenter)

        # buttons (backward and forward)
        self.nav_buttons = QHBoxLayout()
        self.nav_buttons.addStretch(3)
        self.back_button = QPushButton("< Back")
        self.next_button = QPushButton("Next >")
        self.nav_buttons.addWidget(self.back_button)
        self.nav_buttons.addWidget(self.next_button)

        #next button action
        self.next_button.clicked.connect(self.text)

        # style buttons
        self.next_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")
        self.back_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")

        # adds button to layout
        layout.addLayout(self.nav_buttons)

        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        self.prev_window = None

    def text(self, s):
        """text from the text holder"""
        print(self.name.displayText())

    def set_device_previous_window(self, prev_window):
        """set devices window
        """
        self.prev_window = prev_window
        self.back_button.clicked.connect(self.show_device_previous_window)

    def show_device_previous_window(self):
        """shows previous window"""
        self.hide()
        self.prev_window.show()