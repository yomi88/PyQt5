import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        btn = QPushButton('Quit', self) # '버튼의 글씨'로 버튼 생성
        btn.move(100, 100)  # 버튼의 위치
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)   # 클릭하면 하는 행위, 여긴 quit로 꺼지게 함.

        # PyQt5에서의 이벤트 처리는 '시그널'과 '슬롯' 메커니즘으로 이루어진다.
        # 버튼(btn)을 클릭하면 'clicked' 시그널이 만들어진다.
        # instance() 메서드는 현재 인스턴스를 반환한다.
        # 'clicked' 시그널은 어플리케이션을 종료하는 quit() 메서드에 연결된다.
        # 발신자(Sender)와 수신자(Receiver), 두 객체 간에 커뮤니케이션이 이루어진다.
        # 예제에서 발신자는 푸시버튼인 'btn' 이고, 수신자는 어플리케이션 객체인 'app' 이다.

        self.setWindowTitle('Quit Button')  # 프로그램 타이틀
        self.setGeometry(500, 100, 500, 500)    # 위치x, 위치y, 크기x, 크기y
        self.show()


if __name__ == '__main__':

   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())