

SILVER = (101, 115, 131)#Metallic Silver RGB:101,115,131
BLUE = (43, 84, 126)#Blue Jay RGB:43,84,126
BEIGE = (235, 244, 250)#Water RGB:235,244,250
PLATINUM = (229, 228, 226)#Platinum RGB:229,228,226
RED = (228, 34, 23)#Lava Red RGB:228,34,23
BATTLESHIP_GREY = (132,132,130)#Battleship Grey RGB:132,132,130
BLACK = (12, 9, 10)#Midnight RGB:12,9,10

import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill(SILVER)


pygame.draw.rect(screen, BLUE,(75, 225, 350, 75)) #main car body
pygame.draw.polygon(screen, BLUE, ((175, 175),(325, 175), (350, 225), (150, 225))) #top part of car 
pygame.draw.polygon(screen, BEIGE, ((187.5, 187.5 ),(237.5, 187.5), (237.5, 212.5 ), (175, 212.5 )))#back window
pygame.draw.polygon(screen, BEIGE, ((250, 187.5),(300, 187.5), (325, 212.5), (250, 212.5)))#front window
pygame.draw.rect(screen, PLATINUM,(400, 235, 25, 20)) #front lights 
pygame.draw.rect(screen, RED,(75, 235, 25, 20)) #rear lights 
pygame.draw.circle(screen, BLACK, (150, 300),25) #rear wheel
pygame.draw.circle(screen, BLACK, (350, 300),25) #front wheel
pygame.draw.circle(screen, BATTLESHIP_GREY, (150, 300),12) #rear rim
pygame.draw.circle(screen, BATTLESHIP_GREY, (350, 300),12) #front rim
pygame.draw.ellipse(screen, BLACK, (175, 250, 25,10))#rear door handle
pygame.draw.ellipse(screen, BLACK, (250, 250, 25,10))#rear door handle





pygame.display.update()
pygame.time.delay(6000)
pygame.image.save(screen, "car_101107249.bmp")

pygame.quit()





