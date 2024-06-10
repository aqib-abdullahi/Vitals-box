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
        nav_buttons = QHBoxLayout()
        nav_buttons.addStretch(3)
        back_button = QPushButton("< Back")
        next_button = QPushButton("Next >")
        nav_buttons.addWidget(back_button)
        nav_buttons.addWidget(next_button)

        #next button action
        next_button.clicked.connect(self.text)
        #back button action
        back_button.clicked.connect(self.previous_window)

        # style buttons
        next_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")
        back_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")

        # adds button to layout
        layout.addLayout(nav_buttons)


        # center window
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

    def text(self, s):
        """text from the text holder"""
        print(self.name.displayText())

    def previous_window(self):
        """shows name window when next is clicked
        """
        if self.isVisible():
            self.hide()
            from app.ui.widgets.devices_list import DevicesWindow
            prev_window = DevicesWindow()
            prev_window.show()

    # def next_window(self):
    #     """shows name window when next is clicked
    #     """
    #     if not self.name_window.isVisible():
    #         self.hide()
    #         self.name_window.show()
