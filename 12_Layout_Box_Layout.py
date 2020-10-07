# 박스 레이아웃 클래스를 이용하면 유연하고 실용적인 레이아웃을 할 수 있다.
# QHBoxLayout 수평으로 박스 정렬
# QVBoxLayout 수직으로 박스 정렬
# addStretch() 메서드로 필요한 공간을 만든다.
# stretch factor 로 조절한다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 생성
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        # 수평구조, 왼쪽부터 순서대로 배치되니 아래 코딩시 고려하라
        hbox = QHBoxLayout()
        # 신축성 있는 빈공간 제공
        hbox.addStretch(1)  # 수평으로 1만큼 공간 (왼)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)  # 수평으로 1만큼공간 (오)

        vbox = QVBoxLayout()
        vbox.addStretch(3)  # 수직으로 3만큼 공간 (위)
        # 수평박스를 수직박스에 넣어주는 것
        vbox.addLayout(hbox)
        vbox.addStretch(1)  # 수직으로 1만큼 공간 (아래)

        self.setLayout(vbox)    # 위에서 세팅한 레이아웃을 실행
        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())