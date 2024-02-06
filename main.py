import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QFileDialog, QSpinBox
from fake_useragent import UserAgent

class UserAgentGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.ua = UserAgent()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генератор Юзер-Агентов')
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        self.osLabel = QLabel('Выберите ОС:')
        layout.addWidget(self.osLabel)

        self.osCombo = QComboBox()
        self.osCombo.addItems(['Windows', 'macOS', 'Linux', 'Any'])
        layout.addWidget(self.osCombo)

        self.browserLabel = QLabel('Выберите браузер:')
        layout.addWidget(self.browserLabel)

        self.browserCombo = QComboBox()
        self.browserCombo.addItems(['Chrome', 'Firefox', 'Opera', 'Safari', 'Internet Explorer', 'Any'])
        layout.addWidget(self.browserCombo)

        self.quantityLabel = QLabel('Количество Юзер-Агентов:')
        layout.addWidget(self.quantityLabel)

        self.quantitySpinBox = QSpinBox()
        self.quantitySpinBox.setMinimum(1)
        self.quantitySpinBox.setMaximum(100000)
        self.quantitySpinBox.setValue(1)
        layout.addWidget(self.quantitySpinBox)

        self.generateButton = QPushButton('Генерировать Юзер-Агенты')
        self.generateButton.clicked.connect(self.generateUserAgents)
        layout.addWidget(self.generateButton)

        self.userAgentsText = QTextEdit()
        layout.addWidget(self.userAgentsText)

        self.saveButton = QPushButton('Сохранить в файл')
        self.saveButton.clicked.connect(self.saveToFile)
        layout.addWidget(self.saveButton)

        self.setLayout(layout)

    def generateUserAgents(self):
        quantity = self.quantitySpinBox.value()
        userAgents = []
        for _ in range(quantity):
            if self.osCombo.currentText() == 'Any' and self.browserCombo.currentText() == 'Any':
                userAgents.append(self.ua.random)
            else:
                userAgents.append(self.generate_specific_useragent())
        self.userAgentsText.setText('\n'.join(userAgents))

    def generate_specific_useragent(self):
        browser = self.browserCombo.currentText().lower()
        if browser == 'any':
            browser_method = 'random'
        else:
            browser_method = browser
        try:
            return getattr(self.ua, browser_method)
        except:
            return self.ua.random

    def saveToFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "Сохранить как", "", "Text Files (*.txt);;All Files (*)", options=options)
        if fileName:
            with open(fileName, 'w') as file:
                file.write(self.userAgentsText.toPlainText())

def main():
    app = QApplication(sys.argv)
    ex = UserAgentGenerator()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()