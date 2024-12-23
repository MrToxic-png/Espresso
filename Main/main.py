import sqlite3
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from UI import Add, Edit, mainWindow, addEditCoffeeForm


class EditWindow(QDialog, Edit.Ui_Dialog):
    def __init__(self, parent, flags):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.edit.clicked.connect(self.edit_elem)
        con = sqlite3.connect("../data/coffee.sqlite")
        cur = con.cursor()
        r = cur.execute("""SELECT * FROM Coffee""").fetchall()
        self.table.setRowCount(len(r))
        for i in range(len(r)):
            for n in range(len(r[i])):
                self.table.setItem(i, n, QTableWidgetItem(str(r[i][n])))

    def edit_elem(self):
        column_names = ['id', 'kind', 'power', 'type', 'taste', 'price', 'volume']
        row = self.table.currentRow()
        column = self.table.currentColumn()
        if column == 0 or self.result.text() == '':
            return
        con = sqlite3.connect("../data/coffee.sqlite")
        cur = con.cursor()
        cur.execute(f"""UPDATE Coffee
                SET {column_names[column]} = ?
                WHERE id = ?""", (str(self.result.text()), self.table.item(row, 0).text()))
        con.commit()
        self.close()


class AddWindow(QDialog, Add.Ui_Dialog):
    def __init__(self, parent, flags):
        super().__init__(parent=parent, flags=flags)
        self.setupUi(self)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.add.clicked.connect(self.add_elem)

    def add_elem(self):
        con = sqlite3.connect("../data/coffee.sqlite")
        cur = con.cursor()
        if not all([self.name.text(), self.power.text(), self.type.text(), self.taste.text(), self.price.text(),
                    self.volume.text()]):
            return
        cur.execute("""INSERT INTO Coffee(kind, power, type, taste, price, volume) VALUES(?, ?, ?, ?, ?, ?)""", (
            self.name.text(), self.power.text(), self.type.text(), self.taste.text(), self.price.text(),
            self.volume.text()))
        con.commit()
        self.close()


class AddEditCoffeeForm(QDialog, addEditCoffeeForm.Ui_addEditCoffeeForm):
    def __init__(self, parent, flags):
        super().__init__(parent=parent, flags=flags)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setupUi(self)
        self.add.clicked.connect(self.go_to_add)
        self.change.clicked.connect(self.go_to_edit)

    def go_to_add(self):
        e = AddWindow(self, Qt.WindowType.Window)
        e.show()
        self.close()

    def go_to_edit(self):
        e = EditWindow(self, Qt.WindowType.Window)
        e.show()
        self.close()


class Table(QDialog, mainWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.add_change.clicked.connect(self.change)
        self.update_butt.clicked.connect(self.go_update)

    def initUI(self):
        con = sqlite3.connect("../data/coffee.sqlite")
        cur = con.cursor()
        r = cur.execute("""SELECT * FROM Coffee""").fetchall()
        self.table.setRowCount(len(r))
        for i in range(len(r)):
            for n in range(len(r[i])):
                self.table.setItem(i, n, QTableWidgetItem(str(r[i][n])))

    def change(self):
        e = AddEditCoffeeForm(self, Qt.WindowType.Window)
        e.show()

    def go_update(self):
        con = sqlite3.connect("../data/coffee.sqlite")
        cur = con.cursor()
        r = cur.execute("""SELECT * FROM Coffee""").fetchall()
        self.table.setRowCount(len(r))
        for i in range(len(r)):
            for n in range(len(r[i])):
                self.table.setItem(i, n, QTableWidgetItem(str(r[i][n])))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table()
    ex.show()
    sys.exit(app.exec())
