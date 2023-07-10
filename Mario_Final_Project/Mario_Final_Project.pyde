# Avi Shah
# Final: Moving Mario

# creating all the variables
# variables that reset when game is over
def reset_variables():
    global x
    global y
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    global speed1
    global speed2
    global random_num
    global random_num2
    global jump
    global jumpcount
    global boundary
    global key_left
    global key_right
    global key_up
    global menu
    global level_one
    global level_two
    global end_game_1
    global end_game_2
    global time_num
    global frames
    global frame_jump
    global frames_when_dead
    
    # starting position of mario
    x = 100
    y = 425
    
    # rock 1 starting position
    x1 = 50
    y1 = -100
    
    # rock 2 starting position
    x2 = 600
    y2 = -300
    
    # rock 3 starting position
    x3 = 200
    y3 = -100
    
    # rock 4 starting position (only moves horizontally)
    x4 = 1000 
    
    # rocks starting speed for each level
    speed1 = 6
    speed2 = 10
    
    random_num = 0
    random_num2 = 0
    
    # variables for jumping
    jump = False
    jumpcount = 13
    boundary = False
    
    # pressing keys
    key_left = False
    key_right = False
    key_up = False
    menu = False
    
    # levels and when levels end
    level_one = False
    level_two = False
    end_game_1 = False
    end_game_2 = False
    
    # time variables
    time_num = 0
    frames = 0
    frame_jump = 0
    frames_when_dead = 0

reset_variables()

# variables that do not reset
# stars in the menu for level 1
star_1_lvl_1 = False
star_2_lvl_1 = False
star_3_lvl_1 = False

# stars in the menu for level 2
star_1_lvl_2 = False
star_2_lvl_2 = False
star_3_lvl_2 = False

# image variable:
mario_right_img = None
mario_left_img = None
mario_current_img = None
rock_1_img = None
rock_2_img = None
star = None
empty_star = None

# When the rocks collide with mario, the game will end
def collision():
    global end_game_1
    global end_game_2
    
    # level 1
    # hitting rock 1
    if x1-55 < x and x1+65 > x and y1-60 < y and y1+60 > y and level_two == False:
        end_game_1 = True
    # hitting rock 2
    if x2-55 < x and x2+70 > x and y2-60 < y and y2+60 > y and level_two == False:
        end_game_1 = True
        
    # level 2
    # if mario is over horizontal rock, game will not end
    if y + 75 < 425:
        end_game_2 = False
    # hitting rock 4 horizontal
    elif x4 + 40 > x and x4 - 40 < x:
        end_game_2 = True 
    # hitting rock 2 vertical
    if x2-55 < x and x2+70 > x and y2-60 < y and y2+60 > y and level_one == False:
        end_game_2 = True
    # hitting rock 3 vertical
    if x3-55 < x and x3+70 > x and y3-60 < y and y3+60 > y and level_one == False:
        end_game_2 = True

# mario jumping function, I used this video for help: https://www.youtube.com/watch?v=2-DNswzCkqk
def jumping():
    global key_up
    if key_up == True:
        global jump
        global jumpcount
        global neg
        global boundary
        global y
        if y > 425:
            boundary = True
        if boundary == False:
            if jumpcount >= -13:
                neg = 1
                if jumpcount < 0:
                    neg = -1
                y -= (jumpcount ** 2) * 0.25 * neg 
                jumpcount -=1
            else:
                jump = False
                jumpcount = 13
                key_up = False
                y = 425

# mario moving left and right function
def move_left_right():
    global key_left
    global key_right
    global x
    global mario_current_img
    # moving mario left and right
    if key_left == True:
        mario_current_img = mario_left_img
        #making sure mario stays within the borders
        if x > 0:
            x = x - 7
    if key_right == True:
        mario_current_img = mario_right_img
        #making sure mario stays within the borders
        if x < 725:
            x = x + 7

# the background scene inside the game
def scene_setup():
    background(167, 219, 242)
    
    # sun
    stroke(255, 220, 0)
    fill(255, 220, 0)
    ellipse(200, 100, 100, 100)
    
    # cloud 1
    stroke(255)
    fill(255)
    ellipse(600, 123, 200, 50)
    ellipse(590, 95, 100, 50)
    ellipse(640, 150, 100, 30)
    ellipse(565, 150, 100, 30)
        
    # cloud 2
    ellipse(150, 175, 200, 50)
    ellipse(140, 145, 100, 50)
    ellipse(190, 200, 100, 30)
    ellipse(115, 200, 100, 30)
    
    # grass
    stroke(12, 124, 0)
    fill(12, 124, 0)
    rect(0, 470, 800, 30)

def setup():
    size(800, 500)
    background(167, 219, 242)
    # I loaded all the images here
    global mario_right_img
    mario_right_img = loadImage("mario right.png")
    global mario_left_img
    mario_left_img = loadImage("mario left.png")
    global mario_current_img
    mario_current_img = mario_right_img
    global rock_1_img
    rock_1_img = loadImage("rock 1.png")
    global rock_2_img
    rock_2_img = loadImage("rock 2.png")
    global star
    star = loadImage("star.png")
    global empty_star
    empty_star = loadImage("empty star.png")
    
def keyPressed():
    # if left arrow is pressed, mario moves left
    # if right arrow is pressed, mario moves right
    # if up arrow is pressed, mario jumps
    global key_left
    global key_right
    global key_up
    global menu
    if keyCode == LEFT:
        key_left = True
    else:
        key_left = False
    if keyCode == RIGHT:
        key_right = True
    else:
        key_right = False
    if keyCode == UP:
        key_up = True
    # when you are dead and press b, the game goes to the menu (I found that this works when you press any key).
    # going to the menu after pressing any button on the keyboard is better, so I did not change this code
    if keyCode == "B" or "b":
        menu = True
    
def mousePressed():
    global level_one
    global level_two
    # on the menu screen, if button clicked, go to that level
    if mouseX > 150 and mouseX < 350 and mouseY > 300 and mouseY < 400:
        level_one = True
    if mouseX > 450 and mouseX < 650 and mouseY > 300 and mouseY < 400:
        level_two = True

def draw():
    background(167, 219, 242)
    # I globalled everything because I reset the variables when I go back to the menu
    global x
    global y
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    global x4
    
    global speed1
    global speed2
    global random_num
    global random_num2
    
    global jump
    global jumpcount
    global boundary
    
    global key_left
    global key_right
    global key_up
    global menu
    
    global level_one
    global level_two
    global end_game_1
    global end_game_2
    
    global time_num
    global frames
    global frame_jump
    global frames_when_dead
    
    global star_1_lvl_1
    global star_2_lvl_1
    global star_3_lvl_1
    
    global star_1_lvl_2
    global star_2_lvl_2
    global star_3_lvl_2
    
    global mario_current_img
    
    # level one
    if level_one == True:
        collision()
        scene_setup()
        
        # 3, 2, 1 screen
        frames = frames + 1
        fill(0, 97, 112)
        stroke(0)
        if frames < 60:
            textSize(100)
            text("3", 375, 275)
        elif frames < 120:
            text("2", 375, 275)
        elif frames < 180:
            text("1", 375, 275)
        else:
            # inside game
            if end_game_1 == False:
                menu = False
                
                # scoreboard
                time_num = time_num + 1
                stroke(0)
                fill(0, 97, 112)
                textSize(25)
                text("YOUR TIME: " + str(time_num/60), 600, 40)
                
                # moving mario left, right, and up
                move_left_right()
                jumping()
                image(mario_current_img, x, y, 75, 75)
                
                # rock 1
                image(rock_1_img, x1, y1, 100, 100)
    
                # make speed go up exponentially, but limited the speed to 13.5
                if speed1 < 13.5:
                    speed1 = speed1 + 0.0003*speed1
                
                # rock 1 speed goes up    
                y1 = y1 + speed1

                # move rock 1 up after it goes off screen
                if y1 > 500:
                    y1 = -200
        
                    # move rock 1 position randomly
                    random_num = 0
                    import random
                    random_num = random.randint(-325, 400)
                    x1 = 325 + random_num
    
                # rock 2
                image(rock_2_img, x2, y2, 100, 100)
            
                # rock 2 speed goes up
                y2 = y2 + speed1
        
                # move rock 2 up after it goes off screen
                if y2 > 500:
                    y2 = -200
        
                    # move rock 2 position randomly
                    import random
                    random_num = random.randint(-325, 400)
                    x2 = 325 + random_num
            else:
                # You died screen
                fill(0, 97, 112)
                textSize(70)
                text("You Died", 250, 150)
                textSize(25)
                fill(0)
                text("Your Time: " + str(time_num/60), 320, 215)
                
                # if over certain time, show certain amount of stars
                if time_num/60 >= 60:
                    star_3_lvl_1 = True
                    image(star, 320, 250, 50, 50)
                    image(star, 380, 250, 50, 50)
                    image(star, 440, 250, 50, 50)
                elif time_num/60 >= 40:
                    star_2_lvl_1 = True
                    image(star, 320, 250, 50, 50)
                    image(star, 380, 250, 50, 50)
                    image(empty_star, 440, 250, 50, 50)
                elif time_num/60 >= 20:
                    star_1_lvl_1 = True
                    image(star, 320, 250, 50, 50)
                    image(empty_star, 380, 250, 50, 50)
                    image(empty_star, 440, 250, 50, 50)
                else:
                    image(empty_star, 320, 250, 50, 50)
                    image(empty_star, 380, 250, 50, 50)
                    image(empty_star, 440, 250, 50, 50)
                    
                # if you accidently press a button right after you die, it doesn't go back to the screen immediately
                text("Press Any Key to Return to Menu", 210, 400)
                frames_when_dead = frames_when_dead + 1
                if frames_when_dead/60 > 2:
                    if menu == True:
                        # reset all variables to original values
                        reset_variables()

    elif level_two == True:
        collision()
        scene_setup()
        
        # 3, 2, 1 screen
        frames = frames + 1
        fill(0, 97, 112)
        stroke(0)
        if frames < 60:
            textSize(100)
            text("3", 375, 275)
        elif frames < 120:
            text("2", 375, 275)
        elif frames < 180:
            text("1", 375, 275)
        else:
            #inside level two
            if end_game_2 == False:
                menu = False
                
                # scoreboard
                stroke(0)
                fill(0, 97, 112)
                time_num = time_num + 1
                textSize(25)
                text("YOUR TIME: " + str(time_num/60), 600, 40)
                
                # moving mario left, right, and up
                move_left_right()
                jumping()
                image(mario_current_img, x, y, 75, 75)
                
                # first vetical rock
                image(rock_2_img, x2, y2, 100, 100)
                
                # make first rock speed go up at constant rate
                y2 = y2 + 6
        
                # move first rock up after it goes off screen
                if y2 > 500:
                    y2 = -200
        
                    # move first rock position randomly
                    import random
                    random_num = random.randint(-325, 400)
                    x2 = 325 + random_num
                
                # second vertical rock        
                image(rock_2_img, x3, y3, 100, 100)
                
                # make second rock speed go up
                y3 = y3 + 6
        
                # move second rock up after it goes off screen
                if y3 > 500:
                    y3 = -200
        
                    # move second rock position randomly
                    import random
                    random_num = random.randint(-325, 400)
                    x3 = 325 + random_num
                
                # third horizontal rock
                image(rock_1_img, x4, 400, 100, 100)
                
                # make speed for 3rd rock go up exponentially, but limit the speed to 13.5
                if speed2 < 13.5:
                    speed2 = speed2 + 0.0003*speed2
                
                x4 = x4 - speed2
                
                # randomize position of horizontal rock slightly when it goes off screen
                if x4 < -100:
                    import random
                    random_num2 = random.randint(0, 1000)
                    x4 = 800 + random_num2
                
            else:
                # You died screen
                fill(0, 97, 112)
                textSize(70)
                text("You Died", 250, 150)
                textSize(25)
                fill(0)
                global frames_when_dead
                frames_when_dead = frames_when_dead + 1
                text("Your Time: " + str(time_num/60), 320, 215)
                
                # shows number of stars which is depended on the time
                if time_num/60 >= 45:
                    star_3_lvl_2 = True
                    image(star, 320, 250, 50, 50)
                    image(star, 380, 250, 50, 50)
                    image(star, 440, 250, 50, 50)
                elif time_num/60 >= 30:
                    star_2_lvl_2 = True
                    image(star, 320, 250, 50, 50)
                    image(star, 380, 250, 50, 50)
                    image(empty_star, 440, 250, 50, 50)
                elif time_num/60 >= 15:
                    star_1_lvl_2 = True
                    image(star, 320, 250, 50, 50)
                    image(empty_star, 380, 250, 50, 50)
                    image(empty_star, 440, 250, 50, 50)
                else:
                    image(empty_star, 320, 250, 50, 50)
                    image(empty_star, 380, 250, 50, 50)
                    image(empty_star, 440, 250, 50, 50)
                    
                # when you die and accidently press a button, it does not immediately go to menu
                text("Press Any Key to Return to Menu", 210, 400)
                if frames_when_dead/60 > 2:
                    if menu == True:
                        # reset all variables to original values
                        reset_variables()
                
    else:
        # Menu (Main Screen)
        stroke(0)
        fill(239, 179, 90)
        rect(450, 300, 200, 100)
        rect(150, 300, 200, 100)
        stroke(255)
        fill(154, 0, 0)
        textSize(75)
        text("Moving Mario", 160, 150)
        fill(0, 97, 112)
        textSize(20)
        text("Created by Avi Shah", 305, 225)
        textSize(15)
        text("Controls: Left, Right, Down, Up", 300, 460)
        fill(0)
        textSize(40)
        
        # stars next to level one 
        text("Level 1", 180, 365)
        image(empty_star, 180, 250, 50, 50)
        image(empty_star, 230, 250, 50, 50)
        image(empty_star, 280, 250, 50, 50)
        if star_3_lvl_1 == True:
            image(star, 180, 250, 50, 50)
            image(star, 230, 250, 50, 50)
            image(star, 280, 250, 50, 50)
        elif star_2_lvl_1 == True:
            image(star, 180, 250, 50, 50)
            image(star, 230, 250, 50, 50)
        elif star_1_lvl_1 == True:
            image(star, 180, 250, 50, 50)
        
        # stars next to level two
        text("Level 2", 480, 365)
        image(empty_star, 480, 250, 50, 50)
        image(empty_star, 530, 250, 50, 50)
        image(empty_star, 580, 250, 50, 50)
        if star_3_lvl_2 == True:
            image(star, 480, 250, 50, 50)
            image(star, 530, 250, 50, 50)
            image(star, 580, 250, 50, 50)
        elif star_2_lvl_2 == True:
            image(star, 480, 250, 50, 50)
            image(star, 530, 250, 50, 50)
        elif star_1_lvl_2 == True:
            image(star, 480, 250, 50, 50)
