from pytube import YouTube

# Función para descargar vídeo en la máxima calidad disponible
def descargar_video(url):
    try:
        # Crear objeto YouTube
        yt = YouTube(url)

        # Obtener el objeto de la stream con la mayor resolución disponible
        stream = yt.streams.get_highest_resolution()

        # Descargar el vídeo
        stream.download()

        print("Descarga completada.")
    except Exception as e:
        print("Error al descargar el vídeo:", str(e))

# URL del vídeo de YouTube que quieres descargar
url = "URL_DEL_VIDEO_DE_YOUTUBE_AQUI"

# Llamar a la función para descargar el vídeo
descargar_video(url)
