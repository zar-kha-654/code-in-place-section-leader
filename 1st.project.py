from karel.stanfordkarel import *

def main():
    #move until beepers 
    #build the hospital wherever you detect a beeper
    #don't bump into wall 
        while front_is_clear():
            if beepers_present():
                build_hospital() 
            safe_move() # move until beeper

def build_hospital():
    do_one_column()
    move()
    do_one_column()

def do_one_column():
    #pre: karel is facing right 
    #post:to be on the bottom facing right
    if beepers_present():
        pick_beeper()
    turn_left() #now he will face north
    move() #on the 2nd row
    put_beeper()
    move()
    put_beeper() 
    #on the top
    #have to move to the bottom of the row
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    put_beeper()

def safe_move():
    if front_is_clear():
        move()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()
    