from PySide2.QtWidgets import QApplication

from windows.main_window.main_window import MainWindow


def main():
    app = QApplication()

    window = MainWindow()
    window.show()

    return QApplication.exec_()


if __name__ == "__main__":
    main()
