import sys
from PyQt5 import QtWidgets
from gui import PiCalculatorGUI

class PiCalculatorApp(QtWidgets.QApplication):
    def __init__(self, sys_argv):
        super(PiCalculatorApp, self).__init__(sys_argv)
        self.gui = PiCalculatorGUI()

    def run(self):
        self.gui.show()
        return self.exec_()

if __name__ == "__main__":
    app = PiCalculatorApp(sys.argv)
    sys.exit(app.run())