import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QTextEdit, QSpinBox, QFileDialog
import ua_generator  # Используем ua_generator

class UserAgentGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.ua = ua_generator  # Ссылка на модуль ua_generator
        self.initUI()

    def initUI(self):
        self.setWindowTitle('User-Agent Generator | tg: @w1ckedside')
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()
        # Выбор устройства
        self.deviceLabel = QLabel('Выберите тип устройства:')
        layout.addWidget(self.deviceLabel)

        self.deviceCombo = QComboBox()
        self.deviceCombo.addItems(['desktop', 'mobile', 'Any'])
        layout.addWidget(self.deviceCombo)

        # Выбор платформы
        self.platformLabel = QLabel('Выберите платформу:')
        layout.addWidget(self.platformLabel)

        self.platformCombo = QComboBox()
        self.platformCombo.addItems(['windows', 'macos', 'ios', 'linux', 'android', 'Any'])
        layout.addWidget(self.platformCombo)

        # Выбор браузера
        self.browserLabel = QLabel('Выберите браузер:')
        layout.addWidget(self.browserLabel)

        self.browserCombo = QComboBox()
        self.browserCombo.addItems(['chrome', 'edge', 'firefox', 'safari', 'Any'])
        layout.addWidget(self.browserCombo)

        # Количество юзер-агентов
        self.quantityLabel = QLabel('Количество Юзер-Агентов:')
        layout.addWidget(self.quantityLabel)

        self.quantitySpinBox = QSpinBox()
        self.quantitySpinBox.setMinimum(1)
        self.quantitySpinBox.setMaximum(1000000)
        self.quantitySpinBox.setValue(1)
        layout.addWidget(self.quantitySpinBox)

        # Кнопка генерации
        self.generateButton = QPushButton('Генерировать Юзер-Агенты')
        self.generateButton.clicked.connect(self.generateUserAgents)
        layout.addWidget(self.generateButton)

        # Текстовое поле для вывода юзер-агентов
        self.userAgentsText = QTextEdit()
        layout.addWidget(self.userAgentsText)

        # Кнопка сохранения в файл
        self.saveButton = QPushButton('Сохранить в файл')
        self.saveButton.clicked.connect(self.saveToFile)
        layout.addWidget(self.saveButton)

        self.setLayout(layout)

    def generateUserAgents(self):
        quantity = self.quantitySpinBox.value()
        device = self.deviceCombo.currentText()
        platform = self.platformCombo.currentText()
        browser = self.browserCombo.currentText()

        # Преобразование 'Any' в None для использования с ua_generator
        device = None if device == 'Any' else device
        platform = None if platform == 'Any' else (platform,)
        browser = None if browser == 'Any' else browser

        userAgents = []
        for _ in range(quantity):
            ua = self.ua.generate(device=device, platform=platform, browser=browser)
            userAgents.append(ua.text)
        self.userAgentsText.setText('\n'.join(userAgents))

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