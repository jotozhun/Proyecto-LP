from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from main import *
from Yacc import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.resize(700, 600)
        self.setWindowTitle("Lexic&Syntax")
        self.textbox = QTextEdit(self)
        self.resultText = QTextEdit(self)
        self.init_UI()

    def init_UI(self):
        # La barra de herramientas
        toolbar = QToolBar("My toolBar")
        toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(toolbar)
        self.setToolButtonStyle(Qt.ToolButtonIconOnly)

        # Crear Iconos y botones

        newButton = QAction(QIcon("Assets/new.png"), "Nuevo Archivo", self)
        newButton.setStatusTip("Nuevo Archivo")
        newButton.triggered.connect(lambda x: self.onNewFileButton())
        toolbar.addAction(newButton)

        saveButton = QAction(QIcon("Assets/save.png"), "Guardar Archivo", self)
        saveButton.setStatusTip("Guardar Archivo")
        saveButton.triggered.connect(lambda x: self.onSaveButton())
        toolbar.addAction(saveButton)

        lexicoButton = QAction(QIcon("Assets/lex.png"), "Analizar léxico", self)
        lexicoButton.setStatusTip("Ejecutar analizador léxico")
        lexicoButton.triggered.connect(lambda x: self.onLexButton())
        toolbar.addAction(lexicoButton)

        syntaxButton = QAction(QIcon("Assets/synt.png"), "Analizar sintáctica", self)
        syntaxButton.setStatusTip("Ejecutar analizador sintáctico")
        syntaxButton.triggered.connect(lambda x: self.onSyntButton())
        toolbar.addAction(syntaxButton)

        # Cuadro de texto

        self.textbox.move(5, 45)
        self.textbox.resize(395, 550)
        #self.textbox.setCurrentFont(QFont("Times", 18))
        self.textbox.setFontPointSize(int(18))

        self.resultText.move(405, 45)
        self.resultText.resize(290, 550)
        #self.resultText.setReadOnly(True)
        # Cuadro de resultados

    def isTextboxEmpty(self):
        return self.textbox.toPlainText() == ""

    def onNewFileButton(self):
        self.textbox.clear()
        self.resultText.clear()
        self.textbox.setFontPointSize(int(18))

    def onLexButton(self):
        if(not self.isTextboxEmpty()):
            self.resultText.clear()
            textToProcess = self.textbox.toPlainText()
            resultText = lexAnalizer(textToProcess)
            lexFile = open("lexErrors.txt", "r")
            resultText += "\n\n\nErrores de sintaxis: \n\n%s" % lexFile.read()
            lexFile.close()
            #Just for overwriting
            raw = open("lexErrors.txt", "w")
            raw.close()
            self.resultText.setText(resultText)

    def onSyntButton(self):
        if not self.isTextboxEmpty():
            self.resultText.clear()
            textToProcess = self.textbox.toPlainText()
            resultText = analizadorSintactico(textToProcess)
            syntFile = open("yaccErrors.txt", "r")
            resultText += "\n\n\nErrores de sintaxis: \n\n%s" %syntFile.read()
            syntFile.close()
            # Just for overwriting
            raw = open("lexErrors.txt", "w")
            raw.close()
            self.resultText.setText(resultText)

    def onSaveButton(self):
        saveFile = QFileDialog.getSaveFileName(None, "SaveTextFile", "/", "Text Files (*.txt)")

        headText = self.textbox.toPlainText()
        footText = self.resultText.toPlainText()

        if saveFile[0]:
            with open(saveFile[0], 'w') as file:
                file.write("Texto a procesar:\n\n" + headText + "\n\n\n" + "Texto analizado: \n\n" + footText)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()

print("Termina el event loop")