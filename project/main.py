import pygame
import sys
linksgehen = pygame.image.load("project/Grafiken/Mainbild.png")
rechtsgehen = pygame.image.load("project/Grafiken/Mainbild.png")
hochgehen = pygame.image.load("project/Grafiken/Mainbild.png")
runtergehen = pygame.image.load("project/Grafiken/Mainbild.png")
Fackelschein = pygame.image.load("project/Grafiken/blurr.png")
hintergrund = pygame.image.load("project/Grafiken/background.png")
Tuere = False
def winning():
    print("you won")
    global Go
    Go=False
class spieler:
    def __init__(self,x,y,geschw,breite,hoehe,richtg,schritteLinks,schritteRechts):
        self.x = x
        self.y = y
        self.geschw = geschw
        self.breite = breite
        self.hoehe = hoehe
        self.richtg = richtg
        self.schritteLinks = schritteLinks
        self.schritteRechts = schritteRechts
        self.last = [0,0,0,0]
        self.ok = True  
    def laufen(self, Liste, geschw):
        if Liste[0]:
             self.x -= geschw
             self.richtg = [1,0,0,0]
             self.schritteLinks += 1
        elif Liste[1]:
             self.x += geschw
             self.richtg = [0,1,0,0]
             self.schritteRechts += 1
        elif Liste[2]:
             self.y -= geschw
        elif Liste[3]:
             self.y += geschw
        if spielerrechteck.colliderect(ziel): winning()
    def anderslaufen(self, Liste): #nicht notwendig
        if Liste[1]:
             self.x -= self.geschw
             self.richtg = [1,0,0,0]
             self.schritteLinks += 1
        elif Liste[0]:
             self.x += self.geschw
             self.richtg = [0,1,0,0]
             self.schritteRechts += 1
        elif Liste[3]:
             self.y -= self.geschw
        elif Liste[2]:
             self.y += self.geschw
def zeichnen():
    if Tuere == False:  
        door = pygame.draw.rect(screen, (100,100,100),(657, 332, 20, 66), 0) 
       
    else:  
        door = pygame.draw.rect(screen, (100,100,100),(657, 332, 66, 5), 0)
        
    
    
    ziel = pygame.draw.rect(screen, (200,10,47), (1200, 100, 50,50), 0)
    barrier4 = pygame.draw.rect(screen, (200,200,100),(0, 250, 677, 82), 0)
    screen.blit(Fackelschein, (spieler1.x-1900, spieler1.y-1050))
    screen.blit(linksgehen, (spieler1.x,spieler1.y)) 


screen = pygame.display.set_mode([1290,717])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
spieler1 = spieler(10,350,4,42,46,[0,0,0,0,1],0,0)

linkeWand = pygame.draw.rect(screen, (0,0,0), (0,0,2,717), 0)
obereWand = pygame.draw.rect(screen, (0,0,0), (0,0,1278,1),0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1278,0,2,717), 0)
untereWand = pygame.draw.rect(screen, (0,0,0), (0,716,1278,717),0)
barrier1 = pygame.draw.rect(screen, (0,0,0),(800, 112, 77, 456), 0)
barrier2 = pygame.draw.rect(screen, (0,0,0),(0, 397, 677, 82), 0)
barrier3 = pygame.draw.rect(screen, (100,100,100),(0, 250, 677, 82), 0)
door = pygame.draw.rect(screen, (100,100,100),(657, 332, 20, 66), 0)
ziel = pygame.draw.rect(screen, (200,10,47), (1200, 100, 50,50), 0)
Walls = [rechteWand, linkeWand, obereWand, barrier1, barrier2, barrier3, untereWand, door]
richtung = [1,0,0,0]
dorrad = pygame.draw.rect(screen,(0,0,0), (630, 332, 90, 66), 0) #Radius um Tür für Interaktion
Go = True
savex = 10
savey = 350
save2x = 10
save2y = 350
timer = 0
doorcount = 0
while Go:
    move = True
    spielerrechteck = pygame.Rect(spieler1.x, spieler1.y, 42, 46) 
    screen.blit(hintergrund, (0,0))
    gedrueckt = pygame.key.get_pressed()
    for event in pygame.event.get():#Tastatur/Spielefenstereingaben abgreifen
        if event.type ==pygame.QUIT: sys.exit()#Spiel schließen
    counter = 0
    if doorcount != 0: doorcount -= 1 #Zählvariable, um "Türspammen" zu verhindern
    elif gedrueckt[pygame.K_e]:
            if spielerrechteck.colliderect(dorrad):
                if doorcount <= 0:
                    if door in Walls: Walls.remove(door)
                    if Tuere == False:
                        Tuere = True
                    else: 
                        Tuere = False
                        Walls.append(door)
                    doorcount = 20
    
    
    if gedrueckt[pygame.K_RIGHT]:# and not spielerRechteck.colliderect(rechteWand):#Pfeiltaste rechts
        spieler1.laufen([0,1,0,0], spieler1.geschw)
        richtung = [0,1,0,0]
    elif gedrueckt[pygame.K_LEFT]: #and not spielerRechteck.colliderect(linkeWand):#Pfeiltaste links
        spieler1.laufen([1,0,0,0], spieler1.geschw)
        richtung = [1,0,0,0]
    elif gedrueckt[pygame.K_UP]:
        spieler1.laufen([0,0,1,0], spieler1.geschw)
        richtung = [0,0,1,0]
    elif gedrueckt[pygame.K_DOWN]:
        spieler1.laufen([0,0,0,1], spieler1.geschw)
        richtung = [0,0,0,1]
    else:
        move = False
 
    for wall in Walls: 
        if spielerrechteck.colliderect(wall):
             counter += 1
    if counter != 0:
        if move == True:
            spieler1.x=save2x
            spieler1.y=save2y
    
    
       
    if savex != spieler1.x or savey != spieler1.y:
        save2x = savex
        save2y = savey

        savex = spieler1.x
        savey = spieler1.y
    #richtung = [0,0,0,0,1] Links,Rechts, Hoch, Runter, Stehen
    clock.tick(30)
       
    zeichnen() 
     

    pygame.display.update()