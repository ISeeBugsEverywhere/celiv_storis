import sys, os
from PyQt5.QtWidgets import *
from GUI.UI import Ui_MainWindow
import configparser

cpath="Config/cfg.ini"

class mainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # signals:
        self.ui.exit_action.triggered.connect(self.exit_fn)
        self.ui.exit_btn.clicked.connect(self.exit_fn)
        self.ui.calculate_btn.clicked.connect(self.calculate_fn)
        self.load_config()

    def load_config(self):
        cp = configparser.ConfigParser()
        cp.read(cpath)
        section="PARAMS"
        s = cp[section]["s"]
        sb = cp[section]["sb"]
        epsilon = cp[section]["epsilon"]
        r = cp[section]["r"]
        rb = cp[section]["rb"]
        u = cp[section]["u"]
        ub = cp[section]["ub"]
        u0 = cp[section]["u0"]
        u0b = cp[section]["u0b"]
        timp = cp[section]["timp"]
        timpb = cp[section]["timpb"]
        self.ui.sBox.setValue(float(s))
        self.ui.sCombo.setCurrentIndex(int(sb))
        self.ui.epsilonBox.setValue(float(epsilon))
        self.ui.rBox.setValue(float(r))
        self.ui.rCombo.setCurrentIndex(int(rb))
        self.ui.uBox.setValue(float(u))
        self.ui.uCombo.setCurrentIndex(int(ub))
        self.ui.u0Box.setValue(float(u0))
        self.ui.u0Combo.setCurrentIndex(int(u0b))
        self.ui.timpBox.setValue(float(timp))
        self.ui.timpCombo.setCurrentIndex(int(timpb))
        pass

    def save_config(self):
        pass


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