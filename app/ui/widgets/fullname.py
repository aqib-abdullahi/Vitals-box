#!/usr/bin/env python3
"""full name window"""
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QWidget,
                             QLineEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QFormLayout
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

        self.form = QFormLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText("Enter full name")
        self.name.setStyleSheet(" font-size: 14px; font-weight: bold; "
                              "qproperty-alignment: AlignLeft; font-family: Arial;")
        self.name.setFixedSize(360, 30)

        self.form.addRow("Full name:  ", self.name)

        # adds name edit to layout
        self.form.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(self.form)

        # buttons (backward and forward)
        self.nav_buttons = QHBoxLayout()
        self.nav_buttons.addStretch(3)
        self.back_button = QPushButton("< Back")
        self.next_button = QPushButton("Next >")
        self.nav_buttons.addWidget(self.back_button)
        self.nav_buttons.addWidget(self.next_button)

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

        self.name_input = None
        self.prev_window = None
        self.next_date_window = None
        self.last_information_window = None

    def name_text(self):
        """text from the text holder"""
        self.name_input = self.name.displayText()
        print("Fullname: ", self.name_input)
        return self.name_input

    def set_device_previous_window(self, prev_window):
        """set devices window
        """
        self.prev_window = prev_window
        self.back_button.clicked.connect(self.show_device_previous_window)

    def show_device_previous_window(self):
        """shows previous window"""
        self.close()
        self.prev_window.show()

    def set_date_next_window(self, next_date_window, last_information_window):
        """sets the date window"""
        self.next_date_window = next_date_window
        self.last_information_window = last_information_window
        self.next_button.clicked.connect(self.show_date_next_window)

    def show_date_next_window(self):
        """show the date window as next"""
        self.last_information_window.update_name(self.name_text())
        self.close()
        self.next_date_window.show()