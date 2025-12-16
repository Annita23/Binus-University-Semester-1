import pygame
import random
from ursina import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_COLOR = (135, 206, 235)

class Bird:    
    def __init__(self, window):
        self.window = window

        self.spritesheet = pygame.image.load("asset/bird.png").convert_alpha()
        self.columns = 3
        self.rows = 3
        self.frames = []
        self.load_frames()
        self.current_frame = 0
        self.animation_speed = 0.25
        self.frame_timer = 0

        self.pos_x = SCREEN_WIDTH / 10
        self.pos_y = SCREEN_HEIGHT / 2
        self.gravity = 6
        self.jump_strength = 70
        self.width = 80
        self.height = 70

    def load_frames(self):
        sheet_width = self.spritesheet.get_width()
        sheet_height = self.spritesheet.get_height()

        frame_w = sheet_width / self.columns
        frame_h = sheet_height / self.rows

        for y in range(self.rows):
            for x in range(self.columns):
                frame = self.spritesheet.subsurface((x * frame_w, y * frame_h, frame_w, frame_h))
                self.frames.append(frame)

    def animate(self):
        self.frame_timer += self.animation_speed
        if self.frame_timer >= 1:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def draw(self):
        self.animate()

        frame = self.frames[self.current_frame]
        resized = pygame.transform.scale(frame, (self.width, self.height))

        self.window.blit(resized, (self.pos_x, self.pos_y))

    def jump(self):
        self.pos_y -= self.jump_strength

    def add_gravity(self):
        self.pos_y += self.gravity

    def get_position(self):
        return self.pos_x, self.pos_y

    def get_size(self):
        return self.width, self.height



    
class Pipe:
    def __init__(self, window):
        self.window = window

        self.pipe_image = pygame.image.load("asset/pipe.png").convert_alpha()
        self.pipe_image_flipped = pygame.transform.flip(self.pipe_image, False, True) # flip only vertically

        self.width = 120
        self.gap_height = 300
        self.pos_x = SCREEN_WIDTH
        self.top_height = random.randint(80, SCREEN_HEIGHT - self.gap_height - 80)
        self.bottom_height = SCREEN_HEIGHT - self.top_height - self.gap_height

        self.passed = False


    def draw(self):
        top_pipe_scaled = pygame.transform.scale(self.pipe_image_flipped, (self.width, self.top_height))
        self.window.blit(top_pipe_scaled, (self.pos_x, 0))

        bottom_pipe_scaled = pygame.transform.scale(self.pipe_image, (self.width, self.bottom_height))
        self.window.blit(bottom_pipe_scaled, (self.pos_x, self.top_height + self.gap_height))

    def move(self, speed):
        self.pos_x -= speed

    

class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.background = pygame.image.load("asset/background.jpg").convert()
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.bird = Bird(self.window)
        self.font = pygame.font.Font("Arial.ttf", 60)

        self.running = True
        self.score = 0
        self.pipes = []
        self.pipe_speed = 4
        self.speed_level = 0

    def handle_collision(self):
        bird_position = self.bird.get_position()
        bird_size = self.bird.get_size()

        if bird_position[0] < 0 or (bird_position[0] + bird_size[0]) > SCREEN_WIDTH or bird_position[1] < 0 or (bird_position[1] + bird_size[1]) > SCREEN_HEIGHT:
            print("Collision detected! Game Over.")
            self.running = False
        for pipe in self.pipes:
            if (bird_position[0] + bird_size[0] > pipe.pos_x and bird_position[0] < pipe.pos_x + pipe.width):
                if (bird_position[1] < pipe.top_height or bird_position[1] + bird_size[1] > pipe.top_height + pipe.gap_height):
                    print("Collision with pipe! Game Over.")
                    self.running = False

    def update_score(self):
        for pipe in self.pipes:
            if not pipe.passed and pipe.pos_x + pipe.width < self.bird.pos_x:
                pipe.passed = True
                self.score += 1

    def update(self):
        print("Current speed is:", self.pipe_speed)
        self.bird.add_gravity()
        self.generate_pipes()
        self.remove_offscreen_pipes()
        self.update_score()
        self.increase_speed()
        pygame.display.update()

    def generate_pipes(self):
        gap_pipe_distance = 500
        if len(self.pipes) == 0 or self.pipes[-1].pos_x < SCREEN_WIDTH - gap_pipe_distance:
            new_pipe = Pipe(self.window)
            self.pipes.append(new_pipe)

    def remove_offscreen_pipes(self):
        self.pipes = [pipe for pipe in self.pipes if pipe.pos_x + pipe.width > 0]


    def draw(self):
        self.window.blit(self.background, (0, 0))
        self.bird.draw()

        for pipe in self.pipes:
            pipe.move(self.pipe_speed)
            pipe.draw()

        score_text = self.font.render(f"Score : {self.score}", True, (0, 0, 0))
        self.window.blit(score_text, (20, 20))

    

    def increase_speed(self):
        new_level = self.score // 3

        if new_level > self.speed_level:
            self.speed_level = new_level
            self.pipe_speed += 1

    
    def run(self):
        while self.running:
            self.clock.tick(40)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()


            self.handle_collision()
            self.draw()
            self.update()

