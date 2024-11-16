from pytubefix import YouTube
import os

def download(): 
    os.system('cls')

    link = input('Link da música: ')
    caminho = 'C:\\Users\\Walter\\Desktop\\downloader_mp3\\music' #Mude para o caminho desejado

    yt = YouTube(link)
    ys = yt.streams.get_audio_only()
    
    ys.download(output_path=caminho)


    print('\nDownload sucefull\n')

download()