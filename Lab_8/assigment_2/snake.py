import pygame, random, sys

pygame.init()

#SIZE
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
FPS = 10

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

#Image of background
background = pygame.image.load('/Users/damirnurmagambetov/Desktop/PP2_Labs/Lab_8/assigment_2/backgorund.jpeg')

#FONTS
font = pygame.font.SysFont("Verdana", 20)

#function that terminate game
def terminate():
    pygame.quit()
    sys.exit()

#Create Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (1, 0)

    def move(self):
        head = (self.body[0][0] + self.direction[0]*GRID_SIZE,
                self.body[0][1] + self.direction[1]*GRID_SIZE)
        self.body = [head] + self.body[:-1]

    def grow(self):
        self.body.append((0, 0))

    def reset(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (1, 0)

    def check_collision(self, position):
        return self.body[0] == position
    
    def check_self_collision(self):
        return self.body[0] in self.body[1:]
    
    def check_boundary_collision(self):
        head = self.body[0]
        return head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT
    
    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

#Create Food class
class Food:
    def __init__(self):
        global SCORE
        self.position = (random.randint(1, WIDTH//GRID_SIZE)*GRID_SIZE,
                         random.randint(1, HEIGHT//GRID_SIZE)*GRID_SIZE)
        
    def draw(self, surface):
        pygame.draw.rect(surface, RED, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))
    
    def randomize_position(self):
        self.position = (random.randint(1, WIDTH//GRID_SIZE)*GRID_SIZE,
                         random.randint(1, HEIGHT//GRID_SIZE)*GRID_SIZE)
        
    
#Create class Block
class Blocks:
    def __init__(self, size = 3):
        self.blocks = []
        self.size = size

        self.randomize_position()

    def draw(self, surface):
        for block in self.blocks:
            pygame.draw.rect(surface, BLUE, (block[0], block[1], GRID_SIZE, GRID_SIZE))

    def randomize_position(self):
        initial_block = (random.randint(1, WIDTH//GRID_SIZE)*GRID_SIZE,
                       random.randint(1, HEIGHT//GRID_SIZE)*GRID_SIZE)
        self.blocks = [(initial_block[0] + i*GRID_SIZE, initial_block[1]) for i in range(self.size)]
        

#Create class Poison Apple
class Poison_Food:
    def __init__(self):
        self.position = (random.randint(1, WIDTH//GRID_SIZE)*GRID_SIZE,
                         random.randint(1, HEIGHT//GRID_SIZE)*GRID_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, PURPLE, (self.position[0], self.position[1], GRID_SIZE, GRID_SIZE))

    def randomize_position(self):
        self.position = (random.randint(1, WIDTH//GRID_SIZE)*GRID_SIZE,
                         random.randint(1, HEIGHT//GRID_SIZE)*GRID_SIZE)

#Setting Up Display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

S = Snake()
F = Food()
B = Blocks()
PF = Poison_Food()
block_appeared = False #if block is appearing then we can draw it, otherwise we can not.
poison_food_appeared = False #if poison food is appearing then we can draw it, otherwise we can not.

clock = pygame.time.Clock()

#Statistics variables
LEVEL = 1
SCORE = 0

#boolean varibles
running = True
lose = False
win = False

#Function that if our game would be over then we can restart
def restart_game():
    global SCORE, LEVEL, poison_food_appeared, block_appeared, FPS
    S.reset()
    F.randomize_position()
    block_appeared = False
    poison_food_appeared = False
    FPS = 10
    LEVEL = 1
    SCORE = 0

#Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    pressed_keys = pygame.key.get_pressed()

    #Movement of snake
    if pressed_keys[pygame.K_UP] and S.direction != (0, 1):
        S.direction = (0, -1)
    if pressed_keys[pygame.K_DOWN] and S.direction != (0, -1):
        S.direction = (0, 1)
    if pressed_keys[pygame.K_LEFT] and S.direction != (1, 0):
        S.direction = (-1, 0)
    if pressed_keys[pygame.K_RIGHT] and S.direction != (-1, 0):
        S.direction = (1, 0)


    S.move()

    #If snake eat food, snake are growing
    if S.check_collision(F.position):
        F.randomize_position()
        S.grow()
        if block_appeared == True:
            B.randomize_position()
        if poison_food_appeared == True:
            PF.randomize_position()
        SCORE += 10

    #Collisions with boundary and snake
    if S.check_boundary_collision() or S.check_self_collision():
        lose = True
    
    #Appearing blocks
    if  SCORE==10 and block_appeared==False:
        block_appeared = True
        LEVEL += 1
    if block_appeared == True:
        for block in B.blocks:
            if S.check_collision(block):
                lose = True

    #Appearing poison food
    if SCORE==20 and poison_food_appeared==False:
        poison_food_appeared = True
        LEVEL+=1
        block_appeared = False
    if poison_food_appeared == True and S.check_collision(PF.position):
        if len(S.body)>1:
            S.body.pop()
        else:
            lose = True
        PF.randomize_position()
        F.randomize_position()

    #Increasing speed of snake
    if SCORE==30 and block_appeared==False and poison_food_appeared==True:
        FPS=15
        LEVEL+=1
        block_appeared = True

    #winning game
    if SCORE == 50:
        win = True

    #Losing game
    while lose:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            #Restarting game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    lose = False
                    restart_game()

        #Displaying stats
        game_over = font.render("Game Over", True, BLACK)
        restart = font.render("Enter to restart the game", True, BLACK)
        total_level = font.render(f"Your total level: {LEVEL}", True, BLACK)
        total_score = font.render(f"Your total score: {SCORE}", True, BLACK)
        pygame.draw.rect(screen, WHITE, (0, 0, 600, 400))
        screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)))
        screen.blit(restart, restart.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(total_score, total_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75)))
        screen.blit(total_level, total_level.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25)))
        pygame.display.flip()

    #Winning game
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            #Restarting game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    win = False
                    restart_game()

        #Displaying stats
        game_over = font.render("You won the game!", True, BLACK)
        restart = font.render("Enter to restart the game", True, BLACK)
        total_level = font.render(f"Your total level: {LEVEL}", True, BLACK)
        total_score = font.render(f"Your total score: {SCORE}", True, BLACK)
        pygame.draw.rect(screen, WHITE, (0, 0, 600,400))
        screen.blit(game_over, game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)))
        screen.blit(restart, restart.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        screen.blit(total_score, total_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 75)))
        screen.blit(total_level, total_level.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25)))
        pygame.display.flip()

    #Showing live stats
    screen.blit(background, (0, 0))
    score = font.render(f"{SCORE}", True, BLACK)
    screen.blit(font.render(f"SCORE", True, BLACK), (470, 10))
    screen.blit(score, score.get_rect(center=(505, 50)))
    level = font.render(f"{LEVEL}", True, BLACK)
    screen.blit(font.render(f"LEVEL", True, BLACK), (470, 60))
    screen.blit(level, level.get_rect(center=(505, 100)))
    
    #Drawing objects(snake, foods, blocks)
    S.draw(screen)
    F.draw(screen)
    if block_appeared:
        B.draw(screen)
    if poison_food_appeared:
        PF.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)