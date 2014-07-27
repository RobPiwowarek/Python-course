# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [0, 0]
paddle1_pos = [HEIGHT/2 + HALF_PAD_HEIGHT, HEIGHT/2 - HALF_PAD_HEIGHT]
paddle2_pos = [HEIGHT/2 + HALF_PAD_HEIGHT, HEIGHT/2 - HALF_PAD_HEIGHT]
paddle1_vel = 0
paddle2_vel = 0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    
    if right == True:
        vel = [random.randrange(2,4),-random.randrange(1, 3)]
    elif right == False:
        vel = [-random.randrange(2,4),-random.randrange(1, 3)]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    
    score1 = 0
    score2 = 0
    
    rand = random.randrange(1,3)
    if rand == 1:
        ball_init(True)
    elif rand == 2:
        ball_init(False)

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, vel
    global paddle1_vel, paddle2_vel
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0] + paddle1_vel < HEIGHT and paddle1_pos[0] + paddle1_vel >= PAD_HEIGHT:
        paddle1_pos[0] += paddle1_vel
        paddle1_pos[1] += paddle1_vel
    
    if paddle1_pos[0] >= HEIGHT and paddle1_vel != 0:
        paddle1_vel = 0
      
    elif paddle1_pos[0] <= PAD_HEIGHT and paddle1_vel != 0:
        paddle1_vel = 0
        
    if paddle2_pos[0] + paddle2_vel < HEIGHT and paddle2_pos[0] + paddle2_vel >= PAD_HEIGHT:
        paddle2_pos[0] += paddle2_vel
        paddle2_pos[1] += paddle2_vel
        
    if paddle2_pos[0] >= HEIGHT:
        paddle2_vel = 0
    elif paddle2_pos[0] <= PAD_HEIGHT:
        paddle2_vel = 0
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    #collisions
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos[1] and ball_pos[1] <= paddle1_pos[0]:
            vel[0] = -vel[0]
            vel[0] = 1.1 * vel[0]
        else:
            score2 += 1
            ball_init(True)
    elif ball_pos[0] >= (WIDTH-1)-BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos[1] and ball_pos[1] <= paddle2_pos[0]:
            vel[0] = -vel[0]
            vel[0] = 1.1 * vel[0]
        else:
            score1 += 1
            ball_init(False)
    elif ball_pos[1] == HEIGHT-BALL_RADIUS:
        vel[1] = -vel[1]
    elif ball_pos[1] == BALL_RADIUS:
        vel[1] = -vel[1]

    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_line((HALF_PAD_WIDTH, paddle1_pos[0]), (HALF_PAD_WIDTH, paddle1_pos[1]), PAD_WIDTH, "White")
    c.draw_line((WIDTH-HALF_PAD_WIDTH, paddle2_pos[0]), (WIDTH-HALF_PAD_WIDTH, paddle2_pos[1]), PAD_WIDTH, "White")
    c.draw_text(str(score1), (200, 100), 60, "Red")
    c.draw_text(str(score2), (365, 100), 60, "Red")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 3
    
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 3
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button("RESTART", new_game)


# start frame
frame.start()
new_game()

