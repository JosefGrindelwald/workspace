from circleshape import *
from constants import *
class player(CircleShape):
  def __init__(self, x, y, PLAYER_RADIUS)
  rotation = 0 
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
# in the Player class
def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  pygame.draw.polygon(screen,"white" , self.triangle(), LINE_WIDTH )
