import pygame
import random

pygame.init()

player_image = pygame.image.load('dvdlogo.png')
player_scaled_image = pygame.transform.scale(player_image, (200, 120))


color_list =[
(255, 0, 0),(0, 0, 255),
(0, 255, 0), (255, 0, 255),
(0, 255, 255)
]
color = random.choice(color_list)
current_color = color
width = 200
height = 120
x = random.randint(0, 800 - 200)
y = random.randint(0, 600-120)
while True:
  x_velocity = random.randint(-10,10)
  if x_velocity != 0:
    break
while True:
  y_velocity = random.randint(-10,10)
  if y_velocity != 0:
    break

window = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

def draw_screen():
  window.fill((0, 0, 0))
  pygame.draw.rect(window, color, (x, y, width, height))
  window.blit(player_scaled_image, (x,y))
  pygame.display.update()

run = True
while run:
  clock.tick(100)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()
  draw_screen()
  if x >= 800 - width or x <= 0:
    while True:
      color = random.choice(color_list)
      if color != current_color:
        break
    current_color = color
    x_velocity *= -1
  if y >= 600 - height or y <= 0:
    while True:
      color = random.choice(color_list)
      if color != current_color:
        break
    current_color = color
    y_velocity *= -1
  x += x_velocity*0.2
  y += y_velocity*0.2

