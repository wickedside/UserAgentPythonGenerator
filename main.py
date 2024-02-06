import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QFileDialog, QSpinBox
from fake_useragent import UserAgent, FakeUserAgentError

class UserAgentGenerator(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.ua = UserAgent()
        except FakeUserAgentError as e:
            print(f"Ошибка при инициализации fake-useragent: {e}")
            self.ua = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User-Agent generator | tg:@w1ckedside')
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
        if self.ua:
            for _ in range(quantity):
                if self.osCombo.currentText() == 'Any' and self.browserCombo.currentText() == 'Any':
                    userAgents.append(self.ua.random)
                else:
                    userAgent = self.generate_specific_useragent()
                    if userAgent:
                        userAgents.append(userAgent)
                    else:
                        userAgents.append("Не удалось сгенерировать юзер-агент.")
            self.userAgentsText.setText('\n'.join(userAgents))
        else:
            self.userAgentsText.setText("Ошибка инициализации fake-useragent, генерация невозможна.")

    def generate_specific_useragent(self):
        os_filter = self.osCombo.currentText()
        browser = self.browserCombo.currentText().lower()
        if browser == 'any':
            browser_method = 'random'
        else:
            browser_method = browser

        for _ in range(10):  # Попытки найти подходящий юзер-агент
            try:
                userAgent = getattr(self.ua, browser_method)
                if os_filter != 'Any' and self.os_in_useragent(os_filter, userAgent):
                    return userAgent
                elif os_filter == 'Any':
                    return userAgent
            except:
                continue
        return None

    def os_in_useragent(self, os_filter, useragent):
        """Проверяет соответствие ОС в строке юзер-агента."""
        os_keywords = {
            'Windows': 'Windows',
            'macOS': 'Mac',
            'Linux': 'Linux',
        }
        keyword = os_keywords.get(os_filter)
        return keyword in useragent if keyword else False

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