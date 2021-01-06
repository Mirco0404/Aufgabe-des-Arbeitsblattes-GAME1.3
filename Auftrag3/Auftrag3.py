import pygame                   # Stellt Objekte und Konstanten zur Spielprogrammierung zur Verfügung
import os
import random

#----------------------------------Einstellungen für das Spiel---------------------------------
class Settings(object):
    breite = 1200
    höhe = 700
    fps = 60       
    title = "Auftrag Nr.3" 
    file_path = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(file_path, "images")
    sound_path = os.path.join(file_path, "sound")
    bordersize_ground = 50
    bordersize_edge = 30
    schwierigkeit = float(0.0001)

#--------------------------------Klasse des Spielers--------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, pygame):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.set_mode((Settings.breite, Settings.höhe))
        self.image = pygame.image.load(os.path.join(Settings.images_path, "tile001.png")).convert_alpha()     #Das Image wird in self.image gespeichert
        self.image = pygame.transform.scale(self.image, (70, 85))                                              #Das Image wird gescalet
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.breite // 2                                                               #X-Achsen Position wird auf die Breite des Fensters geteilt durch zwei gesetzt
        self.rect.centery = Settings.höhe - Settings.bordersize_ground                                          #Y-Achsen Position wird auf die Höhe des Fensters minus bordersize_ground gesetzt.
        self.speed = 5
        self.list_counter = 0
        self.move_right = False
        self.move_left = False

#--------------------------------Animation beim Rennen nach Links/Rechts--------------------------------
        self.list_run = []
        self.list_run.append(pygame.image.load(os.path.join(Settings.images_path, "tile003.png")))
        self.list_run.append(pygame.image.load(os.path.join(Settings.images_path, "tile004.png")))
        self.list_run.append(pygame.image.load(os.path.join(Settings.images_path, "tile005.png")))
        
#--------------------------------"Animation" beim stehen--------------------------------
        self.list_stand = []
        self.list_stand.append(pygame.image.load(os.path.join(Settings.images_path, "tile001.png")))

#--------------------------------Animation beim Rennen nach oben--------------------------------
        self.list_run_up = []
        self.list_run_up.append(pygame.image.load(os.path.join(Settings.images_path, "tile009.png")))
        self.list_run_up.append(pygame.image.load(os.path.join(Settings.images_path, "tile010.png")))
        self.list_run_up.append(pygame.image.load(os.path.join(Settings.images_path, "tile011.png")))

#--------------------------------Animation beim Rennen nach unten--------------------------------
        self.list_run_down = []
        self.list_run_down.append(pygame.image.load(os.path.join(Settings.images_path, "tile000.png")))
        self.list_run_down.append(pygame.image.load(os.path.join(Settings.images_path, "tile001.png")))
        self.list_run_down.append(pygame.image.load(os.path.join(Settings.images_path, "tile002.png")))    

#------------------------------------------------------------------------------------------------------

    def update(self):
        keys = pygame.key.get_pressed()                                 #In der Variable "keys" werden die Tasten abgespeichert welche im Spiel betätigt werden

        if keys[pygame.K_RIGHT]:                                        #Wenn rechte Pfeiltaste betätigt wird
            self.rect.x += self.speed

            self.list_counter += 0.2
            if self.list_counter >= len(self.list_run):
                self.list_counter = 0
            self.image = self.list_run[int(self.list_counter)]
            self.image = pygame.transform.flip(self.image, 180, 0)      #Bei flip(1. Was soll geflipt werden, 2. Um wie viel Grad auf der X-Achse, 3. Um wie viel Grad auf der Y-Achse)
            self.image = pygame.transform.scale(self.image, (70, 85)) 

        elif keys[pygame.K_LEFT]:                                       #Wenn linke Pfeiltaste betätigt wird
            self.rect.x -= self.speed

            self.list_counter += 0.2
            if self.list_counter >= len(self.list_run):
                self.list_counter = 0
                
            self.image = self.list_run[int(self.list_counter)]
            self.image = pygame.transform.scale(self.image, (70, 85))

        elif keys[pygame.K_UP]:                                         #Wenn obere Pfeiltaste betätigt wird
            self.rect.y -= self.speed

            self.list_counter += 0.125
            if self.list_counter >= len(self.list_run_up):
                self.list_counter = 0
                
            self.image = self.list_run_up[int(self.list_counter)]
            self.image = pygame.transform.scale(self.image, (70, 85))

        elif keys[pygame.K_DOWN]:                                        #Wenn untere Pfeiltaste betätigt wird
            self.rect.y += self.speed

            self.list_counter += 0.125
            if self.list_counter >= len(self.list_run_down):
                self.list_counter = 0
                
            self.image = self.list_run_down[int(self.list_counter)]
            self.image = pygame.transform.scale(self.image, (70, 85))

        else:
            self.list_counter += 0.05
            if self.list_counter >= len(self.list_stand):
                self.list_counter = 0

            self.image = self.list_stand[int(self.list_counter)]
            self.image = pygame.transform.scale(self.image, (70, 85))
            
            if self.move_right == True:                                 #Die beiden if Abfragen sorgen dafür dass der Spieler nach vorne geneigt wird
                pass

            if self.move_left == True:
                self.image = pygame.transform.flip(self.image, 180, 0)  #Bei flip(1. Was soll geflipt werden, 2. Um wie viel Grad auf der X-Achse, 3. Um wie viel Grad auf der Y-Achse)

#-----------------------------------------------------------------------------------------------
        if self.rect.right >= Settings.breite:
            self.rect.right = Settings.breite

        if self.rect.left <= Settings.breite - Settings.breite:
            self.rect.left = Settings.breite - Settings.breite                  #Die vier if Abfragen setzen die Grenze für rechts,links, oben sowie unten

        if self.rect.top <= Settings.höhe - Settings.höhe:
            self.rect.top = Settings.höhe - Settings.höhe

        if self.rect.bottom >= Settings.höhe:
            self.rect.bottom = Settings.höhe


#--------------------------------Klasse der fallenden Hindernisse--------------------------------
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pygame):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(Settings.images_path, "barrel1.png")).convert_alpha()     #Das Image wird in self.image gespeichert
        self.scale = (random.randrange(55,75), random.randrange(65, 75))                                      #Das Image wird gescalet
        self.image = pygame.transform.scale(self.image, self.scale)                                             
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(Settings.breite - 75)
        self.rect.y = random.randrange(-700, 0)
        self.speed = random.randrange(2,4)
        self.max = 3                                                                                            #Es dürfen zu Anfang maximal drei Hindernisse spawnen
    
    def update(self):
        self.rect.y += self.speed
        Settings.schwierigkeit += 0.0003                                                                        #Der Schwierigkeit wird pro Durchlauf 0.0001 angerechnet

        if self.rect.top >= Settings.höhe + Settings.bordersize_edge:                                           #Sobald ein Hinderniss über den unteren Bildschirmrand hinaus ist, wird es gelöscht, ein neues wird über dem
            self.kill()                                                                                         #   oberen Bildschirmrand erstellt und der Score wird um eins erhöht
            game.all_Obstacle.add(Obstacle(pygame))
            game.score += 1

        if Settings.schwierigkeit >= 1:                                                                         #Sobald die Schwierigkeit eine Ganzzahl von 1 oder größer erreicht, erhöht sich die Geschwindigkeit der
            self.rect.y += int(Settings.schwierigkeit)                                                          #   fallenden Objekte
        print(Settings.schwierigkeit)

        if len(game.all_Obstacle.sprites()) < self.max + int(Settings.schwierigkeit):                           #Pro neuer Ganzzahl (von der Schwierigkeit) wird ein Objekt zur maximalen Anzahl der fallenden Objekte hinzugefügt
            game.all_Obstacle.add(Obstacle(pygame))

#--------------------------------Klasse für die Teleportation [Space]--------------------------------            
class collision_check(pygame.sprite.Sprite):
    def __init__(self, pygame):
        pygame.sprite.Sprite.__init__(self)
        self.screen = pygame.display.set_mode((Settings.breite, Settings.höhe))
        self.image = pygame.image.load(os.path.join(Settings.images_path, "collisionbox.jpg")).convert_alpha()     #Das Image wird in self.image gespeichert (Hier wird einfach ein schwarzes JPG genutzt welches nicht gedrawt wird)
        self.image = pygame.transform.scale(self.image, (65, 850))                                              #Das Image wird gescalet
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(0, 1150)
        self.rect.centery = Settings.höhe - Settings.bordersize_ground

    def check_collision(self):
        self.rect.centery = game.Player.rect.centery                                                    #Der (Ich nenne ihn mal Kollisionskasten) Kollisionskasten erhält die Y-Achsen Werte des Spielers
        self.rect.centerx = random.randrange(50, Settings.breite - 50)                                  #Auf der X-Achse "teleportiert" sich dieser Kasten von 50 bis 1150 Pixel (Bei Tastendruck)
        collision = pygame.sprite.groupcollide(game.all_collisions, game.all_Obstacle, False, False)    #Kollisionsabfrage
        if game.teleport > 0:                                                                           #Die teleport Variable steht auf 10 und sobald diese Funktion in Anspruch genommen wird, wird eine Teleportation abgezogen.
            if bool(collision):                                                                         #Wenn der Teleport-Counter bei 0 ist, kann diese Funktion auch nicht mehr genutzt werden
                self.check_collision()
            elif bool(collision) == False:
                game.Player.rect.centerx = self.rect.centerx
                game.teleport -= 1

#--------------------------------Allgemeine Game-Klasse--------------------------------

class Game(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((Settings.breite, Settings.höhe))
        pygame.display.set_caption(Settings.title)
        self.background = pygame.image.load(os.path.join(Settings.images_path, "background3.jpg")).convert()
        self.background = pygame.transform.scale(self.background, (Settings.breite, Settings.höhe))
        self.background_rect = self.background.get_rect()

        self.score = 0                                      #Score für überwundene Hindernisse
        self.teleport = 10                                  #Score für noch vorhandene Teleportationen

        self.all_Player = pygame.sprite.Group()             #all_Player Gruppe wird erstellt
        self.Player = Player(pygame)                        #Objekt wird erzeugt
        self.all_Player.add(self.Player)                    #Objekt wird der Gruppe hinzugefügt

        self.all_Obstacle = pygame.sprite.Group()           #all_Obstacle Gruppe wird erstellt
        self.all_Obstacle.add(Obstacle(pygame))             #Objekt wird der Gruppe hinzugefügt

        self.collision = collision_check(pygame)            #Objekt wird erzeugt
        self.all_collisions = pygame.sprite.Group()         #all_collisions Gruppe wird erstellt
        self.all_collisions.add(self.collision)             #Objekt wird der Gruppe hinzugefügt
        

#------------------------------Textformatierung für Score und Teleport Anzeige------------------------------
        self.font = pygame.font.SysFont("comicsansms", 50)
        self.text = self.font.render(str(self.score), True, (0, 18, 0))

        self.font2 = pygame.font.SysFont("comicsansms", 50)
        self.text2 = self.font.render("Score: ", True, (0, 18, 0))

        self.font3 = pygame.font.SysFont("comicsansms", 50)
        self.text3 = self.font.render("Score: ", True, (0, 18, 0))

        self.font4 = pygame.font.SysFont("comicsansms", 50)
        self.text4 = self.font.render("Score: ", True, (0, 18, 0))
        


        self.clock = pygame.time.Clock()
        self.done = False

#--------------------------------Sound--------------------------------
        pygame.mixer.music.load(os.path.join(Settings.sound_path, "track_1.mp3"))
        pygame.mixer.music.set_volume(.2)
        pygame.mixer.music.play(loops=-1)
        self.music_state = True
#---------------------------------------------------------------------

    def run(self):
        while not self.done:             # Hauptprogrammschleife mit Abbruchkriterium   
            self.clock.tick(Settings.fps)          # Setzt die Taktrate auf max 60fps   
            for event in pygame.event.get():    # Durchwandere alle aufgetretenen  Ereignisse
                if event.type == pygame.QUIT:   # Wenn das rechts obere X im Fenster geklicktr
                    self.done = True    
                elif event.type == pygame.KEYDOWN:              #Event wird abgefragt, d.h. sobald "ESC" betätigt wird, schließt sich das Fenster.
                    if event.key == pygame.K_ESCAPE:
                        self.done = True
                elif event.type == pygame.KEYUP:                #Wenn Leertaste gedrückt wird, wird die check_collisions Funktion von der Klasse collision_check ausgeführt
                    if event.key == pygame.K_SPACE:
                        self.collision.check_collision()


                    
            collision = pygame.sprite.groupcollide(self.all_Player, self.all_Obstacle, False, True, collided=pygame.sprite.collide_rect_ratio(.88))     #Schaut ob Spieler und Hindernisse kollidieren
            if bool(collision) == True:
                self.done = True
            
            self.screen.blit(self.background, self.background_rect)

            self.all_Player.draw(self.screen)                   #Zeichnet den Spieler
            self.all_Player.update()                            #Ruft die update Funktion der Player-Klasse auf
            
            self.all_Obstacle.draw(self.screen)                 #Zeichnet alle fallenden Objekte
            self.all_Obstacle.update()                          #Ruft die update Funktion der Obstacle-Klasse auf

#--------------------------Scoranzeige--------------------------
            self.text = self.font.render(str(self.score), True, (0, 18, 0))                 #Position der Score Zahl wird bestimmt
            self.screen.blit(self.text,
            (220 - self.text.get_width() // 2, 50 - self.text.get_height() // 2))           #Score Zahl wird geblitet

            self.text2 = self.font.render(("Score: "), True, (0, 18, 0))                    #Position des Score Schriftzuges
            self.screen.blit(self.text2,
            (100 - self.text2.get_width() // 2, 50 - self.text2.get_height() // 2))         #Score Schriftzug wird geblitet

#--------------------------Teleportanzeige--------------------------
            self.text3 = self.font.render(str(self.teleport), True, (0, 18, 0))             #Position der Teleport Zahl wird bestimmt
            self.screen.blit(self.text3,
            (Settings.breite - self.text3.get_width() - 25 , 50 - self.text3.get_height() // 2))  #Teleport Zahl wird geblitet

            self.text4 = self.font.render(("Teleports: "), True, (0, 18, 0))                    #Position des Teleport Schriftzuges
            self.screen.blit(self.text4,
            (Settings.breite - self.text4.get_width() - 80, 50 - self.text4.get_height() // 2)) #Score Schriftzug wird geblitet
            
            pygame.display.flip()   # Aktualisiert das Fenster

        
        


if __name__ == '__main__':      # 
                                    
    pygame.init()               # Bereitet die Module zur Verwendung vor  
    game = Game()
    game.run()
  
    pygame.quit()               # beendet pygame