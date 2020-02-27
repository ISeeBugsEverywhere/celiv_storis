import sys, os
from PyQt5.QtWidgets import *
from GUI.UI import Ui_MainWindow
import configparser

cpath="Config/cfg.ini"
section="PARAMS"

class mainUi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # signals:
        self.ui.exit_action.triggered.connect(self.exit_fn)
        self.ui.exit_btn.clicked.connect(self.exit_fn)
        self.ui.calculate_btn.clicked.connect(self.calculate_fn)
        self.epsilon0 = 1
        self.load_config()


    def load_config(self):
        cp = configparser.ConfigParser()
        cp.read(cpath)
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
        self.epsilon0 = float(cp[section]["epsilon0"])
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
        try:
            cp = configparser.ConfigParser()
            cp.read(cpath)
            section='PARAMS'
            cp[section]["s"] = str(self.ui.sBox.value())
            cp[section]["sb"] = str(self.ui.sCombo.currentIndex())
            cp[section]["epsilon"] = str(self.ui.epsilonBox.value())
            cp[section]["r"] = str(self.ui.rBox.value())
            cp[section]["rb"] = str(self.ui.rCombo.currentIndex())
            cp[section]["u"] = str(self.ui.uBox.value())
            cp[section]["ub"] = str(self.ui.uCombo.currentIndex())
            cp[section]["u0"] = str(self.ui.u0Box.value())
            cp[section]["u0b"] = str(self.ui.u0Combo.currentIndex())
            cp[section]["timp"] = str(self.ui.timpBox.value())
            cp[section]["timpb"] = str(self.ui.timpCombo.currentIndex())
            with open(cpath, 'w') as cfg:
                cp.write(cfg)
        except KeyError as k:
            print("ERROR")
            print(k)
            print(k.args)
            win = QMessageBox()
            win.setText("Error with config")
            win.exec()
        pass


    def calculate_fn(self):
        """
        calculates d, in μmeters
        :return:
        """
        s_p, r_p , u_p, u0_p, t_p = self.get_powers()
        print(s_p, r_p , u_p, u0_p, t_p, self.epsilon0)
        s = self.ui.sBox.value()
        e = self.ui.epsilonBox.value()
        r = self.ui.rBox.value()
        u0 = self.ui.u0Box.value()
        u = self.ui.uBox.value()
        t = self.ui.timpBox.value()
        d = (u*u_p)/(t*t_p)*(r*r_p * e*self.epsilon0 * s * s_p)/(u0 * u0_p)
        print("D", d)
        txt = "D in μm : "+str(d)
        self.ui.answer_label.setText(txt)
        self.save_config()
        pass

    def get_powers(self):
        """

        :return: s, r, u, u0, t power factors
        """
        s_idx = self.ui.sCombo.currentIndex()
        s_pow = {
            0 : 1e-6,
            1 : 1e-4
        }
        r_idx = self.ui.rCombo.currentIndex()
        r_pow = {
            0 : 1,
            1 : 1000,
            2 : 1e6
        }
        u_idx = self.ui.uCombo.currentIndex()
        u0_idx = self.ui.u0Combo.currentIndex()
        u_pow = {
            0 : 1e-3,
            1 : 1
        }
        t_idx = self.ui.timpCombo.currentIndex()
        t_pow = {
            0 : 1e-9,
            1 : 1e-6,
            2 : 1e-3,
            3 : 1
        }
        return s_pow.get(s_idx), r_pow.get(r_idx), u_pow.get(u_idx), u_pow.get(u0_idx), t_pow.get(t_idx)


    def exit_fn(self):
        print("exiting...")
        app.exit(42)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainUi()
    window.show()
    sys.exit(app.exec_())