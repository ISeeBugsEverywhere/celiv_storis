import sys, os
from PyQt5.QtWidgets import *
from GUI.UI import Ui_MainWindow
import configparser

class mainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # signals:
        self.ui.exit_action.triggered.connect(self.exit_fn)
        self.ui.exit_btn.clicked.connect(self.exit_fn)
        self.ui.calculate_btn.clicked.connect(self.calculate_fn)


    def calculate_fn(self):
        """
        calculates d, in μmeters
        :return:
        """
        txt = "D in μm"
        self.ui.answer_label.setText(txt)
        pass

    def exit_fn(self):
        print("exiting...")
        app.exit(42)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainUi()
    window.show()
    sys.exit(app.exec_())