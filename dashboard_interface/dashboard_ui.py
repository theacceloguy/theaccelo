import pygame
import random as r
import datetime
import pygame.gfxdraw
import math
import csv

class Charge_Gauge:
    def __init__(self, screen, FONT, x_cord, y_cord, thickness, radius, circle_colour, glow=True):
        self.screen = screen
        self.Font = FONT
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.thickness = thickness
        self.radius = radius
        self.circle_colour = circle_colour
        self.glow = glow

    def draw(self, percent):
        fill_angle = int(percent*270/100)
        per=percent
        if percent > 100:
            percent = 100
        if per <=40:
            per=0
        if per > 100:
            per = 100
        ac = [int(124),int(129),int(246)] 
        for indexi in range(len(ac)):
            if ac[indexi] < 0:
                ac[indexi] = 0
            if ac[indexi] > 255:
                ac[indexi] = 255
        # print(ac)

        # text inside gauge
        pertext = self.Font.render(str(percent) + "%", True, [int(36),int(43),int(71)])
        # Aligning text inbetween gauge
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(pertext, pertext_rect)

        for i in range(0, self.thickness):

            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour)
            if percent >4:
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, ac)

        if percent < 4:
            return

        if self.glow:
            for i in range(0,15):
                ac [3] = int(150 - i*10)
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius + i, -225, fill_angle - 225-8, ac)

            for i in range(0,15):
                ac [3] = int(150 - i*10)
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius -self.thickness - i, -225, fill_angle - 225-8, ac)

            angle_r = math.radians(fill_angle-225-8)
            lx,ly = int((self.radius-self.thickness/2)*math.cos(angle_r)), int( (self.radius-self.thickness/2)*math.sin(angle_r))
            ac[3] = 255
            lx = int(lx+self.x_cord)
            ly = int(ly + self.y_cord)

            pygame.draw.circle(self.screen,ac,(lx,ly),int(self.thickness/2),0)


            for i in range(0,10):
                ac [3] = int(150 - i*15)
                pygame.gfxdraw.arc(screen, int(lx), int(ly), (self.thickness//2)+i , fill_angle -225-10, fill_angle - 225-180-10, ac)

class Speed_Gauge:
    def __init__(self, screen, FONT, x_cord, y_cord, thickness, radius, circle_colour, glow=True):
        self.screen = screen
        self.Font = FONT
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.thickness = thickness
        self.radius = radius
        self.circle_colour = circle_colour
        self.glow = glow

    def draw(self, percent):
        fill_angle = int(percent*270/100)
        per=percent
        if percent > 100:
            percent = 100
        if per <=33:
            per= 0
        if per > 100:
            per = 100
        
        # color of the gauge 
        ac = [int(124),int(129),int(246)]
        for indexi in range(len(ac)):
            if ac[indexi] < 0:
                ac[indexi] = 0
            if ac[indexi] > 255:
                ac[indexi] = 255
        # print(ac)

        # Text inside gauge 
        pertext = self.Font.render(str(percent) + " km/hr", True, [int(36),int(43),int(71)]) 
        # Aligin text inbetween
        pertext_rect = pertext.get_rect(center=(int(self.x_cord), int(self.y_cord)))
        self.screen.blit(pertext, pertext_rect)

        for i in range(0, self.thickness):

            pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, 270 - 225, self.circle_colour)
            if percent >4:
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius - i, -225, fill_angle - 225-8, ac)

        if percent < 4:
            return

        if self.glow:
            for i in range(0,15):
                ac [3] = int(150 - i*10)
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius + i, -225, fill_angle - 225-8, ac)

            for i in range(0,15):
                ac [3] = int(150 - i*10)
                pygame.gfxdraw.arc(screen, int(self.x_cord), int(self.y_cord), self.radius -self.thickness - i, -225, fill_angle - 225-8, ac)

            angle_r = math.radians(fill_angle-225-8)
            lx,ly = int((self.radius-self.thickness/2)*math.cos(angle_r)), int( (self.radius-self.thickness/2)*math.sin(angle_r))
            ac[3] = 255
            lx = int(lx+self.x_cord)
            ly = int(ly + self.y_cord)

            pygame.draw.circle(self.screen,ac,(lx,ly),int(self.thickness/2),0)


            for i in range(0,10):
                ac [3] = int(150 - i*15)
                pygame.gfxdraw.arc(screen, int(lx), int(ly), (self.thickness//2)+i , fill_angle -225-10, fill_angle - 225-180-10, ac)

class Button():
        
        def __init__(self, x , y, image, scale):

            width = image.get_width()
            height = image.get_height() 
            self.image = pygame.transform.scale(image, (int(width * scale),int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x,y)
            self.clicked = False

        def draw(self, surface):

            action = False
            # Get mouse position
            pos = pygame.mouse.get_pos()
            # Check Mouseover and clicked conditions
            if self.rect.collidepoint(pos):

                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # Draw Button
            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1050,750))
clock = pygame.time.Clock()
pygame.display.set_caption('Digital Cluster')
x = datetime.datetime.now()
running = True

while running:

    # initialize font
    myfont = pygame.font.SysFont("consolas", 40) # Speed Guage's Value (90 km)
    myfont1 = pygame.font.SysFont("consolas", 20) # Date, Time
    myfont2 = pygame.font.SysFont("consolas", 45) # Welcome Text
    myfont3 = pygame.font.SysFont("consolas", 35) # Charge Guage's Value (90 %)
    odofont = pygame.font.SysFont("consolas", 25) 
    speed_text_font = pygame.font.SysFont("consolas", 27)
    charge_text_font = pygame.font.SysFont("consolas", 17)
    charger_connected_font = pygame.font.SysFont("consolas",20)
    range_font = pygame.font.SysFont("consolas",16)
    
    # the color of the gauge's rim
    circle_color = (242,245,252)

    # Speed Gauge
    speed_gauge = Speed_Gauge(
        screen = screen,
        FONT = myfont,
        x_cord = 950 / 2,
        y_cord = 1000 / 2,
        thickness = 10,
        radius = 200, 
        circle_colour = circle_color,
        glow = False)
    n = 0
    # Charge Gauge
    charge_gauge = Charge_Gauge(
        screen = screen,
        FONT = myfont3,
        x_cord = 1600 / 2,
        y_cord = 600 / 2,
        thickness = 10,
        radius = 110,
        circle_colour = circle_color,
        glow = False)
    percentage2 = 0

    # Icons 
    img  = pygame.image.load("icons8-maps-50.png").convert_alpha()
    img1 = pygame.image.load("icons8-music-50.png").convert_alpha()
    img2 = pygame.image.load("icons8-phone-50.png").convert_alpha()
    img3 = pygame.image.load("icons8-home-button-50.png").convert_alpha()
    logo = pygame.image.load("accelo_logo1.png").convert_alpha()

    # Icon Buttons 
    map_button = Button(50, 250,img, 1)
    music_button = Button(50, 400,img1, 1)
    phone_button = Button(50, 550,img2, 1)
    switch_button = Button(50, 700,img3, 1)

    while True:

        # opening the CSV file
        with open('TestCSV.csv', mode ='r') as file:
            
            # reading the CSV file
            csvFile = csv.reader(file)
                    
            # displaying the contents of the CSV file
            for rows in csvFile:
                    percentage = int(str(rows[n]))
                    percentage2 = int(str(rows[n]))
                    # n = n+1

        # Background Color 
        screen.fill("#C4D3F2")
        # we define the component after screen.fill, since we add it inside the screen

        # Close screen
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()

        # Time
        time_number = myfont1.render(str(x.strftime("%I:%M %p")), 1, ((36, 43, 71)))
        screen.blit(time_number, (50, 35))

        # Date
        date_number = myfont1.render(x.strftime("%d %B %Y") , 1, ((36, 43, 71)))
        screen.blit(date_number, (50, 60))

        # Welcome Text
        welcome_text = myfont2.render("Welcome, Nitish", 1, ((36, 43, 71)))
        screen.blit(welcome_text, (350, 35))   

        # Drawing the guages
        speed_gauge.draw(percent=percentage)
        charge_gauge.draw(percent=percentage2)

        # Text inside speed-o-meter
        speed_text = speed_text_font.render("SPEED", 1, ((36, 43, 71)))
        screen.blit(speed_text, (432, 425))

        # Text inside charge-o-meter
        charge_text = charge_text_font.render("CHARGE", 1, ((36, 43, 71)))
        screen.blit(charge_text, (773, 250))

        # ODO meter 
        odo_text = odofont.render("ODO :", 1, ((36, 43, 71)))
        screen.blit(odo_text, (390, 650))

        # ODO Number 
        odo_text = odofont.render("827 km", 1, ((36, 43, 71)))
        screen.blit(odo_text, (480, 650))
        
        # Logo
        screen.blit(logo, (750, 600))

        # Button Placement
        # Map Button
        if map_button.draw(screen) == True:
          map_button = Button(75, 250,img, 1.1)
        else:
          map_button = Button(75, 250,img, 1)
        # Music Button
        if music_button.draw(screen)== True:
          music_button = Button(75, 350,img1, 1.1)
        else:
          music_button = Button(75, 350,img1, 1)

        # Phone Button
        if phone_button.draw(screen)== True:
          phone_button = Button(75, 450,img2, 1.1)
        else:
          phone_button = Button(75, 450,img2, 1)

        # Switch Button
        if switch_button.draw(screen)== True:
          
          # Charger Connected Text
          charger_text = charger_connected_font.render("Charger Connected", 1, ((36, 43, 71)))
          screen.blit(charger_text, (750, 425))

          # Switch Button 
          switch_button = Button(75, 550,img3, 1.1)

          # Green Circle   
          pygame.draw.circle(screen, (0,201,195), (730,434), 5)

          # Range   
          Range_remain_text = range_font.render("Fully Charge In:", 1, ((36, 43, 71)))
          screen.blit(Range_remain_text, (750, 455))

          # Range Number
          range_number_text  = range_font.render("35 Mins", 1, ((36, 43, 71)))
          screen.blit(range_number_text , (900, 455))


        else:
          
          # Charger Not Connected Text
          charger_text = charger_connected_font.render("Charger Not Connected", 1, ((36, 43, 71)))
          screen.blit(charger_text, (750, 425))

          # Switch Button 
          switch_button = Button(75, 550,img3, 1)

          # Red Circle  
          pygame.draw.circle(screen, (237,96,102), (730,434), 5)

          # Range   
          Range_remain_text = range_font.render("Charge Remain:", 1, ((36, 43, 71)))
          screen.blit(Range_remain_text, (750, 455))

          # Range Number
          range_number_text = range_font.render("6 hr 44 mins", 1, ((36, 43, 71)))
          screen.blit(range_number_text , (900, 455))


        # updates the entire screen
        pygame.display.update()
        
        # FPS
        clock.tick(60)

pygame.quit()