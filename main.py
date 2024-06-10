#!/usr/bin/env python3
"""entry point"""
from PyQt6.QtWidgets import QApplication
from app.ui.main_window import MainWindow


def run() -> int:
    """runs app entry point"""
    app = QApplication([])
    window = MainWindow()
    window.show()
    return sys.exit(app.exec())


if __name__ == '__main__':
    import sys
    sys.exit(run())
