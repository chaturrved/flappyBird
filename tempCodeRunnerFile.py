

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,900))
    screen.blit(floor_surface,(floor_x_pos + 576,900))

pygame.init()
screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

#Game variables
gravity = 0.25
bird_movement = 0

bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()
bg_surface=pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load('assets/sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,512))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()