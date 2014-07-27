# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import math
import simplegui
import random

# initialize global variables used in your code
num_of_guesses = 0;
user_guess = 0;
secret_num = 0;
border = 100;

def new():
    if border == 1000:
        range1000();
    else:
        range100();

# define event handlers for control panel
    
def range100():
    global num_of_guesses, secret_num, border;
    num_of_guesses = 7;
    border = 100;
    secret_num = random.randrange(0, 100);
    print "New Game."
    print "Number of guesses: ", num_of_guesses;
    print "Range is: ", "[0,", border, ")";   
    print ""
    
def range1000():
    global num_of_guesses, secret_num, border;
    border = 1000;
    num_of_guesses = 10;
    secret_num = random.randrange(0, 1000);
    print "New Game."
    print "Number of guesses: ", num_of_guesses;
    print "Range is: ", "[0,", border, ")";   
    print ""
    
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
    global user_guess, num_of_guesses;
    user_guess = int(guess);
    print "Your guess: ", user_guess;
    
    
    if user_guess < secret_num:
        print "Hint: Higher";
        num_of_guesses = num_of_guesses - 1;
        print "Guesses Left: ", num_of_guesses;
        print "";
    elif user_guess > secret_num:
        print "Hint: Lower"
        num_of_guesses = num_of_guesses - 1;
        print "Guesses Left: ", num_of_guesses;
        print "";
    elif user_guess == secret_num:
        print "Correct!"
        print ""
        new();
        
    if num_of_guesses == 0:
        print "You lost!";
        print ""
        new();
     
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200);

# register event handlers for control elements
f.add_button("Range [0;100)", range100, 200);
f.add_button("Range [0;1000)", range1000, 200);
f.add_input("Enter a guess", get_input, 200);

f.start();
new();


    