def python():
    """
    Função para executar o código Python.
    """
import time
import pygame
import os

# Inicializa o pygame
pygame.init()
pygame.mixer.init()

# Caminho para a música
caminho_musica = os.path.join("Downloads", "The Final Countdown.mp3")

# Carrega a música
pygame.mixer.music.load(caminho_musica)

# Toca a música
pygame.mixer.music.play()

print("Carregando todos os addons do mundo para o python...")
time.sleep(68)
print('Sucesso!')
time.sleep(3)
print("! ATENÇÃO,O SEU COMPUTADOR ESTÁ SUPERAQUECENDO,DESLIGANDO O HIWO !")
time.sleep(2)
pygame.quit()   
# Comando para fechar o Visual Studio Code no Windows
os.system("taskkill /f /im Code.exe")