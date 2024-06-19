#!/usr/bin/env python3
"""Date of birth window"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QWidget,
                             QDateEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QFormLayout
                             )


class DateOfBirth(QWidget):
    """Date of birth input window"""
    def __init__(self):
        """initialize window
        """
        super().__init__()

        self.setWindowTitle("Date Of Birth")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.date_picker = QDateEdit()
        self.date_picker.setCalendarPopup(True)
        self.date_picker.setFixedSize(150, 30)

        self.date_picker.setStyleSheet(" font-size: 17px; font-weight: bold; "
                                       "qproperty-alignment: AlignLeft; font-family: Arial;")

        self.form = QFormLayout()
        self.form.addRow("Date of Birth:  ", self.date_picker)
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

        # Center screen
        center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        self.date_input = None
        self.prev_window = None
        self.next_gender_window = None
        self.last_information_window = None

    def date_changed(self):
        """date input changed"""
        self.date_input = str(self.date_picker.date().toPyDate().strftime("%d/%m/%Y"))
        print("Date of birth: ", self.date_input)
        return self.date_input

    def set_fullname_previous_window(self, prev_window):
        """set devices window
        """
        self.prev_window = prev_window
        self.back_button.clicked.connect(self.show_fullname_previous_window)

    def show_fullname_previous_window(self):
        """shows previous window"""
        self.hide()
        self.prev_window.show()

    def set_gender_next_window(self, next_gender_window, last_information_window):
        """sets the gender window"""
        self.next_gender_window = next_gender_window
        self.last_information_window = last_information_window
        self.next_button.clicked.connect(self.show_gender_next_window)

    def show_gender_next_window(self):
        """show the date window as next"""
        self.hide()
        self.last_information_window.update_dob(self.date_changed())
        self.next_gender_window.show()