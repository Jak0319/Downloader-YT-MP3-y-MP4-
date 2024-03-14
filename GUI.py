import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from pytube import YouTube

class DownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Video Downloader")
        self.setGeometry(200, 200, 400, 200)

        self.url_label = QLabel("Ingrese la URL del vídeo de YouTube:")
        self.url_input = QLineEdit()
        self.download_button = QPushButton("Descargar")
        self.download_button.clicked.connect(self.descargar_video)

        layout = QVBoxLayout()
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)
        self.setLayout(layout)

    def descargar_video(self):
        url = self.url_input.text()
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            print("Descarga completada.")
            self.url_input.setText("")  # Limpiar el campo de entrada después de la descarga
        except Exception as e:
            print("Error al descargar el vídeo:", str(e))

def main():
    app = QApplication(sys.argv)
    window = DownloaderApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
