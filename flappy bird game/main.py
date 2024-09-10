import pygame 
import sys 
import random

# creating the basic screen 
pygame.init()
pygame.mixer.init()
score = 0
wing = pygame.mixer.Sound("Assets/audio/wing.ogg")
hit = pygame.mixer.Sound("Assets/audio/hit.ogg")
die = pygame.mixer.Sound("Assets/audio/die.ogg")
point = pygame.mixer.Sound("Assets/audio/point.ogg")

SCREEN_WIDTH , SCREEN_HEIGHT = 900,500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
FPS = 60
clock = pygame.time.Clock()
Game = True

bg_img = pygame.transform.scale(pygame.image.load("Assets/images/background.jpg"),(SCREEN_WIDTH,SCREEN_HEIGHT))
t_pipe =pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Assets/images/pipe.png"),(SCREEN_WIDTH/15,SCREEN_HEIGHT)),180)
d_pipe =pygame.transform.scale(pygame.image.load("Assets/images/pipe.png"),(SCREEN_WIDTH/15,SCREEN_HEIGHT))
bird_img = pygame.transform.scale(pygame.image.load("Assets/images/bird.png"),(55,60))

xpipe = 872
ytpipe = random.randint(-200,0)
ybpipe = ytpipe+700

toppipes= []
botpipes = []

for i in range(0,2000, 200):
        ytpipe = random.randint(-200,0)
        ybpipe = ytpipe+700
        t_pipe_rect = t_pipe.get_rect(center=(xpipe + i, ytpipe))
        d_pipe_rect = d_pipe.get_rect(center=(xpipe + i, ybpipe))
        toppipes.append(t_pipe_rect)
        botpipes.append(d_pipe_rect)
  
def pipes():
 for p in toppipes:
  screen.blit(t_pipe,p)
 for p in botpipes:
  screen.blit(d_pipe,p)
birdx = 50
birdy = 200
# ceating the bird 
def bird():
   global birdy
   screen.blit(bird_img,bird_rect)
   
hit_sound_played = False
move = True

text_font = pygame.font.SysFont("Arial", 50)

# Function to display score
def display_score(score):
    score_text = text_font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (850, 0))
def main():
#  basic background 
 screen.blit(bg_img,(0,0))
cross = 0
def createpipes():
     ytpipe = random.randint(-200,0)
     ybpipe = ytpipe+700
     if toppipes[0].x <= -150:
            global score
            score+=1
            point.play()
            # Add new pipes to the end of the list
            t_pipe_rect = t_pipe.get_rect(center=(toppipes[-1].x + 200, ytpipe))
            d_pipe_rect = d_pipe.get_rect(center=(toppipes[-1].x + 200, ybpipe))
            toppipes.append(t_pipe_rect)
            botpipes.append(d_pipe_rect)
            # Remove the first pipes from the list if they go off-screen
            toppipes.pop(0)
            botpipes.pop(0)
     # Update positions of all pipes
     if move:
      for t_pipe_rect, d_pipe_rect in zip(toppipes, botpipes):
        t_pipe_rect.centerx -= 2
        d_pipe_rect.centerx -= 2

while Game:
 if move:birdy+=2
 bird_rect= bird_img.get_rect(center = (birdx,birdy))

 
 for event in pygame.event.get():
    if event.type == pygame.QUIT:
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            birdy -= 80
            wing.play()

#  colision properties 
 if bird_rect.y <= 50 :
     move = False
 if bird_rect.y >=450:
     move = False

 for i in toppipes:
   if bird_rect.colliderect(i):
     move = False
     
 for i in botpipes:
   if bird_rect.colliderect(i):
      move = False
 if move == False and not hit_sound_played:
        hit.play()
        hit_sound_played = True
 createpipes()
 main()
 bird()
 pipes()
 display_score(score)

 pygame.display.update()

 clock.tick(FPS)

