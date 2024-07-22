import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


def suppress_qt_warnings():  # 해상도별 글자크기 강제 고정하는 함수
    os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"


if __name__ == "__main__":

    suppress_qt_warnings()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
