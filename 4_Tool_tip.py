import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self) # '버튼의 글씨'로 버튼 생성
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(100, 100)  # 버튼의 위치
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')  # 프로그램 타이틀
        self.setGeometry(500, 100, 500, 500)    # 위치x, 위치y, 크기x, 크기y
        self.show()


if __name__ == '__main__':

   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())