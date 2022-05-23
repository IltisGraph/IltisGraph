import pygame as pg
import random
import time
actuall = 0
curl = 1
Chests = []
cwtd = ""

whattodo = ""
class Spieler(pg.sprite.Sprite):
	def __init__(self, x, y, block = "Stein", blockin = None):
		self.x, self.y = x, y
		self.Blockus = block
		self.Blockin = blockin
		self.Blocku = None
		self.BlockR = None
		self.BlockL = None
		self.BlockL2, self.BlockR2 = None, None
		self.image = pg.image.load("PushyP.png")
		self.Bild = self.image
	def move(self, direction):
		if direction == "R" and self.checkifpossible("R"):
			self.x += 65
		if direction == "L" and self.checkifpossible("L"):
			self.x -= 65
	def checkifpossible(self, direction):
		whattor = None
		if direction == "L" and (self.x - 65) >= 20 and (self.BlockL == "Luft" or self.BlockL == None or self.BlockL == "Liane" or self.checkMK("L", whattodo)):
			whattor = True
		if direction == "R" and (self.x + 65) <= 1905 and (self.BlockR == "Luft" or self.BlockR == None or self.BlockR == "Liane" or self.checkMK("R", whattodo)):
			whattor = True
		
		if whattor == True:
			return True
		if whattor == None:
			return False
	def moveud(self, ud):
		if ud == "U" and self.checkud("U"):
			self.y -= 75
		if ud == "D" and self.checkud("D"):
			self.y += 75
	def checkud(self, ud):
		if ud == "U" and self.Blockin == "Liane" and (self.Blocku == "Luft" or self.Blocku == "Liane" or self.Blocku == None):
			return True
		if ud == "D" and (self.Blockus == "Liane" or self.Blockus == "Luft"):
			return True
	def fall(self):
		self.Blockus = None
		self.y += 25
	
	# Kisten Bewegen
	def moveK(self, d, wtd):
		if d == "R" and self.checkMK("R", wtd):
			pass
		if d == "L" and self.checkMK("L", wtd):
			pass
			
	def checkMK(self, d, wtd):
		global whattodo
		brake = False
		print("hihihi")
		
		for i in range(len(wtd)):
			for b in range(len(wtd[i])):
				c = wtd[i][b]
				print("DO")
				if d == "R" and wtd[i][b].x == Pushy.x +65 and wtd[i][b].y == Pushy.y - 10 and self.checkifV("R"):
					ch = None
					for d in range(len(Chests)):
						h = Chests[d]
						if h.x == c.x and h.y == c.y:
							ch = d
							print("t2HE"*100)
							print("i: " + str(i))
							print("b: " + str(b))
							break
					
					Chests[ch].x += 65
					wtd[i][b].x += 65
						
					
					print("gemacht")
					for f in range(len(wtd[i])):
						if wtd[i][f].x == Chests[ch].x and wtd[i][f].y == Chests[ch].y and wtd[i][f].typer == "Luft":
							wtd[i][f].x -= 65
					whattodo = wtd
					return True
					brake = True
					break
				if d == "L" and wtd[i][b].x == Pushy.x - 65 and wtd[i][b].y == Pushy.y - 10 and self.checkifV("L"):
					ch = None
					for d in range(len(Chests)):
						h = Chests[d]
						if h.x == c.x and h.y == c.y:
							ch = d
							break
					
					Chests[ch].x -= 65
					wtd[i][b].x -= 65
					li = i
					lb = b
					print("i: "+ str(li), "b: " + str(lb))
					print("x: " + str(wtd[li][lb].x))
						
					print("Gemacht")
					for f in range(len(wtd[i])):
						if wtd[i][f].x == Chests[ch].x and wtd[i][f].y == Chests[ch].y and wtd[i][f].typer == "Luft":
							wtd[i][f].x += 65
					cwtd = whattodo
					whattodo = wtd
					
					
					
					return True
					brake = True
					break
			if brake == True:
				break
				
				
		whattodo = wtd
		
	
	def checkifV(self, d):
		if d == "R" and (self.BlockR2 == "Luft") and self.BlockR == "Kiste":
			return True
		if d == "L" and self.BlockL2 == "Luft" and self.BlockL == "Kiste":
			return True
		
class Stone(pg.sprite.Sprite):
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.schiebbar = False
		self.image = pg.image.load("Stein.png")
		self.Bild = self.image
		self.ret = True
		self.typer = "Stone"

class Liane(pg.sprite.Sprite):
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.schiebbar = False
		self.image = pg.image.load("Liane.png")
		self.Bild = self.image
		self.ret = True
		self.typer = "Liane"

class none():
	def __init__(self, x, y):
		self.x, self.y = x,y
		self.ret = False
	
		self.typer = "Luft"
		
class Barrel():
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.ret = False
		self.image = pg.image.load("Kiste.png")
		self.Bild = self.image
		
		self.typer = "Kiste"	

class Goal():
	def __init__(self, x, y):
		self.x, self.y = x, y
		self.ret = True
		self.image = pg.image.load("Tür.png")
		self.Bild = self.image
		self.typer = "Ziel"
		
		
def deAK():
	print("Blockus: " + str(Pushy.Blockus))
	print("Blocku: " + str(Pushy.Blocku))
	print("Blockin: " + str(Pushy.Blockin))
	print("x, y: " + str(Pushy.x) + " " + str(Pushy.y))
	print("L, R: " + str(Pushy.BlockL) + " " + str(Pushy.BlockR))
	print("l2, R2: " + str(Pushy.BlockL2) + " , " + str(Pushy.BlockR2))
	
		
	end = time.time()
	print("sek: " + str(end-start))
	#fps berechnen
	print("FPS: " + str(round((1) / (end - start))))
	
Lvl1 = [[3, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], [0, 0, 0, 2, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2], [1, 1, 1, 1, 1,1, 1, 1, 1, 1, 3, 3, 2, 3, 1, 1, 1, 1], [1, 0, 1, 1, 2, 1,0, 1], [1, 0, 1, 1, 1, 1, 2, 1], [1, 0, 1, 1,1]]
Pushy = Spieler(215, 85)
Stein = Stone(600, 500)

White = (255, 255, 255)
Green = (15, 179, 0)
Blue = (0, 66, 219)
Grey = (166, 166, 166)
pg.init()
Fenster = pg.display.set_mode((2000, 1000))

Fenster.fill(White)

#lvl decodieren
def decodeL(lvl):

	out = [[], [], [], [], [], []]
	for i in range(len(lvl)):
		for b in range(len(lvl[i])):
			if lvl[i][b] == 0:
				out[i].append(none(b*65+20, i*75 + 150))
			if lvl[i][b] == 1:
				out[i].append(Stone(b*65+20, i*75 + 150))
			if lvl[i][b] == 2:
				out[i].append(Liane(b*65+20, i*75 + 150))
			if lvl[i][b] == 3:
				out[i].append(Barrel(b*65+20, i*75 + 150))
				Chests.append(Barrel(b*65+20, i*75 + 150))
			if lvl[i][b] == 4:
				out[i].append(Goal(b*65+20, i*75 + 150))
				
	return out
				

def akstats():
	global actuall
	global curl
	global whattodo
	
	whattodo = decodeL(Lvl1)
	actuall += 1
	print("llvl decoded")
	#fallen + blöcke anzeigen
	
	for i in range(len(whattodo)):
		for b in range(len(whattodo[i])):
			c = whattodo[i][b]
			if whattodo[i][b].x == Pushy.x and whattodo[i][b].y == Pushy.y + 65:
				Pushy.Blockus = whattodo[i][b].typer
			if c.x == Pushy.x and c.y == Pushy.y - 10:
				Pushy.Blockin = c.typer
			if c.x == Pushy.x and c.y == Pushy.y -  85:
				Pushy.Blocku = c.typer
			if c.x == Pushy.x - 65 and c.y == Pushy.y - 10:
				Pushy.BlockL = c.typer
			if c.x == Pushy.x +65 and c.y == Pushy.y - 10:
				Pushy.BlockR = c.typer	
			if c.x == Pushy.x - 65 - 65 and c.y == Pushy.y - 10:
				Pushy.BlockL2 = c.typer
			if c.x == Pushy.x +65 + 65 and c.y == Pushy.y - 10:
				Pushy.BlockR2 = c.typer
			
				
				
while True:
	start = time.time()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			break
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_RIGHT:
				Pushy.move("R")
				#Pushy.moveK("R", whattodo)
			if event.key == pg.K_LEFT:
				Pushy.move("L")
				#Pushy.moveK("L", whattodo)
			if event.key == pg.K_UP:
				Pushy.moveud("U")
			if event.key == pg.K_DOWN:
				Pushy.moveud("D")
			if event.key == pg.K_a:
				deAK()
			if event.key == pg.K_s:
				print("*"*100)
				for i in whattodo[1]:
					
					print(str(i.x) + ", type: " + str(i.typer))
			if event.key == pg.K_d:
				print("Chests: " + str(len(Chests)))
				print("wtd: " + str(len(whattodo)))
			
				
			
	Fenster.fill(Blue)
	#untere spielfeldbegrenzung
	pg.draw.rect(Fenster, Grey, (-10, 1050, 2100, 100))
	# begrenzung rechts + links
	pg.draw.rect(Fenster, Grey, (-10, -10, 30, 1250))
	pg.draw.rect(Fenster, Grey, (1970, -10, 2100, 1250))
	
	
	# nach unten fallen
	
	Fenster.blit(Pushy.Bild, (Pushy.x, Pushy.y))
	#level anzeigen
	if curl != actuall:
		whattodo = decodeL(Lvl1)
		actuall += 1
		print("llvl decoded")
	#fallen + blöcke anzeigen
	
	for i in range(len(whattodo)):
		for b in range(len(whattodo[i])):
			c = whattodo[i][b]
			if whattodo[i][b].x == Pushy.x and whattodo[i][b].y == Pushy.y + 65:
				Pushy.Blockus = whattodo[i][b].typer
			if c.x == Pushy.x and c.y == Pushy.y - 10:
				Pushy.Blockin = c.typer
			if c.x == Pushy.x and c.y == Pushy.y -  85:
				Pushy.Blocku = c.typer
			if c.x == Pushy.x - 65 and c.y == Pushy.y - 10:
				Pushy.BlockL = c.typer
			if c.x == Pushy.x +65 and c.y == Pushy.y - 10:
				Pushy.BlockR = c.typer	
			if c.x == Pushy.x - 65 - 65 and c.y == Pushy.y - 10:
				Pushy.BlockL2 = c.typer
			if c.x == Pushy.x +65 + 65 and c.y == Pushy.y - 10:
				Pushy.BlockR2 = c.typer
			
	
			
			if whattodo[i][b].ret != False:
				Fenster.blit(whattodo[i][b].Bild, (whattodo[i][b].x, whattodo[i][b].y))
	if (Pushy.Blockus == "Luft" or Pushy.Blockus == None) and Pushy.y <= 960 and Pushy.Blockin != "Liane":
				Pushy.fall()
	if Pushy.y == 85:
		Pushy.Blockin == "Luft"
		Pushy.BlockR, Pushy.BlockL, Pushy.BlockR2, Pushy.Block2L= "Luft", "Luft", "Luft", "Luft"
	if Pushy.y == 985:
		Pushy.Blockus = "Stone"
		Pushy.Blockin = "Luft"
		Pushy.BlockR, Pushy.BlockL, Pushy.BlockR2, Pushy.Block2L= "Luft", "Luft", "Luft", "Luft"
	
	# kisten anzeigen
	for i in Chests:
		Fenster.blit(i.Bild, (i.x, i.y))
	pg.display.update()
	
	#debug
	end = time.time()
pg.quit()