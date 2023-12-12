#Bei diesem Projekt handelt es sich um eine Übung anhand eines Tutorials für pygame
import pygame
import sys

pygame.init()#Initalisiert pygame
hintergrund = pygame.image.load("Grafiken/hintergrund.png")#Pfad zu Bild
screen = pygame.display.set_mode([1200,595])#Erzeugt Fenster mit Höhe und Breite in Pixeln
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Tutorial")#Name der Anwendung

angriffLinks = pygame.image.load("Grafiken/angriffLinks.png")
angriffRechts = pygame.image.load("Grafiken/angriffRechts.png")
sprung = pygame.image.load("Grafiken/sprung.png")
rechtsgehen = [pygame.image.load("Grafiken/rechts1.png"), pygame.image.load("Grafiken/rechts2.png"), pygame.image.load("Grafiken/rechts3.png"), pygame.image.load("Grafiken/rechts4.png"), pygame.image.load("Grafiken/rechts5.png"), pygame.image.load("Grafiken/rechts6.png"), pygame.image.load("Grafiken/rechts7.png"), pygame.image.load("Grafiken/rechts8.png")]
linksgehen = [pygame.image.load("Grafiken/links1.png"), pygame.image.load("Grafiken/links2.png"), pygame.image.load("Grafiken/links3.png"), pygame.image.load("Grafiken/links4.png"), pygame.image.load("Grafiken/links5.png"), pygame.image.load("Grafiken/links6.png"), pygame.image.load("Grafiken/links7.png"), pygame.image.load("Grafiken/links8.png")]
sprungSound = pygame.mixer.Sound("Sounds/sprung.wav")
sprungSound.set_volume(0.1)
siegSound = pygame.mixer.Sound("Sounds/robosieg.wav")
siegSound.set_volume(0.1)
verlorenSound = pygame.mixer.Sound("Sounds/robotod.wav")
verlorenSound.set_volume(0.1)
sieger = pygame.image.load("Grafiken/Sieg.png")
verlierer = pygame.image.load("Grafiken/verloren.png")

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
          self.last = [1,0]
          self.ok = True
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
             self.last = [1,0]
        if self.richtg[1]:
             screen.blit(rechtsgehen[self.schritteRechts//8], (self.x,self.y))
             self.last = [0,1]
        if self.richtg[2]:
             if self.last[0]:
               screen.blit(angriffLinks, (self.x, self.y))
             else:
                  screen.blit(angriffRechts, (self.x, self.y))
        if self.richtg[3]:
             screen.blit(sprung, (self.x,self.y))         
class kugel:
     def __init__(self,spX,spY,richtung,radius,farbe,geschw):
          self.x = spX
          self.y = spY
          if richtung[0]:
               self.x +=5
               self.geschw = -1*geschw
          elif richtung[1]:
               self.x += 92
               self.geschw = geschw
          self.y += 84
          self.radius = radius
          self.farbe = farbe
     def bewegen(self):
          self.x += self.geschw
     def zeichnen(self):
          pygame.draw.circle(screen, self.farbe, (self.x, self.y), self.radius, 0)
class Zombie:
     def __init__(self, x,y,geschw,breite,hoehe,richtg,xMin,xMax):
          self.x = x
          self.y = y
          self.geschw = geschw
          self.breite=breite
          self.hoehe = hoehe
          self.richtg = richtg
          self.schritteRechts = 0
          self.schritteLinks = 0
          self.xMin = xMin
          self.xMax = xMax
          self.leben = 6
          self.linksListe = [pygame.image.load("Grafiken/l1.png"),pygame.image.load("Grafiken/l2.png"),pygame.image.load("Grafiken/l3.png"),pygame.image.load("Grafiken/l4.png"),pygame.image.load("Grafiken/l5.png"),pygame.image.load("Grafiken/l6.png"),pygame.image.load("Grafiken/l7.png"),pygame.image.load("Grafiken/l8.png")]
          self.rechtsListe = [pygame.image.load("Grafiken/r1.png"),pygame.image.load("Grafiken/r2.png"),pygame.image.load("Grafiken/r3.png"),pygame.image.load("Grafiken/r4.png"),pygame.image.load("Grafiken/r5.png"),pygame.image.load("Grafiken/r6.png"),pygame.image.load("Grafiken/r7.png"),pygame.image.load("Grafiken/r8.png")]
          self.ganz = pygame.image.load("Grafiken/voll.png")
          self.halb = pygame.image.load("Grafiken/halb.png")
          self.leer = pygame.image.load("Grafiken/leer.png")

     def zZeichnen(self):
          if self.schritteRechts == 63:
               self.schritteRechts = 0
          elif self.schritteLinks == 63:
               self.schritteLinks = 0
          if self.richtg[0]:
               screen.blit(self.linksListe[self.schritteLinks//8], (self.x, self.y))
          if self.richtg[1]:
               screen.blit(self.rechtsListe[self.schritteRechts//8], (self.x, self.y))
     def Laufen(self):
          self.x += self.geschw
          if self.geschw > 0:
               self.richtg = [0,1]
               self.schritteRechts +=1
          else:
               self.richtg = [1,0]
               self.schritteLinks += 1
     def hinHer(self):
          if self.x > self.xMax:
               self.geschw *= -1
          elif self.x < self.xMin:
               self.geschw *= -1
          self.Laufen()
     def herzen(self):
          if self.leben >=2:
               screen.blit(self.ganz, (507,15))#Koordinate oben links
               if self.leben >= 4:
                    screen.blit(self.ganz, (569, 15))
                    if self.leben == 6:
                         screen.blit(self.ganz, (631,15))
                    elif self.leben == 5:
                         screen.blit(self.halb, (631,15))
               elif self.leben == 3:
                    screen.blit(self.halb, (569, 15))
          elif self.leben == 1:
               screen.blit(self.halb, (507,15))

          if self.leben <= 0:
               screen.blit(self.leer, (507,15))
          if self.leben <= 2:
               screen.blit(self.leer, (569, 15))
          if self.leben <= 4:
               screen.blit(self.leer, (631,15))

def zeichnen():
          global schritteLinks, schritteRechts, gewonnen, verloren #Zugriff als globale Variable und nicht klassenintern
        #screen.fill((0,0,0)) #Faerbt Bildschirm --> Spileer bewegt sich
          screen.blit(hintergrund, (0,0))
          for k in kugeln:
           k.zeichnen()
        #pygame.draw.rect(screen, (0,0,255), (x,y,breite,hoehe))#spielfigur
          spieler1.spZeichnen()
          zombie1.zZeichnen()
          zombie1.herzen()
        
          if gewonnen:
             screen.blit(sieger, (0,0))
          elif verloren:
             screen.blit(verlierer, (0,0))
          pygame.display.update()

def kugelhandler():
     global kugeln
     for k in kugeln:
         if k.x >= 0 and k.x <= 1200:
              k.bewegen()
         else:
              kugeln.remove(k)
def Kollision():
     global kugeln, verloren, gewonnen, go
     zombieRechteck = pygame.Rect(zombie1.x+18, zombie1.y+24, zombie1.breite-36, zombie1.hoehe-24)#+18 weil unsichtbarer Bildteil von 18 px
     spielerRechteck =pygame.Rect(spieler1.x+18, spieler1.y+36, spieler1.breite-36, spieler1.hoehe-36)
     
     for k in kugeln:
          kugelRechteck = pygame.Rect(k.x-k.radius, k.y-k.radius, k.radius*2, k.radius*2)
          if zombieRechteck.colliderect(kugelRechteck):
               kugeln.remove(k)
               zombie1.leben -= 1
               if zombie1.leben <= 0 and not verloren:
                    gewonnen = True
                    pygame.mixer.Sound.play(siegSound)
                    screen.blit(sieger,(0,0))
                    go = False
     if zombieRechteck.colliderect(spielerRechteck):
          verloren = True
          gewonnen = False
          pygame.mixer.Sound.play(verlorenSound)
          screen.blit(verlierer,(0,0))
          go = False

linkeWand = pygame.draw.rect(screen, (0,0,0), (0,0,2,600), 0)
rechteWand = pygame.draw.rect(screen, (0,0,0), (1199,0,2,600), 0)
spieler1 = spieler(300,391,4,96,128,-16,[0,0,1,0],0,0)
zombie1 = Zombie(600, 393, 8, 96, 128, [0,0,1,0], 40, 1090)
verloren = False
gewonnen = False
kugeln = []
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

    if gedrueckt[pygame.K_SPACE]:
         if len(kugeln) <= 0 and spieler1.ok:
              kugeln.append(kugel(round(spieler1.x), round(spieler1.y), spieler1.last, 8, (0,0,0),7))
         spieler1.ok = False
    else:
         spieler1.ok = True


    kugelhandler()
    zombie1.hinHer()
    Kollision()
    zeichnen()        
    clock.tick(60)#Anzahl FPS

while True:
     screen.blit(verlierer, (0,0))
     for event in pygame.event.get():
          if event.type == pygame.QUIT: sys.exit()
     zeichnen()
     