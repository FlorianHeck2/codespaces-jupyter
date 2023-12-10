#Bei diesem Projekt handelt es sich um eine Übung anhand eines Tutorials für pygame
import pygame
import sys

pygame.init()#Initalisiert pygame
hintergrund = pygame.image.load("Grafiken/hintergrund.png")#Pfad zu Bild
screen = pygame.display.set_mode([1200,595])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Tutorial")#Name der Anwendung

stehen = pygame.image.load("Grafiken/stand.png")
sprung = pygame.image.load("Grafiken/sprung.png")
rechtsgehen = [pygame.image.load("Grafiken/rechts1.png"), pygame.image.load("Grafiken/rechts2.png"), pygame.image.load("Grafiken/rechts3.png"), pygame.image.load("Grafiken/rechts4.png"), pygame.image.load("Grafiken/rechts5.png"), pygame.image.load("Grafiken/rechts6.png"), pygame.image.load("Grafiken/rechts7.png"), pygame.image.load("Grafiken/rechts8.png")]
linksgehen = [pygame.image.load("Grafiken/links1.png"), pygame.image.load("Grafiken/links2.png"), pygame.image.load("Grafiken/links3.png"), pygame.image.load("Grafiken/links4.png"), pygame.image.load("Grafiken/links5.png"), pygame.image.load("Grafiken/links6.png"), pygame.image.load("Grafiken/links7.png"), pygame.image.load("Grafiken/links8.png")]
sprungSound = pygame.mixer.Sound("Sounds/sprung.wav")
sprungSound.set_volume(0.1)

class spieler:
     def __init__(self,x,y,geschw,breite,hoehe,sprungvar,richtg,schritteLinks,schritteRechts):
          self.x = x
          self.y = y
          self.geschw = geschw
          self.breite = breite
          self.hoehe = hoehe
          self.sprungvar = sprungvar
          self.richtg = richtg
          self.schritteLinks = schritteLinks
          self.schritteRechts = schritteRechts
          self.sprung = False
     def laufen(self, Liste):
        if Liste[0]:
             self.x -= self.geschw
             self.richtg = [1,0,0,0]
             self.schritteLinks += 1
        if Liste[1]:
             self.x += self.geschw
             self.richtg = [0,1,0,0]
             self.schritteRechts += 1
     def resetSchritte(self):
          self.schritteRechts = 0
          self.schritteLinks = 0
     def stehen(self):
          self.richtg = [0,0,1,0]
          self.resetSchritte()
     def sprungSetzen(self):
          if self.sprungvar == -16:
            self.sprung = True
            self.sprungvar = 15
            pygame.mixer.Sound.play(sprungSound)
     def springen(self):
          if self.sprung:
                self.richtg = [0,0,0,1]
                if self.sprungvar >= -15:
                    n = 1
                    if self.sprungvar < 0:
                        n = -1
                    self.y -= (self.sprungvar**2)*0.17*n
                    self.sprungvar -= 1     
                else:
                     self.sprung = False 
     def spZeichnen(self):
        if self.schritteRechts == 63:
             self.schritteRechts = 0
        if self.schritteLinks == 63:
            self.schritteLinks = 0
        if self.richtg[0]:
             screen.blit(linksgehen[self.schritteLinks//8], (self.x,self.y))
        if self.richtg[1]:
             screen.blit(rechtsgehen[self.schritteRechts//8], (self.x,self.y))
        if self.richtg[2]:
             screen.blit(stehen, (self.x,self.y))
        if self.richtg[3]:
             screen.blit(sprung, (self.x,self.y))         

def zeichnen():
        global schritteLinks, schritteRechts #Zugriff als globale Variable und nicht klassenintern
        #screen.fill((0,0,0)) #Faerbt Bildschirm --> Spileer bewegt sich
        screen.blit(hintergrund, (0,0))
        #pygame.draw.rect(screen, (0,0,255), (x,y,breite,hoehe))#spielfigur
        spieler1.spZeichnen()

        pygame.display.update()

linkeWand = pygame.draw.rect(screen, (0,0,0), (0,0,2,600), 0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1199,0,2,600), 0)

spieler1 = spieler(300,391,5,96,128,-16,[0,0,1,0],0,0)

go = True
#[links, rechts, stand, sprung]
#richtg = [0, 0, 0, 0]


while go:#Mainloop --> hier läuft das Spiel ab
    for event in pygame.event.get():#Tastatur/Spielefenstereingaben abgreifen
        if event.type ==pygame.QUIT: sys.exit()#Spiel schließen

    spielerRechteck = pygame.Rect(spieler1.x,spieler1.y,96,128)
    gedrueckt = pygame.key.get_pressed()#schaut, ob zu Zeitpunkt Bewegung passiert
    richtg = [0,0,1,0]
    
    if gedrueckt[pygame.K_RIGHT] and not spielerRechteck.colliderect(rechteWand):#Pfeiltaste rechts
        spieler1.laufen([0,1])
    elif gedrueckt[pygame.K_LEFT] and not spielerRechteck.colliderect(linkeWand):#Pfeiltaste links
        spieler1.laufen([1,0])
    else: 
         spieler1.stehen()
    if gedrueckt[pygame.K_UP] and spieler1.sprungvar == -16:#Pfeiltaste oben, y-Achse invertiert
        spieler1.sprungSetzen()
    spieler1.springen()


    zeichnen()        
    clock.tick(60)#Anzahl FPS

