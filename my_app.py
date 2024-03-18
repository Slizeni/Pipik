# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
app = QApplication([])
main = QWidget()
main.setWindowTitle('Определитель победителя')
but = QPushButton('Сгенерировать')
text = QLabel('Нажми чтобы узнать победителя')
winner = QLabel('?')
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main.setLayout(line)
main.show()
app.exec_()