import os
from pytube import YouTube

def descargar_video(url, ruta_descarga):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=ruta_descarga)
        print(f"Vídeo descargado en {ruta_descarga}")
    except Exception as e:
        print(f"Error al descargar el vídeo: {e}")

if __name__ == "__main__":
    url_video = input("Ingresa la URL del vídeo de YouTube: ")
    ruta_descarga = input("Ingresa la ruta donde deseas guardar el vídeo: ")

    if not os.path.exists(ruta_descarga):
        os.makedirs(ruta_descarga)

    descargar_video(url_video, ruta_descarga)
