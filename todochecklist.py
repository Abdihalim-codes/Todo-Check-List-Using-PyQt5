import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        loadUi(r"C:\Users\cabdo\Desktop\Python-GUI-Projects\GUI-Todo-Checklist\main.ui", self)
        
        # Set window title
        self.setWindowTitle("Todo Checklist")

        # Set window icon
        self.setWindowIcon(QtGui.QIcon("menu-burger.png"))

        # Set window size policy
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        # Set minimum window size
        self.setMinimumSize(QSize(600, 400))

        # Set maximum window size
        self.setMaximumSize(QSize(800, 600))

        # Center the window on the screen
        screen_geometry = QApplication.desktop().availableGeometry()
        window_geometry = self.geometry()
        self.move((screen_geometry.width() - window_geometry.width()) // 2,
                  (screen_geometry.height() - window_geometry.height()) // 2)

        # Populate the todo list
        todos = ["Walk dog", "Buy groceries", "Send email", "Call bank", "Clean house"]
        for todo in todos:
            item = QListWidgetItem(todo)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.listWidget.addItem(item)

        # Connect the add button to a function
        self.pushButton.clicked.connect(self.toggle_all)

    def toggle_all(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
            else:
                item.setCheckState(QtCore.Qt.Checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())