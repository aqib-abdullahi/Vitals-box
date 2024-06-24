#!/usr/bin/env python3
"""Entire information window"""
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import (QWidget,
                             QLineEdit,
                             QVBoxLayout,
                             QHBoxLayout,
                             QApplication,
                             QPushButton,
                             QFormLayout
                             )


class Information(QWidget):
    """weight option to set
    """
    def __init__(self):
        """initializes the window"""
        super().__init__()

        self.setWindowTitle("Information")
        self.setGeometry(0, 0, 600, 400)
        self.setMinimumWidth(400)
        self.setMinimumHeight(60)
        self.setMaximumSize(700, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.form = QFormLayout()

        self.name = QLineEdit()
        self.name.setEnabled(False)

        self.date_of_birth = QLineEdit()
        self.date_of_birth.setEnabled(False)

        self.gender = QLineEdit()
        self.gender.setEnabled(False)

        self.weight = QLineEdit()
        self.weight.setEnabled(False)

        # form style (dropdown list styling)
        self.name.setStyleSheet(" font-size: 12px; font-weight: bold; "
                              "qproperty-alignment: AlignCenter; font-family: Arial;")
        self.name.setFixedSize(250,25)

        self.date_of_birth.setStyleSheet(" font-size: 12px; font-weight: bold; "
                           "qproperty-alignment: AlignCenter; font-family: Arial;")
        self.date_of_birth.setFixedSize(250, 25)

        self.gender.setStyleSheet(" font-size: 12px; font-weight: bold; "
                           "qproperty-alignment: AlignCenter; font-family: Arial;")
        self.gender.setFixedSize(250, 25)

        self.weight.setStyleSheet(" font-size: 12px; font-weight: bold; "
                           "qproperty-alignment: AlignCenter; font-family: Arial;")
        self.weight.setFixedSize(250, 25)


        self.form.addRow("Name:   ", self.name)
        self.form.addRow("Date of birth:   ", self.date_of_birth)
        self.form.addRow("Gender:   ", self.gender)
        self.form.addRow("Weight:   ", self.weight)
        self.form.setFormAlignment(Qt.AlignmentFlag.AlignCenter)

        # adds name edit to layout
        layout.addLayout(self.form)

        # buttons (backward and forward)
        self.nav_buttons = QHBoxLayout()
        self.nav_buttons.addStretch(3)
        self.back_button = QPushButton("< Back")
        self.next_button = QPushButton("Start measurement")
        self.nav_buttons.addWidget(self.back_button)
        self.nav_buttons.addWidget(self.next_button)

        # style buttons
        self.next_button.setStyleSheet(" font-size: 13px; font-weight: bold; "
                                  "qproperty-alignment: AlignLeft; font-family: Arial;")
        self.next_button.setFixedWidth(180)
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
        self.next_measurement_window = None

    def set_weight_previous_window(self, prev_window):
        """set devices window
        """
        self.prev_window = prev_window
        self.back_button.clicked.connect(self.show_weight_previous_window)

    def show_weight_previous_window(self):
        """shows previous window"""
        self.hide()
        self.prev_window.show()

    def set_measurement_next_window(self, next_measurement_window):
        """sets the gender window"""
        self.next_measurement_window = next_measurement_window
        self.next_button.clicked.connect(self.show_measurement_next_window)

    def show_measurement_next_window(self):
        """show the date window as next"""
        self.hide()
        self.next_measurement_window.show()

    def update_name(self, name):
        """update name space"""
        self.name.setText(name)

    def update_dob(self, date_of_birth):
        """update date of birth space"""
        self.date_of_birth.setText(date_of_birth)

    def update_gender(self, gender):
        """update gender space"""
        self.gender.setText(gender)

    def update_weight(self, weight):
        """update weight space"""
        self.weight.setText(weight)
