import random

def number_to_name(number):
    if number == 0:
        return "rock";
    elif number == 1:
        return "Spock";
    elif number == 2:
        return "paper";
    elif number == 3:
        return "lizard";
    elif number == 4:
        return "scissors";
    
def name_to_number(name):
    if name == "rock":
        return 0;
    elif name == "Spock":
        return 1;
    elif name == "paper":
        return 2;
    elif name == "lizard":
        return 3;
    elif name == "scissors":
        return 4;

def rpsls(name): 
    player_guess = name_to_number(name);
    comp_guess = random.randrange(0,5);
   
    result = (player_guess - comp_guess) % 5;
    
    # names of players' choices
    print "Player chooses: ",name;
    print "Computer chooses: ",number_to_name(comp_guess);
    
    if result == 1 or result == 2:
        print "Player wins!";
    elif result == 3 or result == 4:
        print "Computer wins!";
    else:
        print "Tie!";
       
    # separating different games (blank lines)
    print ""
    
# testing code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")