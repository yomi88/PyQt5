import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        # 이건또 뭐임? , 부모 class 에서 init 가져올때 아래처럼 쓴다고 함.
        super().__init__()
        self.initUI()

    def initUI(self):

        # 라벨 위젯 생성
        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        # setStyleSheet 메서드는 CSS 를 그대로 구현한 것으로 보임.
        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 10px")
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        # QVBoxLayout() 메서드는 수직으로 박스를 구성해 준다.
        vbox = QVBoxLayout()
        # addWidget 메서드는 인덱스에 라벨 변수를 넣어주면 적용된다.
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        # 이건 무슨의미?
        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())