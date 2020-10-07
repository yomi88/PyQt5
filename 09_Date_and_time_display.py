from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()
# 수 10 7 2020
print(now.toString())
print(type(now))
print()
# 7.10.20
print(now.toString('d.M.yy'))
# 07.10.2020
print(now.toString('dd.MM.yyyy'))
# 수.10월.2020
print(now.toString('ddd.MMMM.yyyy'))

# 2020-10-07
print(now.toString(Qt.ISODate))
# 2020년 10월 7일 수요일
print(now.toString(Qt.DefaultLocaleLongDate))
print("-" * 40)


from PyQt5.QtCore import QTime, Qt

time = QTime.currentTime()
print(time.toString())
print()
# 12.18.14
print(time.toString('h.m.s'))
# 12.18.14
print(time.toString('hh.mm.ss'))
# 12.18.14.275
print(time.toString('hh.mm.ss.zzz'))
# 오후 12:18:14
print(time.toString(Qt.DefaultLocaleLongDate))
# 오후 12:18
print(time.toString(Qt.DefaultLocaleShortDate))
print("-" * 40)


from PyQt5.QtCore import QDateTime, Qt

datetime = QDateTime.currentDateTime()
# 7.10.20 12:19:44
print(datetime.toString('d.M.yy hh:mm:ss'))
# 07.10.2020, 12:19:44
print(datetime.toString('dd.MM.yyyy, hh:mm:ss'))
# 2020년 10월 7일 수요일 오후 12:19:44
print(datetime.toString(Qt.DefaultLocaleLongDate))
# 2020-10-07 오후 12:19
print(datetime.toString(Qt.DefaultLocaleShortDate))
print("-" * 40)


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt, QTime, QDateTime

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()
        self.datetime = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        # self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        # self.statusBar().showMessage(self.time.toString(Qt.DefaultLocaleLongDate))
        self.statusBar().showMessage(self.datetime.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
