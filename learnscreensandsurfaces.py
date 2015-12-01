import pygame
import sys

screen=pygame.display.set_mode([640,480])
pygame.init()

background=pygame.image.load("image.png")
screen.blit(background,[0,0])
pygame.display.update()
while 1:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      print("Exiting")
      pygame.quit()
    if event.type==pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        print("You pressed the space bar")
        

'''
 while 1:
        for event in pygame.event.get():
15            if event.type == pygame.QUIT: sys.exit()

17        ballrect = ballrect.move(speed)
18        if ballrect.left < 0 or ballrect.right > width:
19            speed[0] = -speed[0]
20        if ballrect.top < 0 or ballrect.bottom > height:
21            speed[1] = -speed[1]
22
23        screen.fill(black)
24        screen.blit(ball, ballrect)
25        pygame.display.flip()
'''