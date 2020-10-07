import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    # 메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar

    # -----------------------------
    # | Menu Bar                  |
    # -----------------------------
    # | Toolbars                  |
    # -----------------------------
    # |     Dock Widgets          |
    # |    -------------------    |
    # |    |                 |    |
    # |    | Central Widget  |    |
    # |    |                 |    |
    # |    -------------------    |
    # |                           |
    # -----------------------------
    # | Status Bar                |
    # -----------------------------

    def initUI(self):
        self.statusBar().showMessage('Ready')   # 상태바에 표시할 내용
        self.setWindowTitle('Statusbar')    # 타이틀
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())