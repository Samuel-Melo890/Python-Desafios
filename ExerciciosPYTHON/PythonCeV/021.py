print('='*8,'Tocando Um MP3','='*8)

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=10)
pygame.event.wait()
print('Musica: Sell Your Soul')
