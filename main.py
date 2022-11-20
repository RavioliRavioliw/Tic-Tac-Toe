import pygame as pyg
import buttons

pyg.init()

#screen resolution
reso_x = 900
reso_y = 900

#colors
color = (150, 255, 200)
black = (0, 0 , 0)
blue = (0, 0, 255)
red = (255, 0, 0)



#turn
turn = 1



#clock
clock = pyg.time.Clock()

screen = pyg.display.set_mode((reso_x, reso_y))
pyg.display.set_caption("tic tac toe 2")

background = pyg.Surface(screen.get_size())
background = background.convert()
background.fill((color))


#grills

grill = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


winer = 0

#images load
start = pyg.image.load("img/start_button.png").convert_alpha()
exit = pyg.image.load("img/exit_button.png").convert_alpha()
main_menu = pyg.image.load("img/pagina_principal.png").convert_alpha()
p_1_win = pyg.image.load("img/player_1_win.png").convert_alpha()
p_2_win = pyg.image.load("img/player_2_win.png").convert_alpha()
restart = pyg.image.load("img/restart_button.png").convert_alpha()
tie = pyg.image.load("img/draw.png").convert_alpha()

#give the image rects and properties of click
start_button = buttons.Button(323, 319, start, 0.8)
exit_button = buttons.Button(327, 662, exit, 0.8)
restart_button = buttons.Button(313, 505, restart, 0.7)

#functions

#the grill lines
def Lines():
	pyg.draw.line(screen, black, (reso_x // 3, 0), (reso_x // 3, reso_y), 10)
	pyg.draw.line(screen, black, ((reso_x // 3) * 2, 0), ((reso_x // 3) * 2, reso_y), 10)
	pyg.draw.line(screen, black, (0, reso_y // 3), (reso_x, reso_y // 3), 10)
	pyg.draw.line(screen, black, (0, (reso_y // 3) * 2), (reso_x, (reso_y // 3) *2), 10)
	
#drawing the cross
def cross(x, y):
	pyg.draw.line(screen, blue, (x * 300 + 10, y * 300 + 10), (x * 300 + 290, y * 300 + 290), 10)
	pyg.draw.line(screen, blue, (x * 300 + 10, y * 300 + 300), (x * 300 + 290, y * 300), 10)

#drawing the circle
def circle(x, y):
	pyg.draw.circle(screen, red, (x * 300 + 150, y * 300 + 150), 140, 2)
	

#win
def win():
	global winer
	global grill
	#vertical

	for x in grill:
		if sum(x) == 3:
			winer = 1
			
		
		if sum(x) == 27:
			winer = 2
			


		#-----
		if grill[0][0] == 1 and grill[1][0] == 1 and grill[2][0] == 1:
			winer = 1
			
		if grill[0][1] == 1 and grill[1][1] == 1 and grill[2][1] == 1:
			winer = 1
			
		if grill[0][2] == 1 and grill[1][2] == 1 and grill[2][2] == 1:
			winer = 1
					
		if grill[0][0] == 1 and grill[1][1] == 1 and grill[2][2] == 1:
			winer = 1
			
		if grill[2][0] == 1 and grill[1][1] == 1 and grill[0][2] == 1:
			winer = 1
			
		#------------------------

		if grill[0][0] == 9 and grill[1][0] == 9 and grill[2][0] == 9:
			winer = 2
			
		if grill[0][1] == 9 and grill[1][1] == 9 and grill[2][1] == 9:
			winer = 2
		
		if grill[0][2] == 9 and grill[1][2] == 9 and grill[2][2] == 9:
			winer = 2
				
		if grill[0][0] == 9 and grill[1][1] == 9 and grill[2][2] == 9:
			winer = 2
			
		if grill[2][0] == 9 and grill[1][1] == 9 and grill[0][2] == 9:
			winer = 2
				
		#-------------------------------------
		#check tie
		if sum(grill[0]) + sum(grill[1]) + sum(grill[2]) == 41:
			winer = 3
			
#-------------------------------------------------------------------------------

#some variables
game_start = False
click = False


screen.blit(background, (0, 0))
	
def Main_menu():
	core = True
	screen.blit(background, (0, 0))


	while core:

		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				pyg.quit()

		screen.blit(main_menu, (0, 0))
		if exit_button.draw(screen):
			pyg.quit()
		if start_button.draw(screen):
			play_game()
			core = False
			
			
#-------------------------------------------------------------------------------

		clock.tick(60)
		pyg.display.update()
	return

def player_1_win():
	global winer
	global grill
	global turn
	turn = 1

	while True:
		screen.blit(p_1_win, (0, 0))
		if restart_button.draw(screen):
			winer = 0
			grill = [[0,0,0], [0, 0, 0], [0, 0, 0]]
			Main_menu()
			
			



		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				pyg.quit()

		clock.tick(60)
		pyg.display.update()

#----------------------------------------------------------------------------
def player_2_win():
	global winer
	global grill
	global turn
	turn = 1

	while True:
		screen.blit(p_2_win, (0, 0))
		if restart_button.draw(screen):
			winer = 0
			grill = [[0,0,0], [0, 0, 0], [0, 0, 0]]
			Main_menu()
			
			



		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				pyg.quit()

		clock.tick(60)
		pyg.display.update()
#------------------------------------------------------------------------------------
def tiee():
	global winer
	global grill
	global turn
	turn = 1

	while True:
		screen.blit(tie, (0, 0))
		if restart_button.draw(screen):
			winer = 0
			grill = [[0,0,0], [0, 0, 0], [0, 0, 0]]
			Main_menu()
			
			



		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				pyg.quit()

		clock.tick(60)
		pyg.display.update()

#------------------------------------------------------------------------------------



def play_game():
	screen.blit(background, (0, 0))
	global winer
	global turn

	core = True

	while core:
		
		
		if winer == 1:
			player_1_win()
			core = False
		if winer == 2:
			player_2_win()
			core = False
		if winer == 3:
			tiee()
			core = False
			
			
			

		for event in pyg.event.get():
			if event.type == pyg.QUIT:
				pyg.quit()


			win()
			Lines()
			if event.type == pyg.MOUSEBUTTONDOWN:

				pos_x = event.pos[0]
				pos_y = event.pos[1]

				grill_x = pos_x // 300
				grill_y = pos_y // 300

				if grill[grill_x][grill_y] == 0:
					if turn == 1:
						grill[grill_x][grill_y] = 1
						cross(grill_x, grill_y)
						turn *= -1
					else:
						grill[grill_x][grill_y] = 9
						circle(grill_x, grill_y)
						turn *= -1


		

		clock.tick(60)
		pyg.display.update()
	return




	



if __name__ == '__main__':
	Main_menu()
	
