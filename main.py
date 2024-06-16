import pygame

WIDTH = 1000
HEIGH = 600
SIZE  = (WIDTH, HEIGH) 
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(
                                    pygame.image.load("test_background.png"),
                                    SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        self.rect = self.image.get_rect()
        self.rect.center = coords
    
    def reset(self):
        window.blit(self.image, self.rect)


class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            
            self.rect.x += 5


test_object = Player("test_image.png", (100,100), (100,100))

test_object2 = GameSprite("test_image.png", (100,100), (300,100))

game_over = False
finish  = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    if not finish:
        window.blit(background, (0,0))
        test_object.update()
        test_object.reset()
        test_object2.update()
        test_object2.reset()

        if test_object.rect.colliderect(test_object2.rect):
            finish = True

        pygame.display.update()
        clock.tick(FPS)