from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import sqlite3
import sys


class All(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        con = sqlite3.connect("release/data/coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM characteristic""").fetchall()
        result = list(map(lambda x: list(x), result))

        r = ''''''

        for i in result:
            res = f'{str(i[0])}). {i[1]}, прожарка {i[2]}, тип кофе {i[3]}, цена {i[4]} руб, описание: {i[5]}, вес {i[6]} кг'
            r += res + '\n' + '\n'

        self.information.setPlainText(r)


class Add(QWidget, All):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = All()
    w.show()
    sys.exit(app.exec_())
