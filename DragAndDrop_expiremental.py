from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag

class DragButton(QPushButton):

    def mouseMoveEvent(self, e):

        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)
            drag.exec_(Qt.MoveAction)
            
class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.blayout = QHBoxLayout()
        for l in ['A', 'B', 'C', 'D']:
            btn = QPushButton(l)
            self.blayout.addWidget(btn)

        self.setLayout(self.blayout)


app = QApplication([])
w = Window()
w.show()

app.exec_()