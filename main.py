#!/usr/bin/env python3
"""entry point"""
from PyQt6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.ui.widgets.devices_list import DevicesWindow
from app.ui.widgets.fullname import FullName
from app.ui.widgets.date_of_birth import DateOfBirth
from app.ui.widgets.gender import Gender
from app.ui.widgets.weight import Weight
from app.ui.widgets.information import Information
from app.ui.widgets.measurement import Measurement


def run() -> int:
    """runs app entry point"""
    app = QApplication([])
    main_window = MainWindow()
    device_window = DevicesWindow()
    fullname_window = FullName()
    date_of_birth_window = DateOfBirth()
    gender_window = Gender()
    weight_window = Weight()
    information_window = Information()
    measurement_window = Measurement()

    main_window.set_device_next_window(device_window)
    device_window.set_name_next_window(fullname_window)
    fullname_window.set_device_previous_window(device_window)
    fullname_window.set_date_next_window(date_of_birth_window)
    date_of_birth_window.set_fullname_previous_window(fullname_window)
    date_of_birth_window.set_gender_next_window(gender_window)
    gender_window.set_date_previous_window(date_of_birth_window)
    gender_window.set_weight_next_window(weight_window)
    weight_window.set_gender_previous_window(gender_window)
    weight_window.set_information_next_window(information_window)
    information_window.set_weight_previous_window(weight_window)
    information_window.set_measurement_next_window(measurement_window)

    main_window.show()
    return sys.exit(app.exec())


if __name__ == '__main__':
    import sys
    sys.exit(run())