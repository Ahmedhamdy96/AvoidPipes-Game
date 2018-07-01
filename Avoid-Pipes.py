import pygame
from pygame.locals import * 
import random 

pygame.init() 

# defining colors  
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# creating the game display 
wedith = 1000 
hight = 750 

screen = pygame.display.set_mode((wedith,hight), 0 , 32 )
pygame.display.set_caption("Avoid Pipes Game")

# clock object to track time 
clock = pygame.time.Clock()

# ball initial position 
x_ball  = wedith/2 
y_ball = hight/2 
radious = 20 
# pipes initial position  
x_pipes = 200 
y_pipes = 200 

# pipes shape parameters  
pipes_wedith = 60
pipe_hight = random.randrange(0,500)
pipe_color = white 
# to control falling speed 
gravity =  600
# set speeds for  the ball and pipes moving 
speed_ball = 400 
speed_pipes = 400 
# initial score 
score = 0

# creating texts 
# my name :D  
name_font = pygame.font.SysFont("ubuntu",15)
name_font_font_surface = name_font.render(" Ahmed Hamdy " , True , gray , None)    
name_font_x = hight + 100
name_font_y = wedith - 300 

# your score info
your_score = pygame.font.SysFont("ubuntu" , 20 )
your_score_surface = your_score.render(" Your Score " ,  True , gray , None)
your_score_x = wedith - 150 
your_score_y = 50 

# displaying score
score_font = pygame.font.SysFont("ubuntu" , 30 )
score_font_x = wedith - 100 
score_font_y = 100


# game over 
game_over = pygame.font.SysFont("ubuntu",60)
game_over_surface = game_over.render(" Game Over " , True , white , None )
game_over_x = wedith/2 - 130
game_over_y = hight/2 - 100

# try again 
try_again = pygame.font.SysFont("ubuntu" , 30 )
try_again_surface = try_again.render("Try Again . . . " , True , white , None)
try_again_x = wedith/2 - 100
try_again_y = hight/2 


final_score_x = wedith/2 	
final_score_y = 100 


# game loop 
while True :
	# a pygame function > get the state of all keyboard buttons
	pressed_key = pygame.key.get_pressed()  
	# clock.tick() returns the time ( in milliseconds ) between two frames 
	# may take an optional parameter which is the maximum frame rate clock.tick(FBS)
	time_passed = clock.tick()
	# converting time to be in seconds 
	time_passed_seconds = time_passed / 1000.0
	# v = x / t 
	# we need to move in a specific speed (v)
	# and we have the time between to frame (t)
	# so , we need to calculate the distace we should move in each frame to move in this speed 
	
	y_distance = time_passed_seconds * speed_ball     # ball speed  
	pipe_distance = time_passed_seconds * speed_pipes # pipes speed

	# handle events 
	for event in pygame.event.get() :
	# QUIT = the window X button   
		if event.type==QUIT: 
			exit()
	# to move ball up if we keep pressing  [ space ] or [ ^ ]  		
	if pressed_key[K_UP] or pressed_key[K_SPACE] : 
		y_ball -=y_distance
	# to keep ball inside the game display and not escape 
		if y_ball <= 0 : 
			y_ball = 0  
	
	# >>>> testing <<<< 		
	#if pressed_key[K_DOWN] : 
	#	y_ball +=y_distance
	

	# to make ball fall down if we don't press [ space ] or [ ^ ]
	else : 
		y_ball += y_distance + ( time_passed_seconds*gravity ) # gravity = pixle / sec so,we multiply by time to obtain distance
	# to keep ball inside the game display and not escape
		if y_ball >= hight : 
			y_ball = hight
	
	# during game pipes moves from the left side to the right side of the screen 
	x_pipes += pipe_distance 
	y_pipes = 0 
	

	# score is increasing if the pipes reaches the right side of the screen  
	if x_pipes >= wedith :  
		# start from the left side again 
		x_pipes = 0
		score += 1 
		# print(score)
		# regenerate a random hight  
		pipe_hight = random.randrange(0,500)

	if (x_ball+radious)<=(x_pipes+pipes_wedith) and (x_ball+radious)>=x_pipes : 
		if (y_ball - radious) > pipe_hight and (y_ball + radious) < pipe_hight+200 : 
			pipe_color = green
		else :  
			pipe_color = red
			if x_pipes > x_ball : 
				#print("Your Score is  : {} ".format(score))
				

				final_score = pygame.font.SysFont("ubuntu" , 90 ) 
				final_score_surface = final_score.render(str(score) , True , green , None)

				screen.fill(black)
				screen.blit(final_score_surface , (final_score_x , final_score_y ))
				screen.blit(game_over_surface , (game_over_x,game_over_y))
				screen.blit(try_again_surface , (try_again_x , try_again_y))

				pygame.display.update()
				pygame.time.delay(1000)
				score = 0
				#exit()
	else :  
		pipe_color = white

    # Drawing
	screen.fill(black)

	# display name on game display 
	screen.blit(name_font_font_surface, (name_font_x,name_font_y))
	
	screen.blit(your_score_surface , (your_score_x , your_score_y ))

	# rerendering score 
	score_font_surface = score_font.render(str(score) , True , white , None)
	screen.blit(score_font_surface , (score_font_x,score_font_y))
	
	pygame.draw.circle(screen , blue ,(int(x_ball) , int(y_ball)) , radious)
	pygame.draw.rect( screen  ,  pipe_color  , (  x_pipes , y_pipes , pipes_wedith ,  pipe_hight ) ) # upper 
	pygame.draw.rect( screen  ,  pipe_color  , (  x_pipes , hight , pipes_wedith ,   -( hight - pipe_hight)+200 ) ) # lower 	

	# updating screen 
	pygame.display.update() 
