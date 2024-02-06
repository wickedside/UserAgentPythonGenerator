import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QFileDialog

class UserAgentGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User-Agents generator | tg:@w1ckedside')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.osLabel = QLabel('Выберите ОС:')
        layout.addWidget(self.osLabel)

        self.osCombo = QComboBox()
        self.osCombo.addItems(['Windows', 'macOS', 'Linux'])
        layout.addWidget(self.osCombo)

        self.browserLabel = QLabel('Выберите браузер:')
        layout.addWidget(self.browserLabel)

        self.browserCombo = QComboBox()
        self.browserCombo.addItems(['Chrome', 'Firefox', 'Opera'])
        layout.addWidget(self.browserCombo)

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
        os = self.osCombo.currentText()
        browser = self.browserCombo.currentText()
        # Простой пример генерации юзер-агента, можно расширить для большей уникальности
        userAgent = f"Mozilla/5.0 ({os}; AppleWebKit/537.36 (KHTML, like Gecko) {browser}/90.0 Safari/537.36"
        self.userAgentsText.setText(userAgent)

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