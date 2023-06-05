from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import backend

class PiCalculatorGUI(QtWidgets.QWidget):
    def __init__(self):
        super(PiCalculatorGUI, self).__init__()
        self.setWindowTitle("Calculadora de Pi")
        self.setup_ui()

    def setup_ui(self):
        self.label_result = QtWidgets.QLabel("Valor de π:")
        self.label_result.setAlignment(Qt.AlignCenter)

        self.label_time = QtWidgets.QLabel("Tempo de execução:")
        self.label_time.setAlignment(Qt.AlignCenter)

        self.button_calculate = QtWidgets.QPushButton("Calcular")
        self.button_calculate.clicked.connect(self.calculate_pi)

        self.spin_threads = QtWidgets.QSpinBox()
        self.spin_threads.setMinimum(1)
        self.spin_threads.setMaximum(1000)
        self.spin_threads.setValue(8)
        self.spin_threads.setPrefix("Número de threads: ")

        self.spin_iterations = QtWidgets.QSpinBox()
        self.spin_iterations.setMinimum(1)
        self.spin_iterations.setMaximum(1000000000)
        self.spin_iterations.setValue(100000000)
        self.spin_iterations.setPrefix("Número de iterações: ")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.spin_threads)
        layout.addWidget(self.spin_iterations)
        layout.addWidget(self.button_calculate)
        layout.addWidget(self.label_result)
        layout.addWidget(self.label_time)

        self.setLayout(layout)

    def calculate_pi(self):
        num_threads = self.spin_threads.value()
        num_iterations = self.spin_iterations.value()

        valor_pi, tempo_execucao = testepireal.calcular_pi(num_iterations, num_threads)

        self.label_result.setText(f"Valor de π: {valor_pi}")
        self.label_time.setText(f"Tempo de execução: {tempo_execucao:.7f} segundos")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PiCalculatorGUI()
    window.show()
    sys.exit(app.exec_())