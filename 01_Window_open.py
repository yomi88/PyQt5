import sys
from PyQt5.QtWidgets import QApplication, QWidget
# QtWidgets 에는 기본적인 UI 구성요소를 제공하는 위젯 클래스 들이 포함되어 있다.

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application') # 창의 타이틀
        self.move(1500, 100)    # 창이 나타나는 위치 (모니터에서) 좌에서 우로, 위에서 아래로
        self.resize(500, 300)   # 창 사이즈
        self.show() # 창 오픈
        # 여기서 창은 위젯이라고 한다.

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
