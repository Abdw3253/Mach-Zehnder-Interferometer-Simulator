from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton


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