import pygame

pygame.init()
WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  screen.fill("Purple")

  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
      player_pos.y -= 300 * dt
  if keys[pygame.K_s]:
      player_pos.y += 300 * dt
  if keys[pygame.K_a]:
      player_pos.x -= 300 * dt
  if keys[pygame.K_d]:
      player_pos.x += 300 * dt

  pygame.display.flip()

  clock.tick(60)

pygame.quit()
