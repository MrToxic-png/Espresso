import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem


class Table(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        r = cur.execute("""SELECT * FROM Coffee""").fetchall()
        for i in range(len(r)):
            for n in range(len(r[i])):
                self.table.setItem(i, n, QTableWidgetItem(str(r[i][n])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    sys.exit(app.exec())
