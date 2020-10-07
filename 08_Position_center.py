import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self): # 클래스 열면 무조건 초기에 실행
        super().__init__()
        self.initUI()   # 클래스 열어 이닛이 실행하면서 실행하라고 있는 녀석

    def initUI(self):
        self.setWindowTitle('Centering')    # 제목
        self.resize(500, 350)   # 창 사이즈
        self.center()   # 화면 가운데 위치하게 하는 메서드
        self.show()     # 창을 보여주라는 메서드

    def center(self):   # center 메서드 생성
        qr = self.frameGeometry()   # 창의 위치와 크기 정보를 가져옴.
        print(qr)
        # 사용하는 모니터 화면의 가운데 위치가 어디인지 파악
        # 아래껄로 위치 잡으면 왼쪽 위 모서리 기준으로 잡힘
        cp = QDesktopWidget().availableGeometry().center()
        print(cp)
        # 그래서 모서리 기준을 창의 센터로 잡음
        qr.moveCenter(cp)
        print(qr)
        self.move(qr.topLeft())
        print(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
