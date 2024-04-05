#Faça um programa em python que abra e reproduza o audio de um arquivo mp3
import pygame
#inicializar todos os modulos do pygame
pygame.init()

#Inicializando apenar o mixer pygame
#pygame.mixer.init()

#Carregar um arquivo de musica para reprodução
pygame.mixer.music.load('Eduardo.mp3')

#Iniciar a reprodução do fluxo de musica
pygame.mixer.music.play()

#Aguardar fim da musica para finalizar, método atualizado necessita do input() antes
input() 
pygame.event.wait()

#Esse loop verifica se o canal de musica está em uso,
#quando não mais em uso, ele sai do loop
#while pygame.mixer.music.get_busy():    
#   continue #usado para voltar ao inicio do loop

#sair do programa
#pygame.quit() 
