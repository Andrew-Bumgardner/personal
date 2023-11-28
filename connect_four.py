import pygame
import math
import numpy as np


win = pygame.display.set_mode((700, 700))
width = 700
height = 700
sqr_size = 100
turn = 0
yellow = (255,255,0)
red = (255,0,0)
pygame.init()



# draw(surface, color, coords, dimensions)

def create_board():
	board = np.zeros((6,7))
	return board

board = create_board()

class piece(object):

	def __init__(self, pos, color):
		self.pos = pos
		self.color = color

	def recolor(self, color):
		self.color = color

	def move(self):
		mouse = pygame.mouse.get_pos()
		self.pos = (mouse[0], self.pos[1])

	def draw(self, surface):
		pygame.draw.circle(surface, self.color, (self.pos[0],self.pos[1]), 45)

hover_piece = piece((50, 50), yellow)

def is_valid_location(board, col):
	if board[0][col] == 0:
		return True
	else:
		return False


def mouse_click(mouse_pos):
	global turn
	
	col = 0

	if mouse_pos[0] <= 100:
		col = 0
	elif mouse_pos[0] <= 200 and mouse_pos[0] > 100:
		col = 1
	elif mouse_pos[0] <= 300 and mouse_pos[0] > 200:
		col = 2
	elif mouse_pos[0] <= 400 and mouse_pos[0] > 300:
		col = 3
	elif mouse_pos[0] <= 500 and mouse_pos[0] > 400:
		col = 4
	elif mouse_pos[0] <= 600 and mouse_pos[0] > 500:
		col = 5
	elif mouse_pos[0] <= 700 and mouse_pos[0] > 600:
		col = 6

	if is_valid_location(board, col) == True:
		drop_piece(col, hover_piece.color)

	turn += 1
	turn = turn % 2

def drop_piece(col, color):
	for x in range(1,7):
		if board[-x][col] == 0:
			if turn == 0:
				board[-x][col] = 1
				break
			elif turn == 1:
				board[-x][col] = 2
				break
		else:
			continue




def draw_board(surface):
	pygame.draw.rect(surface, (0,0,255), (0,100,700,600))
	for i in range(7):
		for j in range(6):
			if board[j][i] == 0:
				pygame.draw.circle(surface, (0,0,0), ((i*100)+50, (j*100)+150), 45)
			elif board[j][i] == 1:
				pygame.draw.circle(surface, yellow, ((i*100)+50, (j*100)+150), 45)
			elif board[j][i] == 2:
				pygame.draw.circle(surface, red, ((i*100)+50, (j*100)+150), 45)

def redraw_window(surface):
	surface.fill((0,0,0))
	draw_board(surface)
	hover_piece.draw(surface)
	pygame.time.delay(10)
	clock.tick(30)
	pygame.display.update()
	
def game_win(board, piece):
	
	# horizontal checking
	for y in range(6):
		for x in range(4):
			if board[y][x] == piece and board[y][x+1] == piece and board[y][x+2] == piece and board[y][x+3] == piece:
				return True

	# vertical checking
	for y in range(3):
		for x in range(7):
			if board[y][x] == piece and board[y+1][x] == piece and board[y+2][x] == piece and board[y+3][x] == piece:
				return True

	# diagonal checking
	
	# positive slope
	for y in range(1, 4):
		for x in range(4):
			if board[-y][x] == piece and board[-(y+1)][x+1] == piece and board[-(y+2)][x+2] == piece and board[-(y+3)][x+3] == piece:
				return True

	# negative slope
	for y in range(3):
		for x in range(4):
			if board[y][x] == piece and board[y+1][x+1] == piece and board[y+2][x+2] == piece and board[y+3][x+3] == piece:
				return True


window = pygame.display.get_surface()


flag = True
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 75)

while flag:
	
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_click(pygame.mouse.get_pos())


	hover_piece.move()
	redraw_window(win)

	if turn == 0:
		hover_piece.recolor(yellow)
		if game_win(board, 2):
			label = myfont.render("Player 1 wins!", 1, red)
			labelRect = label.get_rect()
			labelRect.center = (350, 50)

			win.blit(label, labelRect)
			flag = False


	elif turn == 1:
		hover_piece.recolor(red)
		if game_win(board, 1):
			label = myfont.render("Player 2 wins!", 1, red)
			labelRect = label.get_rect()
			labelRect.center = (350, 50)

			win.blit(label, labelRect)
			flag = False

	

	if flag == False:
		pygame.time.wait(3000)
