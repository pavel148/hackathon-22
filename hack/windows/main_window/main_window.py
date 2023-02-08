import csv
from typing import List, Optional

from PySide2.QtWidgets import QMainWindow, QWidget

from widgets.FolderWidget import FolderWidget
from windows.main_window.main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__opened_window: Optional[QWidget] = None
        self.__data: Optional[List[List[str]]] = []

        self.__load_data()

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__setup_listeners()

    def __setup_listeners(self):
        self.__ui.treePushButton.clicked.connect(lambda: self.__view_data(FolderWidget.ViewType.Tree))
        self.__ui.folderPushButton.clicked.connect(lambda: self.__view_data(FolderWidget.ViewType.Folder))

    def __load_data(self):
        for i in range(1, 11):
            with open(f"data/{i:02}.csv") as file:
                self.__data.extend(csv.reader(file))

    def __view_data(self, view_type: FolderWidget.ViewType):
        self.__opened_window = FolderWidget()
        self.__opened_window.load_data(self.__data, view_type)
        self.__opened_window.show()
