from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, 
        QGridLayout, QGroupBox, QHBoxLayout, QLineEdit,
        QSizePolicy, QStyleFactory, QVBoxLayout, QWidget)
import sentiment_logic

# Simple demo on how the GUI could be implemented in PyQT6

# Built on the examples of: 
# https://github.com/pyqt/examples/tree/_/src/02%20PyQt%20Widgets
# https://www.nltk.org/howto/sentiment.html

# Python version used 3.10.6 64-bit

# Requires pip install PyQT6 and the bundled file
# Bundled File: 
# Requires pip install nltk and nltk data:
# https://www.nltk.org/data.html


class MainGUI(QWidget):
    def __init__(self, parent=None):
        super(MainGUI, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        self.createTopGroupBox()
        self.createBottomGroupBox()

        topLayout = QHBoxLayout()

        topLayout.addStretch(1)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topGroupBox, 0, 0)
        mainLayout.addWidget(self.bottomGroupBox, 1, 0)
        mainLayout.setRowStretch(0, 1)
        mainLayout.setColumnStretch(0, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("SentimentAnalysisDemo built with PyQT6")
        self.changeStyle("Fusion")

        self.setMinimumSize(1200, 800)

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        QApplication.setPalette(self.originalPalette)

    def createTopGroupBox(self):
        self.topGroupBox = QGroupBox("Result")
        self.line_edit = QLineEdit()
        self.line_edit.setText("Enter a statement in the input text box, and we will analyze whether it has a positive or negative sentiment.")

        self.line_edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.line_edit.setAlignment(Qt.AlignmentFlag.AlignTop)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        self.topGroupBox.setLayout(layout)

    def createBottomGroupBox(self):
        self.bottomGroupBox = QGroupBox("Input")
        self.line_edit_input = QLineEdit('Yoda is the best character in star wars')

        self.line_edit_input.returnPressed.connect(self.on_return_pressed)

        layout = QGridLayout()
        layout.addWidget(self.line_edit_input, 0, 0, 1, 2)
        layout.setRowStretch(0, 1)
        self.bottomGroupBox.setLayout(layout)

    def on_return_pressed(self):
        text = self.line_edit_input.text()
        result = sentiment_logic.sentiment_analysis(text)
        self.line_edit.setText(result)
        self.line_edit_input.clear()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    gallery = MainGUI()
    gallery.show()
    sys.exit(app.exec())
