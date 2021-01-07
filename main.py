#pip install pytube
import pytube



def Download(url):
    video = pytube.YouTube(url)
    print("Recherche de la video")
    for stream in video.streams:
        get_hight_video = video.streams.get_highest_resolution()
        print("Téléchargement...")
        down = get_hight_video.download()
        if down:
            print("Terminé")

if __name__ == "__main__":
    url = input("Entrer url: ")
    Download(url)