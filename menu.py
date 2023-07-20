import random
import praw #reddit api
import os
from pytube import YouTube
import pyautogui
import time
from gtts import gTTS
from moviepy.editor import *


#Videos de Youtube para background
#Videos de background minecraft
minecraftParkour1="https://youtu.be/O4-83D-VN1U"
minecraftParkour2="https://youtu.be/Pt5_GSKIWQM"
minecraftParkour3="https://youtu.be/YuS7fY2xPSg"
minecraftParkour4="https://youtu.be/Bxqeq8Bdr5A"

#Videos de background asmrSlime
asmrSlime1 = "https://www.youtube.com/watch?v=UjL6x-umRMY"
asmrSlime2 = "https://www.youtube.com/watch?v=s-XRQFXhz24"
asmrSlime3 = "https://www.youtube.com/watch?v=-s0p3jBXg58"
asmrSlime4 = "https://www.youtube.com/watch?v=16MJeAC8kbQ"

#Videos de background Subway Surfers
subwaySurfers1 = "https://youtu.be/h8mzKm6iNt4"
subwaySurfers2 = "https://youtu.be/VwJaIa_Eyds"
subwaySurfers3 = "https://www.youtube.com/watch?v=YmOzMks3UaE"
subwaySurfers4 = "https://youtu.be/AYqHUiYFke4"

#Videos de background Animaciones
animaciones1 = "https://youtu.be/2avT63Pjljg"#ocean
animaciones2 = "https://youtu.be/pi_Ci18ZwqA"#nyancat
animaciones3 = "https://youtu.be/PB4gId2mPNc"#space
animaciones4 = "https://www.youtube.com/watch?v=nGnX6GkrOgk"#space 2



#subreddits de terror Categoria 1

#subredditTerror1 = "Terror1.txt"
#subredditTerror2 = "Terror2.txt"
#subredditTerror3 = "Terror3.txt"
#subredditTerror4 = "Terror4.txt"

#subreddits de Categoria 2

#subreddits de Categoria 3

#subreddits de Categoria 4

def CargarDeRedit():
        # Set up Reddit API credentials and create a PRAW instance
        # Llenar los campos para poder utilizar esta app
    reddit = praw.Reddit(client_id='client id', 
                        client_secret='client-secret',
                        username='example-username',
                        password='Secret_Password',
                        user_agent='automatizacion')

    # Elegir el subreddit y el tipo de post

    
    post_type = 'top' # También puede ser 'top', 'new', o 'rising'

    # Obtener el subreddit y los posts
    subreddit = reddit.subreddit(subreddit_name)
    if post_type == 'hot':
        posts = subreddit.hot(limit=1)##se modifca el numero de comentarios q se quiere de primer nivel
    elif post_type == 'top':
        posts = subreddit.top(limit=1)
    elif post_type == 'new':
        posts = subreddit.new(limit=1)
    elif post_type == 'rising':
        posts = subreddit.rising(limit=1)

    # Abrir el archivo de texto en modo escritura
    with open('storagetxt/postreddit.txt', 'w') as f:
        # Escribir el título y los 5 primeros comentarios de respuesta en primer nivel en el archivo de texto
        for post in posts:
            #f.write('-----------------------------------------------------------------\n')
            f.write(f'Post title: {post.title}\n\n')
            #f.write('-----------------------------------------------------------------\n')
            f.write(f'Post content: {post.selftext}\n\n')
            print("-------------------------------")
            print("Reddit almacenado correctamente")
            print("-------------------------------")
    ConvertirTextoAudio()


def descargarvideo():
    # URL del video a descargar
    
    # Creamos un objeto YouTube y obtenemos la mejor resolución disponible
    youtube = YouTube(url)
    stream = youtube.streams.get_highest_resolution()
        # Descargamos el video y lo renombramos con el nombre que deseamos
    print("Descargando video...")
    filename = "mi_video_descargado.mp4" # Reemplazar "mi_video" con el nombre que desee
    stream.download(output_path='download', filename=filename)
    print("Descarga completada satisfactoriamente")
    subreddit()
        
    
if not os.path.exists('download'):
    os.makedirs('download')




#subir video a facebook
def subirVideoTikTok():
    print("-----------")
    print("Subiendo...")
    print("-----------")
    #tiktok
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.write('chrome.exe "tiktok.com/upload/?lang=es"', interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")
    #bucle para volver a buscar la imagen si no la encuentra
    while True:
        try:
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/button.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
        except:
            print("no se encontro la imagen")
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/button.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break

    #time.sleep(15)
    #btupload= pyautogui.locateOnScreen('button.png')
    #print(pyautogui.click(*pyautogui.center(btupload)))
    time.sleep(2)
    pyautogui.hotkey('alt', 'd')
    time.sleep(2)
    pyautogui.write('C:/Users/josel/Documents/pythonaut/processeditfinal/', interval=0.1)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)   

    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    ##en el archivo original renombrar como queramos que se agregue en la publicacion 
    pyautogui.write('finalsubir', interval=0.1)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(150)
    #8 flechas abajo
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    #bucle para volver a buscar la imagen si no la encuentra
    while True:
        try:
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/publicar.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
        except:
            print("no se encontro la imagen")
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/publicar.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
    time.sleep(2)
    #bucle para volver a buscar la imagen si no la encuentra
    while True:
        try:
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/perfil.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
        except:
            print("no se encontro la imagen")
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/perfil.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
    print("----------------------------")
    print("Video Subido con Exito :D :D")
    print("----------------------------")
    time.sleep(5)
    main()

#subir video a facebook
def subirVideoTikTokAll():
    print("-----------")
    print("Subiendo...")
    print("-----------")
    #tiktok
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.write('chrome.exe "tiktok.com/upload/?lang=es"', interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")
    #bucle para volver a buscar la imagen si no la 2encuentra
    while True:
        try:
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/button.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
        except:
            print("no se encontro la imagen")
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/button.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break

    #time.sleep(15)
    #btupload= pyautogui.locateOnScreen('button.png')
    #print(pyautogui.click(*pyautogui.center(btupload)))
    time.sleep(2)
    pyautogui.hotkey('alt', 'd')
    time.sleep(2)
    pyautogui.write('C:/Users/josel/Documents/pythonaut/processeditfinal/', interval=0.1)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)   

    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    ##en el archivo original renombrar como queramos que se agregue en la publicacion 
    pyautogui.write('finalsubir', interval=0.1)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(200)
    #8 flechas abajo
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    time.sleep(1)
    pyautogui.press("down")
    #bucle para volver a buscar la imagen si no la encuentra
    while True:
        try:
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/publicar.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
        except:
            print("no se encontro la imagen")
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/publicar.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
    time.sleep(2)
    #bucle para volver a buscar la imagen si no la encuentra
    while True:
        try:
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/perfil.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
        except:
            print("no se encontro la imagen")
            time.sleep(5)
            btupload= pyautogui.locateOnScreen('imgrecogtiktok/perfil.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
    print("----------------------------")
    print("Video Subido con Exito :D :D")
    print("----------------------------")
    time.sleep(5)
    subirVideoInstagram()



#subir video a youtube
def subirVideoInstagram():
    print("Subiendo...")
    time.sleep(5)
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.write('chrome.exe "instagram.com"', interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")
    #bucle para volver a buscar la imagen si no la encuentra
    while True:
        try:
            time.sleep(1)
            btupload= pyautogui.locateOnScreen('imgrecoginstagram/crear.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
        except:
            print("no se encontro la imagen")
            time.sleep(1)
            btupload= pyautogui.locateOnScreen('imgrecoginstagram/crear.png')
            print(pyautogui.click(*pyautogui.center(btupload)))
            break
    time.sleep(2)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('alt', 'd')
    time.sleep(2)
    pyautogui.write('C:/Users/josel/Documents/pythonaut/processeditfinal/', interval=0.1)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    ##en el archivo original renombrar como queramos que se agregue en la publicacion 
    pyautogui.write('finalsubir', interval=0.1)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(2)
    pyautogui.hotkey('enter')
    #time.sleep(400)
    #pyautogui.hotkey('tab')
    time.sleep(2)
    #pyautogui.hotkey('enter')
    time.sleep(1)
    print("----------------------------")
    print("Video subido con exito :D :D")
    print("----------------------------")
    main()

#subir video a instagram   
def subirVideoYoutube():
    print("Subir video a instagram")
    main()

#subir video a twitter
def subirVideoTwitter():
    print("Subir video a twitter")
    main()

def SubirTodasLasRedes():
    print("Subir video a todas las redes")
    subirVideoTikTokAll()
    main()


#esta funcion es la que posee todo el codigo a ejecutar
def Comencemos():
    print("Comencemos")
    


#funcion para subir video con opciones de seguridad para evitar errores
def subirVideo():
    print("¿Seguro quieres subir el video?, si decides que SI, no hay vuelta atras")
    print("1. Si")
    print("2. No")
    opcion = input("\nElija una opción (1-2): ")
    if opcion in ['1', '2']:
        opcion = int(opcion)
        if opcion == 1:
            Comencemos()
        elif opcion == 2:
            print("No se subira el video")
            main()
    else:
        print("Opcion no valida")
        subirVideo()
    
#listas de subreddits
subreddits = ["talesfromtechsupport", "findareddit", "learnpython", "LifeProTips"]

#lista de videos
videos = [["Minecraft", minecraftParkour1, minecraftParkour2, minecraftParkour3, minecraftParkour4],
          ["Slime", asmrSlime1, asmrSlime2, asmrSlime3, asmrSlime4],
          ["SubwaySurfers", subwaySurfers1, subwaySurfers2, subwaySurfers3, subwaySurfers4],
          ["animaciones", animaciones1, animaciones2, animaciones3, animaciones4]]

def ConvertirTextoAudio():
            # Leer el archivo de texto
    with open("storagetxt/postreddit.txt", "r") as archivo:
        texto = archivo.read().replace("\n", " ")
    # Crear objeto gTTS y generar archivo de audio
    tts = gTTS(text=texto, lang="en")
    tts.save("audio/audio.mp3")
    print("--------------------------------------")
    print("Texto a audio convertido correctamente")
    print("--------------------------------------")
    EditarVideo()

def EditarVideo():
    print("------------Editando Video------------")
    print()
    print("//////////////////////////////////////")
    print()
    #cortar video
    print()
    print("------------Cortando Video------------")
    video = VideoFileClip("download/mi_video_descargado.mp4")
    cortado = video.subclip(1, 270)#el segundo 1 al 2 en este caso como prueba
    cortado.write_videofile("processedit/vidcut.mp4")
    print()
    print("//////////////////////////////////////")
    print("------Adjuntando Audio con Video------")
    video = VideoFileClip("processedit/vidcut.mp4")
    audio = AudioFileClip("audio/audio.mp3")
    video = video.set_audio(audio)
    video.write_videofile("processedit/vidconaudio.mp4")
    print()
    print("//////////////////////////////////////")
    print()
    print("--Modificando la velocidad del video--")
    # modificar la velocidad del video
    video = VideoFileClip("processedit/vidconaudio.mp4").fx(vfx.speedx, 0.90)
    video.write_videofile("processeditfinal/finalsubir.mp4")
    print()
    print("//////////////////////////////////////")
    print()
    print("-------Video Listo para subir---------")
    Plataforma()
    main()



#funcion para elegir un subreddit
def subreddit():
    global subreddit_name 
    print("----------------------------------------------------")
    print("Seleccione un subreddit para acceder a su contenido:")
    print("----------------------------------------------------")
    for i, subreddit in enumerate(subreddits):
        print(f"{i+1}. {subreddit}")

    opcion = input("\nElija una opción (1-4): ")

    if opcion in ['1', '2', '3', '4']:
        
        opcion = int(opcion)
        print(f"Ha elegido el subreddit {subreddits[opcion-1]}")
        subreddit_name = subreddits[opcion-1]
        CargarDeRedit()
        main()
    else:
        
        opcion = random.randint(1, 4)
        print(f"Opción no válida. Se ha elegido aleatoriamente el subreddit {subreddits[opcion-1]}")
        subreddit_name = subreddits[opcion-1]
        CargarDeRedit()
        main()
    


#funcion para elegir un video de background
def video_background():
    global url
    print("------------------------------------------")
    print("Seleccione un tipo de video de background:")
    print("------------------------------------------")
    for i, video in enumerate(videos):
        print(f"{i+1}. {video[0]}")
    print("------------------------------------")
    opcion = input("\nElija una opción (1-4): ")
    print("------------------------------------")
    if opcion in ['1', '2', '3', '4']:
        opcion = int(opcion)
        print("------------------------------------")
        print(f"Ha elegido el tipo de video {videos[opcion-1][0]}")
        print("Videos disponibles:")
        print("------------------------------------")
        for i, video in enumerate(videos[opcion-1][1:]):
            print(f"{i+1}. {video}")
        video_opcion = input("\nElija un video (1-4): ")
        print("------------------------------------")
        if video_opcion in ['1', '2', '3', '4']:
            video_opcion = int(video_opcion)
            print(f"Ha elegido el video {videos[opcion-1][video_opcion]}")
            url= videos[opcion-1][video_opcion]
            descargarvideo()
            main()
          
        else:
            video_opcion = random.randint(1, 4)
            print(f"Opción no válida. Se ha elegido aleatoriamente el video {videos[opcion-1][video_opcion]}")
            url= videos[opcion-1][video_opcion]
            descargarvideo()
            main()
    else:
        opcion = random.randint(1, 4)
        print(f"Opción no válida. Se ha elegido aleatoriamente el tipo de video {videos[opcion-1][0]}")
        print("Videos disponibles:")
        for i, video in enumerate(videos[opcion-1][1:]):
            print(f"{i+1}. {video}")
        video_opcion = random.randint(1, 4)
        print(f"Se ha elegido aleatoriamente el video {videos[opcion-1][video_opcion]}")
        url= videos[opcion-1][video_opcion]
    descargarvideo()
    main()
        




#menu de subida
def Plataforma():
    print()
    print()
    print("----------------------")
    print("Seleccione una opción:")
    print("----------------------")
    print("1. TikTok")
    print("2. Instagram")
    print("3. Subir a todas las plataformas")
    print("4. Volver al menú principal")
    print("------------------------------------")
    opcion = input("\nElija una opción (1-4): ")
    print("------------------------------------")

    if opcion == '1':
        subirVideoTikTok()
    elif opcion == '2':
        subirVideoInstagram()
    elif opcion == '3':
        SubirTodasLasRedes()
    elif opcion == '4':
        main()
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        Plataforma()



#menu principal
#funcion main
def ConfiguracionVideo():
    video_background()
    


#menu principal
def main():
    print()
    print()
    print("------------------------------------------------------------------------")
    print('\033[33m' + 'Bienvenido a la aplicación de creación de videos para TikTok e Instagram' + '\033[0m')
    print("------------------------------------------------------------------------")
    print('\033[32m' + 'Seleccione una opción:' + '\033[0m')
    print("----------------------")
    print('\033[32m' + '1. Configuración de video' + '\033[0m')
    print('\033[32m' + '2. Salir' + '\033[0m')
 

    opcion = input("\nElija una opción (1-2): ")

    if opcion == '1':
        ConfiguracionVideo()
    elif opcion == '2':
        print("Saliendo...")
        exit()  
    else:
        print("Opción no válida. Inténtelo de nuevo.")
        main()
    


main()