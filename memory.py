# implementation of card game - Memory

import simplegui
import random

sound = simplegui.load_sound("http://hangtar.fikszradio.hu/Otorai_tea/2008/Otorai_tea_20080619/07%20-%20Rick%20Astley%20-%20Never%20Gonna%20Give%20You%20Up.mp3")
image = simplegui.load_image("http://myhometruths.com/wp-content/uploads/2013/02/rick-astley.jpg")
moves = 0
i = 0
index = [0,0]
state = 0
card_list1 = range(0,8)
card_list2 = range(0,8)
main_list = card_list1 + card_list2
exposed_list = []
rick = 0

while i < 16:
     exposed_list.append(False)
     i += 1

# helper function to initialize globals
def init():
    global state, exposed_list
    i = 0
    state = 0
    random.shuffle(main_list)
    for i in range(0,16):
        exposed_list[i] = False
     
# define event handlers
def mouseclick(pos):
    global state, exposed_list, main_list, index, moves
    
    if exposed_list[int(pos[0] / 50)] == False:
        
        if state == 1:
            state = 2
            index[1] = int(pos[0] / 50)
            exposed_list[index[1]] = True
        else:
            state = 1
            if index[1] != index[0] and main_list[index[1]] == main_list[index[0]]:
                pass
            else:
                exposed_list[index[1]] = False
                exposed_list[index[0]] = False
            index[0] = int(pos[0] / 50)
            exposed_list[index[0]] = True
        
        moves += 1
    
    
def stop():
    global sound, rick
    rick = 0
    sound.pause()

def start():
    global sound, rick
    sound.play()
    rick = 1
    
    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed_list, main_list, image
    i = 0
    for i in range(0,16): 
        if exposed_list[i] == False:
            canvas.draw_line([50*i,0],[50*i,150],1, "Green")
        else:
            canvas.draw_line([25+50*i,0],[25+50*i,150],50, "Grey")
            canvas.draw_line([50*i,0],[50*i,150],1, "Black")
            canvas.draw_text(str(main_list[i]), (25+50*i, 75), 32, "White")
    
    if rick == 1:
        canvas.draw_image(image, (image.get_width()/2,image.get_height()/2),(image.get_width(),image.get_height()),(200,75),(400,150))
        canvas.draw_image(image, (image.get_width()/2,image.get_height()/2),(image.get_width(),image.get_height()),(700,75),(200,150))
        canvas.draw_image(image, (image.get_width()/2,image.get_height()/2),(image.get_width(),image.get_height()),(500,75),(300,150))
        canvas.draw_text("You got RICK ROLLED!", (150,75), 45, "Red")
    label.set_text("Moves = " + str(moves))
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory by Piw.Corp.", 800, 150)
frame.add_button("Restart", init)
frame.add_button("Sound: OFF", stop, 200)
frame.add_button("Sound: ON", start, 200)
label = frame.add_label("Moves = " + str(moves))

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()

# Always remember to review the grading rubric