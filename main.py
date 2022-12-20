# https://github.com/AmirHusnutdinov/coffee1.git
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
con = sqlite3.connect("coffee.db")
cur = con.cursor()
result = cur.execute("""SELECT * FROM coffe""").fetchall()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setHorizontalHeaderLabels(["id", "Название сорта", "Степень обжарки",
                                                    "Молотый/В зернах", "Описание",
                                                    "Цена в руб.", "Масса в г"])
        for i in range(len(result)):
            for j in range(len(result[0])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(f"{result[i][j]}"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
