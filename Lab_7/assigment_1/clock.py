import pygame
import datetime

COLOR_BACK = (250, 255, 255)

pygame.display.set_caption("Mickey Clock")
screen = pygame.display.set_mode((830, 900))

main_clock = pygame.image.load("/Users/damirnurmagambetov/Desktop/PP2_Labs/Lab_7/assigment_1/images/main-clock.png")
left_hand = pygame.image.load("/Users/damirnurmagambetov/Desktop/PP2_Labs/Lab_7/assigment_1/images/left-hand.png")
right_hand = pygame.image.load("/Users/damirnurmagambetov/Desktop/PP2_Labs/Lab_7/assigment_1/images/right-hand.png")

left_hand = pygame.transform.rotate(left_hand, 90)
right_hand = pygame.transform.rotate(right_hand, 90)

screen.fill(COLOR_BACK)

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

clock = pygame.time.Clock()

l_center = (343, 145)
r_center = (320, 213)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(COLOR_BACK)
    screen.blit(main_clock, (0, 0))
    time = datetime.datetime.now()
    minute = time.minute
    second = time.second

    blitRotateCenter(screen, left_hand, l_center, ((second)) * -6)
    blitRotateCenter(screen, right_hand, r_center, (minute) * -6)
    pygame.display.flip()
    clock.tick(60)