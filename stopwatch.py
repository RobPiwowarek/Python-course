# template for "Stopwatch: The Game"
import simplegui

# define global variables
tenths_of_seconds = 0
stops = 0
count = 0
is_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = 0
    sec_b = 0
    sec_c = 0
    min = 0
    
    tenths = t % 10
    sec_b = int(t/10) % 10
    sec_c = int(t/100) % 6
    min = int(int(t/100) / 6)
    
    formatted = str(min) + ":" + str(sec_c) + str(sec_b) + "." + str(tenths)
    
    return formatted
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global time, is_running
    time.start()
    is_running = True
    
    
def stop():
    global time, is_running, count, stops, tenths_of_seconds
    time.stop()
        
    if is_running == True:
        stops += 1
        if tenths_of_seconds % 10 == 0:
            count += 1
        is_running = False
    
def reset():
    global stops, count, tenths_of_seconds, is_running
    stops = 0
    count = 0
    tenths_of_seconds = 0
    is_running = False
    
# define event handler for timer with 0.1 sec interval
def timer():
    global tenths_of_seconds, is_running
    if is_running == True:
        tenths_of_seconds += 1
    
# define draw handler
def draw(canvas):
    global tenths_of_seconds, count, stops, is_running
    canvas.draw_text(format(tenths_of_seconds), (150,150), 32, "White")
    canvas.draw_text(str(count), (250,50), 12, "White")
    canvas.draw_text("/", (260,50), 12, "White")
    canvas.draw_text(str(stops), (265,50), 12, "White")
                     
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)

start_button = frame.add_button("Start", start)
stop_button = frame.add_button("Stop", stop)
reset_button = frame.add_button("Reset", reset)

frame.set_draw_handler(draw)

time = simplegui.create_timer(100, timer)

# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric
