import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('color changing sprite')

    # Mapping of color names to RGB values
    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'white': pygame.Color('white')
    }
    current_color = colors['white']

    x, y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 10
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0, x), 500 - sprite_width)
        y = min(max(0, y), 500 - sprite_height)

        # Change color based on boundary contact
        if x == 0: current_color = colors['blue']
        elif x == 440 :colors['yellow']
        elif y == 0: current_color = colors['red']
        elif y == 440:
            current_color = colors['green']
        else:
            current_color = colors['white']

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color,
                         (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()


main()
