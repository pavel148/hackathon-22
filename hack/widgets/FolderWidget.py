from enum import Enum, auto
from typing import List

from PySide2.QtCore import QObject, Qt
from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem


class FolderWidget(QTreeWidget):
    class ViewType(Enum):
        Tree = auto()
        Folder = auto()

    def __init__(self, parent: QObject = None):
        super().__init__(parent)

        self.setHeaderLabels(["Name", "1", "2", "3", "4", "5", "6", "7"])
        self.setWindowTitle("Data view")

    def load_data(self, data: List[List[str]], view_type: ViewType):
        if view_type == FolderWidget.ViewType.Tree:
            self.__load_tree(data)
        else:
            self.__load_folders(data)

        self.sortItems(0, Qt.SortOrder.AscendingOrder)

    def __load_tree(self, data: List[List[str]]):
        tree = {line[1]: QTreeWidgetItem([line[1].split("-")[-1]] + [item.split("-")[0] for item in line[3:]]) for line in data}

        for line in data:
            if len(line[2]) != 0:
                tree[line[2]].addChild(tree[line[1]])

        root = QTreeWidgetItem(self, ["root"])
        root.addChildren([tree[line[1]] for line in data if len(line[2]) == 0])

    def __load_folders(self, data: List[List[str]]):
        folder_paths = {line[1][:line[1].rfind("-")] for line in data if line[1].rfind("-") != -1}
        folders = {path: QTreeWidgetItem([path if path.rfind("-") == -1 else path[path.rfind("-") + 1:]]) for path in folder_paths}

        root = QTreeWidgetItem(self, ["root"])

        for folder, item in folders.items():
            if folder.rfind("-") == -1:
                root.addChild(item)
            else:
                folders[folder[:folder.rfind("-")]].addChild(item)

        for line in data:
            if line[1].rfind("-") != -1:
                folders[line[1][:line[1].rfind("-")]].addChild(QTreeWidgetItem([line[1].split("-")[-1]] + [item.split("-")[0] for item in line[3:]]))
            else:
                root.addChild(QTreeWidgetItem([line[1].split("-")[-1]] + [item.split("-")[0] for item in line[3:]]))
