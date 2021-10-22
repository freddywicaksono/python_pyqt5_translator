from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
from googletrans import Translator
import sys

qtcreator_file = "translator.ui"
UI_TranslatorWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyWindow(QtWidgets.QMainWindow, UI_TranslatorWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UI_TranslatorWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.btnTerjemahkan.clicked.connect(self.terjemahkan)

    def terjemahkan(self):
        # membuat instance object
        penterjemah = Translator()

        # mengambil data dari pilihan combobox saat ini
        dest = str(self.lang_destination.currentText())

        # mengambil teks untuk diterjemahkan
        sourceText = self.txtSource.text()

        # mengambil pilihan bahasa
        lang_dest = dest[0:2]

        # proses menterjemahkan ...
        hasil = penterjemah.translate(sourceText, src='id', dest=lang_dest) 
        # Translated(src=id, dest=en, text=we have a car, pronunciation=we have a car, extra_data="{'translat...")
        # hasil.src, hasil.dest, hasil.text, hasil.pronunciation, hasil.extra_data

        # menampilkan hasil terjemahan
        self.txtHasilTerjemahan.setText(str(hasil.text))      
          

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    win = MyWindow()
    win.show() # Show in normal mode
    sys.exit(app.exec_())  