import sys
# QtWidgets 에는 기본적인 UI 구성요소를 제공하는 위젯 클래스 들이 포함되어 있다.
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Icon') # 창의 타이틀
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 300, 200)    # 창의 위치와 크기 설정 (위치x, 위치y, 크기x, 크기y)
        self.show() # 창 오픈
        # 여기서 창은 위젯이라고 한다.


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())