import sys
import random

from PyQt6 import uic
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.x = 400
        self.y = 250
        self.pushButton.clicked.connect(lambda x: self.update())

    def initUi(self):
        self.setGeometry(0, 0, 600, 600)
        self.circle = False

    def paintEvent(self, event):
        self.side = random.randint(20, 400)
        paint = QPainter(self)
        brush = QBrush(QColor(255, 255, 0))
        paint.setBrush(brush)
        paint.drawEllipse(self.x - self.side, self.y - self.side, self.side * 2, self.side * 2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())