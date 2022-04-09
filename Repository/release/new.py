import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        file = "release/ui/Cof.ui"
        uic.loadUi(file, self)
        self.con = sqlite3.connect("release/data/coffee.sqlite")

        self.pushButton.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.pushButton_2.clicked.connect(self.save_results)
        self.pushButton_3.clicked.connect(self.new_coffee)
        self.save = True

        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM characteristic WHERE id=?",
                             (item_id := self.spinBox.text(),)).fetchall()
        self.tableWidget.setRowCount(1)

        if not result:
            self.statusBar().showMessage('Ничего не найдено')
            return

        else:
            self.statusBar().showMessage(f"Нашлась запись с id = {item_id}")
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE characteristic SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            que += "WHERE id = ?"
            cur.execute(que, (self.spinBox.text(),))
            self.con.commit()
            self.modified.clear()

    def new_coffee(self):
        self.save = not self.save
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM characteristic WHERE id=?",
                             (self.spinBox.text(),)).fetchall()
        result = [('', '', '', '', '', '', '')]
        self.statusBar().showMessage('Создать новую запись')

        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(7)

        self.titles = [description[0] for description in cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

        if self.save:
            cur = self.con.cursor()
            que = "INSERT INTO characteristic VALUES\n"
            que += ", ".join([f"'{self.modified.get(key)}'"
                              for key in self.modified.keys()])
            print(que)
            que += "WHERE id = ?"
            cur.execute(que, (self.spinBox.text(),))
            self.con.commit()
            self.modified.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
