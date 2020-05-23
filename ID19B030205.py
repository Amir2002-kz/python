import pika
import sys
import json
import time
import uuid
from threading import Thread
import pygame
import random
screen= pygame.display.set_mode((1000,700))
pygame.init()
clock=pygame.time.Clock()
done = True
secund=0
FPS= 60
class MainMenu(object):
    def __init__(self,screen):
        self.x1=self.x2=self.x3=self.x4=self.x5=self.a=self.b=self.c=self.a1=self.b1=self.c1=self.a2=self.b2=self.c2=0
        self.screen=screen
        self.Sp=pygame.Rect(350,290,300,30)
        self.Spfon=pygame.Rect(348,288,304,34)
        self.Mp=pygame.Rect(350,330,300,30)
        self.Mpfon=pygame.Rect(348,328,304,34)
        self.MpAI=pygame.Rect(350,370,300,30)
        self.MpAIfon=pygame.Rect(348,368,304,34)
        self.Op=pygame.Rect(350,430,145,30)
        self.Opfon=pygame.Rect(348,428,149,34)
        self.Qu=pygame.Rect(505,430,145,30)
        self.Qufon=pygame.Rect(503,428,149,34)
        self.mish=(0,0,0,0)
        self.battle=pygame.Rect(140,53,298,61)
        self.of=pygame.Rect(463,53,96,61)
        self.tanks=pygame.Rect(600,53,254,61)
    def color(self,x1,y1):
        self.mish=(x1,y1,2,2)
        if self.Sp.colliderect(self.mish):
            self.x1=255
        elif not self.Sp.colliderect(self.mish):
            self.x1=0

        if self.Mp.colliderect(self.mish):
            self.x2=255
        elif not self.Mp.colliderect(self.mish):
            self.x2=0

        if self.MpAI.colliderect(self.mish):
            self.x3=255
        elif not self.MpAI.colliderect(self.mish):
            self.x3=0

        if self.Op.colliderect(self.mish):
            self.x4=255
        elif not self.Op.colliderect(self.mish):
            self.x4=0

        if self.Qu.colliderect(self.mish):
            self.x5=255
        elif not self.Qu.colliderect(self.mish):
            self.x5=0
        
        if self.battle.colliderect(self.mish):
            self.a=139
            self.b=90
            self.c=43
        elif not self.battle.colliderect(self.mish):
            self.a=self.b=self.c=0

        if self.of.colliderect(self.mish):
            self.a1=139
            self.b1=90
            self.c1=43
        elif not self.of.colliderect(self.mish):
            self.a1=self.b1=self.c1=0
        
        if self.tanks.colliderect(self.mish):
            self.a2=139
            self.b2=90
            self.c2=43
        elif not self.tanks.colliderect(self.mish):
            self.a2=self.b2=self.c2=0
    def draw(self):
        pygame.draw.rect(self.screen,(0,0,0),self.Spfon)
        pygame.draw.rect(self.screen,(128,128,128),self.Sp)
        f1 = pygame.font.SysFont('calibri', 25)
        text1 = f1.render('SinglePlayer', 1, (self.x1, 0, 0))
        self.screen.blit(text1, (430, 293))
        self.screen.blit(text1, (431, 293))
        

        pygame.draw.rect(self.screen,(0,0,0),self.Mpfon)
        pygame.draw.rect(self.screen,(128,128,128),self.Mp)
        f2 = pygame.font.SysFont('calibri', 25)
        text2 = f2.render('MultiPlayer', 1, (self.x2, 0, 0))
        self.screen.blit(text2, (435, 333))
        self.screen.blit(text2, (434, 333))
        

        pygame.draw.rect(self.screen,(0,0,0),self.MpAIfon)
        pygame.draw.rect(self.screen,(128,128,128),self.MpAI)
        f3 = pygame.font.SysFont('calibri', 25)
        text3 = f3.render('MultiPlayer AI', 1, (self.x3, 0, 0))
        self.screen.blit(text3, (425, 373))
        self.screen.blit(text3, (424, 373))
        

        pygame.draw.rect(self.screen,(0,0,0),self.Opfon)
        pygame.draw.rect(self.screen,(128,128,128),self.Op)
        f4 = pygame.font.SysFont('calibri', 25)
        text4 = f4.render('Options...', 1, (self.x4, 0, 0))
        self.screen.blit(text4, (380, 433))
        self.screen.blit(text4, (379, 433))
        

        pygame.draw.rect(self.screen,(0,0,0),self.Qufon)
        pygame.draw.rect(self.screen,(128,128,128),self.Qu)
        f5 = pygame.font.SysFont('calibri', 25)
        text5 = f5.render('Quit Game', 1, (self.x5, 0, 0))
        self.screen.blit(text5, (525, 433))
        self.screen.blit(text5, (524, 433))
        

        f6 = pygame.font.SysFont('blackadderitc', 35)
        text6 = f6.render('Battle of Tanks 1.8.9', 1, (0,0,0))
        self.screen.blit(text6, (1, 663))

        f7 = pygame.font.SysFont('blackadderitc', 35)
        text7 = f7.render('Do not distribute!!!', 1, (0,0,0))
        self.screen.blit(text7, (757, 663))

        f8 = pygame.font.SysFont('snapitc', 80)
        text8 = f8.render('Battle ', 1000, (self.a,self.b,self.c))
        self.screen.blit(text8, (140, 30))

        f9 = pygame.font.SysFont('snapitc', 80)
        text9= f9.render('of ', 1000, (self.a1,self.b1,self.c1))
        self.screen.blit(text9, (462, 30))

        f10 = pygame.font.SysFont('snapitc', 80)
        text10 = f10.render('tanks', 1000, (self.a2,self.b2,self.c2))
        self.screen.blit(text10, (600, 30))

    def perehod(self,x1,y1):
        global MM
        if self.Sp.colliderect(self.mish):
            global SP
            SP=True
            MM=False
        if self.Mp.colliderect(self.mish):
            global MP
            MP = True
            MM = False
        if self.MpAI.colliderect(self.mish):
            global MPAI
            MPAI = True
            MM = False
        if self.Op.colliderect(self.mish):
            global OP
            OP = True
            MM = False
        if self.Qu.colliderect(self.mish):
            global QU
            QU = True
            MM = False
            
class single(object):
    def __init__(self,screen):
        self.Next=False
        self.FPS=60
        self.secund=0
        self.ms=0
        self.Back=False
        self.screen=screen
        self.SINgle=pygame.Rect(180,165,283,74)
        self.player=pygame.Rect(502,165,283,74)
        self.mish=pygame.Rect(0,0,0,0)
        self.x1=self.x2=self.a1=self.b1=self.c1=self.a2=self.b2=self.c2=0
        self.nextfon=pygame.Rect(796,646,204,54)
        self.next=pygame.Rect(798,648,200,50)
        self.backfon=pygame.Rect(0,646,204,54)
        self.back=pygame.Rect(2,648,200,50)
    def color(self,x1,y1):
        self.mish=pygame.Rect(x1,y1,2,2)
        if self.next.colliderect(self.mish):
            self.x2=255
        elif not self.next.colliderect(self.mish):
            self.x2=0
        
        if self.back.colliderect(self.mish):
            self.x1=255
        elif not self.back.colliderect(self.mish):
            self.x1=0
        
        if self.SINgle.colliderect(self.mish):
            self.a1=139
            self.b1=90
            self.c1=43
        elif not self.SINgle.colliderect(self.mish):
            self.a1=self.b1=self.c1=0
        
        if self.player.colliderect(self.mish):
            self.a2=139
            self.b2=90
            self.c2=43
        elif not self.player.colliderect(self.mish):
            self.a2=self.b2=self.c2=0

    def draw(self,singfon):
        clock=pygame.time.Clock()
        self.ms=clock.tick(self.FPS)
        self.secund+=self.ms/1000
        self.screen.blit(singfon,(0,0))

        f8 = pygame.font.SysFont('snapitc', 80)
        text8 = f8.render('Single ', 1000, (self.a1,self.b1,self.c1))
        screen.blit(text8, (180, 140))
        f88 = pygame.font.SysFont('snapitc', 80)
        text88 = f88.render('player', 1000, (self.a2,self.b2,self.c2))
        screen.blit(text88, (502, 140))

        pygame.draw.rect(self.screen,(0,0,0), self.backfon)
        pygame.draw.rect(self.screen,(128,128,128), self.back)
        f1 = pygame.font.SysFont('calibri', 20)
        text1 = f1.render('Back to Main-Menu', 1000, (self.x1,0,0))
        screen.blit(text1, (20, 665))
        screen.blit(text1, (19, 665))
        
        pygame.draw.rect(self.screen,(0,0,0), self.nextfon)
        pygame.draw.rect(self.screen,(128,128,128), self.next)
        f3 = pygame.font.SysFont('calibri', 20)
        text3 = f3.render('Play Single-Player', 1000, (self.x2,0,0))
        screen.blit(text3, (826, 665))
        screen.blit(text3, (825, 665))
        
        f6 = pygame.font.SysFont('blackadderitc', 35)
        text6 = f6.render('Almabekov Amir', 1, (0,0,0))
        screen.blit(text6, (1, 1))
        
    def perehod (self,x1,y1):
        self.nazhatie=pygame.Rect(x1,y1,2,2) 
        global SP 
        global SPGAME
        global MM
        if  self.next.colliderect(self.nazhatie):
            SPGAME=True
            SP = False
        if self.back.colliderect(self.nazhatie):
            SP = False
            MM= True
class Tank(object):
    def __init__(self,screen):
        self.x=50
        self.y=650
        self.x1=200
        self.y1=650
        self.screen=screen
        self.Hp1=self.Hp2=3
        self.speed1=0
        self.speed2=0
        self.up=self.down=self.right=self.left=False
        self.a=self.b=self.c=self.d=self.a1=self.b1=self.c1=self.d1=0
        self.s=0
        self.double=False
        self.first=False
        self.second=False
    def direction(self,direction1,number):
    
        if number ==1:
            if direction1== "up":
                self.up=True
                self.right=self.down=self.left=False
                self.a=self.x+17
                self.b=self.y-20
                self.c=6
                self.d=20
            elif direction1=="down":
                self.down=True
                self.right=self.up=self.left=False
                self.a=self.x+17
                self.b=self.y+40
                self.c=6
                self.d=20

            elif direction1 == "right":
                self.right=True
                self.up=self.down=self.left=False
                self.a=self.x+40
                self.b=self.y+17
                self.c=20
                self.d=6

            elif direction1=="left":
                self.left=True
                self.right=self.down=self.up=False
                self.a=self.x-20
                self.b=self.y+17
                self.c=20
                self.d=6
        else:
            if direction1== "up":
                self.up=True
                self.right=self.down=self.left=False
                self.a1=self.x1+17
                self.b1=self.y1-20
                self.c1=6
                self.d1=20
            elif direction1=="down":
                self.down=True
                self.right=self.up=self.left=False
                self.a1=self.x1+17
                self.b1=self.y1+40
                self.c1=6
                self.d1=20

            elif direction1 == "right":
                self.right=True
                self.up=self.down=self.left=False
                self.a1=self.x1+40
                self.b1=self.y1+17
                self.c1=20
                self.d1=6

            elif direction1=="left":
                self.left=True
                self.right=self.down=self.up=False
                self.a1=self.x1-20
                self.b1=self.y1+17
                self.c1=20
                self.d1=6
        
    def move(self,number,s):
        if not self.double:
            self.s=s*150
            self.speed1=self.s
            self.speed2=self.s
        if self.double and self.first:
            self.s=s*300
            self.speed1=self.s
        if self.double and self.second:
            self.s=s*300
            self.speed2=self.s
        if number ==1:
            if self.up:
                self.y-=self.speed1
                self.b-=self.speed1
            if self.down:
                self.y+=self.speed1
                self.b+=self.speed1
            if self.right:
                self.x+=self.speed1
                self.a+=self.speed1
            if self.left:
                self.x-=self.speed1
                self.a-=self.speed1
        else:
            if self.up:
                self.y1-=self.speed2
                self.b1-=self.speed2
            if self.down:
                self.y1+=self.speed2
                self.b1+=self.speed2
            if self.right:
                self.x1+=self.speed2
                self.a1+=self.speed2
            if self.left:
                self.x1-=self.speed2
                self.a1-=self.speed2
    def infinitepole(self,number):
        if number == 1:
            if self.x > 1040:
                self.x = -40
            elif self.x < -40:
                self.x = 1040
            elif self.y> 740:
                self.y = -40
            elif self.y< -40:
                self.y = 740
        else:
            if self.x1 > 1040:
                self.x1 = -40
            elif self.x1 < -40:
                self.x1 = 1040
            elif self.y1> 740:
                self.y1 = -40
            elif self.y1< -40:
                self.y1 = 740
    def HP1(self):
        return self.Hp1
    def HP2(self):
        return self.Hp2
    def draw(self,number):
        if number ==1:
            pygame.draw.rect(self.screen,(0,0,0),(self.x,self.y,40,40))
            pygame.draw.rect(self.screen,(0,0,0),(self.a,self.b,self.c,self.d))
        else:
            pygame.draw.rect(self.screen,(255,0,0),(self.x1,self.y1,40,40))
            pygame.draw.rect(self.screen,(255,0,0),(self.a1,self.b1,self.c1,self.d1))
    def restart(self,number):
        global direction1
        global direction2
        if number==1:
            self.Hp1=3
            direction1="up"
            self.x=50
            self.y=650
            self.speed1=self.s
            bullet.speed1=10
        else:
            self.Hp2=3
            direction2="right"
            self.x1=200
            self.y1=650
            self.speed2=self.s
            bullet.speed2=10
        
            

class Bullet (object):
    def __init__(self,screen):
        self.x=self.y=self.x1=self.y1=0
        self.up1 = self.down1=self.right1=self.left1=self.up2=self.down2=self.right2=self.left2=self.shooting1=self.shooting2=False
        self.screen = screen
        self.speed1 = 10
        self.speed2=10
        self.tank1=self.bullet1=self.tank2=self.bullet2=pygame.Rect(0,0,0,0)
        self.double=self.first=self.second=False
    def shoot1(self,direction,x,y):
        self.x = x
        self.y = y
        self.bullet1=pygame.Rect(self.x,self.y,10,10)
        self.shooting1 = True
        if direction == "up" :
            self.bullet1.right+=16
            self.up1 = True
            self.down1=self.right1=self.left1=False

        elif direction == "down":
            self.bullet1.right +=16
            self.bullet1.top += 40
            self.down1 = True
            self.up1=self.right1=self.left1=False
        elif direction == "left":
            self.bullet1.top += 16
            self.left1 = True
            self.down1=self.right1=self.up1=False
        elif direction == "right":
            self.bullet1.top += 16
            self.bullet1.right += 40
            self.right1 = True
            self.down1=self.up1=self.left1=False
    def move1(self,d,f,s):
        if not self.double:
            self.speed1=s*230
        elif self.double and self.first:
            self.speed1=s*460
        self.d=d
        self.f=f
        self.tank2=pygame.Rect(self.d,self.f,40,40)
        if self.up1:
            if self.bullet1.colliderect(self.tank2) :
                player.Hp2-=1
                self.bullet1.top=self.bullet1.left=-100
                self.shooting1=False
           
            self.bullet1.top -= self.speed1
            if self.bullet1.top<0:
                self.shooting1=False
        elif self.down1:
            if self.bullet1.colliderect(self.tank2) :
                player.Hp2-=1
                self.bullet1.top=self.bullet1.left=-100
                self.shooting1=False
            
            self.bullet1.bottom += self.speed1
            if self.bullet1.bottom>600:
                self.shooting1=False
        elif self.left1:
            if self.bullet1.colliderect(self.tank2):
                player.Hp2-=1
                self.bullet1.top=self.bullet1.left=-100
                self.shooting1=False
            
            self.bullet1.left -= self.speed1
            if self.bullet1.left<0:
                self.shooting1=False
        elif self.right1:
            if self.bullet1.colliderect(self.tank2) :
                player.Hp2-=1
                self.bullet1.top=self.bullet1.left=-100            
                self.shooting1=False
            self.bullet1.right += self.speed1
            if self.bullet1.right>1000:
                self.shooting1=False
    def draw1(self):
        pygame.draw.rect(self.screen, (0,0,0), self.bullet1)

    def shoot2(self,direction,x,y):
        self.x1 = x
        self.y1 = y
        self.bullet2=pygame.Rect(self.x1,self.y1,10,10)
        self.shooting2 = True
        if direction == "up" :
            self.bullet2.right+=16
            self.up2 = True
            self.down2=self.right2=self.left2=False
        elif direction == "down":
            self.bullet2.right +=16
            self.bullet2.top += 40
            self.up2 =self.right2= self.left2=False
            self.down2=True 
        elif direction == "left":
            self.bullet2.top += 16
            self.up2 =self.down2= self.right2=False
            self.left2=True
        elif direction == "right":
            self.bullet2.top += 16
            self.bullet2.right += 40
            self.up2 =self.left2=self.down2= False
            self.right2=True
            
    def move2(self,d,f,s):
        if not self.double:
            self.speed2=s*230
        elif self.double and self.second:
            self.speed2=s*460
        self.d=d
        self.f=f
        self.tank1=pygame.Rect(self.d,self.f,40,40)
        if self.up2:
            if self.bullet2.colliderect(self.tank1) :
                player.Hp1-=1
                self.bullet2.top=self.bullet2.left=-100
                self.shooting2=False
           
            self.bullet2.top -= self.speed2
            if self.bullet2.top<0:
                self.shooting2=False
        elif self.down2:
            if self.bullet2.colliderect(self.tank1) :
                player.Hp1-=1
                self.bullet2.top=self.bullet2.left=-100
                self.shooting2=False
            
            self.bullet2.bottom += self.speed2
            if self.bullet2.bottom>600:
                self.shooting2=False
        elif self.left2:
            if self.bullet2.colliderect(self.tank1):
                player.Hp1-=1
                self.bullet2.top=self.bullet2.left=-100
                self.shooting2=False
            
            self.bullet2.left -= self.speed2
            if self.bullet2.left<0:
                self.shooting2=False
        elif self.right2:
            if self.bullet2.colliderect(self.tank1) :
                player.Hp1-=1
                self.bullet2.top=self.bullet2.left=-100
                self.shooting2=False
            self.bullet2.right += self.speed2
            if self.bullet2.right>1000:
                self.shooting2=False
    def draw2(self):
        pygame.draw.rect(self.screen, (0,0,0), self.bullet2)

class Options(object):
    def __init__(self,screen):
        self.screen=screen
        self.a=191
        self.b=62
        self.c=255
        self.svetliifon=pygame.Rect(9,278,124,64)
        self.svetlii=pygame.Rect(11,280,120,60)

        self.aquamarinefon=pygame.Rect(295,278,124,64)
        self.aquamarine=pygame.Rect(297,280,120,60)

        self.greenablefon=pygame.Rect(581,278,124,64)
        self.greenable=pygame.Rect(583,280,120,60)

        self.blackablefon=pygame.Rect(867,278,124,64)
        self.blackable=pygame.Rect(869,280,120,60)

        self.warfon=pygame.Rect(8,458,144,64)
        self.war=pygame.Rect(10,460,140,60)

        self.winfon=pygame.Rect(418,458,144,64)
        self.win=pygame.Rect(420,460,140,60)

        self.shotfon=pygame.Rect(848,458,144,64)
        self.shot=pygame.Rect(850,460,140,60)

        self.war16fon=pygame.Rect(8,538,144,24)
        self.war16=pygame.Rect(10,540,140,20)
        self.war24fon=pygame.Rect(8,573,144,24)
        self.war24=pygame.Rect(10,575,140,20)
        self.war32fon=pygame.Rect(8,608,144,24)
        self.war32=pygame.Rect(10,610,140,20)
        
        self.win16fon=pygame.Rect(418,538,144,24)
        self.win16=pygame.Rect(420,540,140,20)
        self.win24fon=pygame.Rect(418,573,144,24)
        self.win24=pygame.Rect(420,575,140,20)
        self.win32fon=pygame.Rect(418,608,144,24)
        self.win32=pygame.Rect(420,610,140,20)

        self.shot16fon=pygame.Rect(848,538,144,24)
        self.shot16=pygame.Rect(850,540,140,20)
        self.shot24fon=pygame.Rect(848,573,144,24)
        self.shot24=pygame.Rect(850,575,140,20)
        self.shot32fon=pygame.Rect(848,608,144,24)
        self.shot32=pygame.Rect(850,610,140,20)

        self.backfon=pygame.Rect(0,646,204,54)
        self.back=pygame.Rect(2,648,200,50)

        self.warfon1=self.warfon2=self.warfon3=self.warfon4=128
        self.warnad1=self.warnad2=self.warnad3=self.warnad4=0
        self.winfon1=self.winfon2=self.winfon3=self.winfon4=128
        self.winnad1=self.winnad2=self.winnad3=self.winnad4=0
        self.shotfon1=self.shotfon2=self.shotfon3=self.shotfon4=128
        self.shotnad1=self.shotnad2=self.shotnad3=self.shotnad4=0

        self.backnad=self.vol1=self.vol2=self.vol3=1

        self.x=210
        self.y=180
        self.z=140
    def color(self,x1,y1):
        self.mish=pygame.Rect(x1,y1,2,2)
        if self.mish.colliderect(self.win):
            self.winfon1=0
            self.winnad1=255
        if not self.mish.colliderect(self.win):
            self.winfon1=128
            self.winnad1=0
        
        if self.mish.colliderect(self.win16):
            self.winfon2=0
            self.winnad2=255
        if not self.mish.colliderect(self.win16):
            self.winfon2=128
            self.winnad2=0
        
        if self.mish.colliderect(self.win24):
            self.winfon3=0
            self.winnad3=255
        if not self.mish.colliderect(self.win24):
            self.winfon3=128
            self.winnad3=0

        if self.mish.colliderect(self.win32):
            self.winfon4=0
            self.winnad4=255
        if not self.mish.colliderect(self.win32):
            self.winfon4=128
            self.winnad4=0
        #------------------------------------
        if self.mish.colliderect(self.war):
            self.warfon1=0
            self.warnad1=255
        if not self.mish.colliderect(self.war):
            self.warfon1=128
            self.warnad1=0
        
        if self.mish.colliderect(self.war16):
            self.warfon2=0
            self.warnad2=255
        if not self.mish.colliderect(self.war16):
            self.warfon2=128
            self.warnad2=0
        
        if self.mish.colliderect(self.war24):
            self.warfon3=0
            self.warnad3=255
        if not self.mish.colliderect(self.war24):
            self.warfon3=128
            self.warnad3=0

        if self.mish.colliderect(self.war32):
            self.warfon4=0
            self.warnad4=255
        if not self.mish.colliderect(self.war32):
            self.warfon4=128
            self.warnad4=0
        #------------------------------------

        if self.mish.colliderect(self.shot):
            self.shotfon1=0
            self.shotnad1=255
        if not self.mish.colliderect(self.shot):
            self.shotfon1=128
            self.shotnad1=0
        
        if self.mish.colliderect(self.shot16):
            self.shotfon2=0
            self.shotnad2=255
        if not self.mish.colliderect(self.shot16):
            self.shotfon2=128
            self.shotnad2=0
        
        if self.mish.colliderect(self.shot24):
            self.shotfon3=0
            self.shotnad3=255
        if not self.mish.colliderect(self.shot24):
            self.shotfon3=128
            self.shotnad3=0

        if self.mish.colliderect(self.shot32):
            self.shotfon4=0
            self.shotnad4=255
        if not self.mish.colliderect(self.shot32):
            self.shotfon4=128
            self.shotnad4=0
        #----------------------------------------
        if self.mish.colliderect(self.back):
            self.backnad=255
        if not self.mish.colliderect(self.back):
            self.backnad=0
    def perehod(self,x1,y1):
        self.nazhatie=pygame.Rect(x1,y1,2,2) 
        global MM
        global OP
        if self.nazhatie.colliderect(self.back):
            OP = False
            MM = True
    def press(self,x1,y1,war,win,vistrel,vol2,vol3):
        self.nazhatie=pygame.Rect(x1,y1,2,2) 
        if self.nazhatie.colliderect(self.win):
            win.play()
            win.set_volume(1/vol2)
        if self.nazhatie.colliderect(self.shot):
            vistrel.play()
            vistrel.set_volume(1/vol3)
        if self.nazhatie.colliderect(self.war16):
            self.vol1=2
        if self.nazhatie.colliderect(self.war24):
            self.vol1=4
        if self.nazhatie.colliderect(self.war32):
            self.vol1=8
        
        if self.nazhatie.colliderect(self.win16):
            self.vol2=2
        if self.nazhatie.colliderect(self.win24):
            self.vol2=4
        if self.nazhatie.colliderect(self.win32):
            self.vol2=8

        if self.nazhatie.colliderect(self.shot16):
            self.vol3=2
        if self.nazhatie.colliderect(self.shot24):
            self.vol3=4
        if self.nazhatie.colliderect(self.shot32):
            self.vol3=8

        if self.nazhatie.colliderect(self.svetlii):
            self.x=210
            self.y=180
            self.z=140
        if self.nazhatie.colliderect(self.aquamarine):
            self.x=102
            self.y=205
            self.z=170
        if self.nazhatie.colliderect(self.greenable):
            self.x=118
            self.y=238
            self.z=0
        if self.nazhatie.colliderect(self.blackable):
            self.x=128
            self.y=138
            self.z=135
    def pressreturn(self):
        return self.vol1,self.vol2,self.vol3
    def pressreturn2(self):
        return self.x,self.y,self.z
    def draw(self):
        screen.fill((191,62,255))
        f1 = pygame.font.SysFont('snapitc', 80)
        text1 = f1.render('Options...', 10, (0, 0, 0))
        self.screen.blit(text1, (250,80))

        f6 = pygame.font.SysFont('blackadderitc', 35)
        text6 = f6.render('Almabekov Amir', 1, (0,0,0))
        self.screen.blit(text6, (1, 1))

        f6 = pygame.font.SysFont('calibri', 40)
        text6 = f6.render('Game background (Choose one)', 1, (0,0,0))
        self.screen.blit(text6, (220,220))
        self.screen.blit(text6, (219,220))
        self.screen.blit(text6, (218,220))
        

        pygame.draw.rect(self.screen,(0,0,0),self.svetliifon)
        pygame.draw.rect(self.screen,(210,180,140),self.svetlii)

        pygame.draw.rect(self.screen,(0,0,0),self.aquamarinefon)
        pygame.draw.rect(self.screen,(102,205,170),self.aquamarine)

        pygame.draw.rect(self.screen,(0,0,0),self.greenablefon)
        pygame.draw.rect(self.screen,(118,238,0),self.greenable)

        pygame.draw.rect(self.screen,(0,0,0),self.blackablefon)
        pygame.draw.rect(self.screen,(85,107,47),self.blackable)

        f6 = pygame.font.SysFont('calibri', 40)
        text6 = f6.render('Audio effects(adjust the volume)', 1, (0,0,0))
        self.screen.blit(text6, (220,400))
        self.screen.blit(text6, (219,400))
        self.screen.blit(text6, (218,400))
        
        pygame.draw.rect(self.screen,(0,0,0),self.warfon)
        pygame.draw.rect(self.screen,(self.warfon1,self.warfon1,self.warfon1),self.war)
        f6 = pygame.font.SysFont('calibri', 25)
        text6 = f6.render('Fon music', 1, (self.warnad1,0,0))
        self.screen.blit(text6, (26,480))
        self.screen.blit(text6, (27,480))
        f6 = pygame.font.SysFont('calibri', 15)
        text6 = f6.render('(now playing)', 1, (self.warnad1,0,0))
        self.screen.blit(text6, (34,503))
        self.screen.blit(text6, (35,503))

        pygame.draw.rect(self.screen,(0,0,0),self.war16fon)
        pygame.draw.rect(self.screen,(self.warfon2,self.warfon2,self.warfon2),self.war16)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 2', 1, (self.warnad2,0,0))
        self.screen.blit(text6, (18,543))
        self.screen.blit(text6, (17,543))

        pygame.draw.rect(self.screen,(0,0,0),self.war24fon)
        pygame.draw.rect(self.screen,(self.warfon3,self.warfon3,self.warfon3),self.war24)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 4', 1, (self.warnad3,0,0))
        self.screen.blit(text6, (18,578))
        self.screen.blit(text6, (17,578))

        pygame.draw.rect(self.screen,(0,0,0),self.war32fon)
        pygame.draw.rect(self.screen,(self.warfon4,self.warfon4,self.warfon4),self.war32)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 8', 1, (self.warnad4,0,0))
        self.screen.blit(text6, (18,613))
        self.screen.blit(text6, (17,613))
        #----------------------------------------------------
        pygame.draw.rect(self.screen,(0,0,0),self.winfon)
        pygame.draw.rect(self.screen,(self.winfon1,self.winfon1,self.winfon1),self.win)
        f6 = pygame.font.SysFont('calibri', 25)
        text6 = f6.render('Win effect', 1, (self.winnad1,0,0))
        self.screen.blit(text6, (438,480))
        self.screen.blit(text6, (437,480))

        pygame.draw.rect(self.screen,(0,0,0),self.win16fon)
        pygame.draw.rect(self.screen,(self.winfon2,self.winfon2,self.winfon2),self.win16)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 2', 1, (self.winnad2,0,0))
        self.screen.blit(text6, (428,543))
        self.screen.blit(text6, (427,543))

        pygame.draw.rect(self.screen,(0,0,0),self.win24fon)
        pygame.draw.rect(self.screen,(self.winfon3,self.winfon3,self.winfon3),self.win24)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 4', 1, (self.winnad3,0,0))
        self.screen.blit(text6, (428,578))
        self.screen.blit(text6, (427,578))

        pygame.draw.rect(self.screen,(0,0,0),self.win32fon)
        pygame.draw.rect(self.screen,(self.winfon4,self.winfon4,self.winfon4),self.win32)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 8', 1, (self.winnad4,0,0))
        self.screen.blit(text6, (428,613))
        self.screen.blit(text6, (427,613))
        #----------------------------------------------------
        pygame.draw.rect(self.screen,(0,0,0),self.shotfon)
        pygame.draw.rect(self.screen,(self.shotfon1,self.shotfon1,self.shotfon1),self.shot)
        f6 = pygame.font.SysFont('calibri', 25)
        text6 = f6.render('Shot effect', 1, (self.shotnad1,0,0))
        self.screen.blit(text6, (865,480))
        self.screen.blit(text6, (866,480))

        pygame.draw.rect(self.screen,(0,0,0),self.shot16fon)
        pygame.draw.rect(self.screen,(self.shotfon2,self.shotfon2,self.shotfon2),self.shot16)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 2', 1, (self.shotnad2,0,0))
        self.screen.blit(text6, (853,543))
        self.screen.blit(text6, (854,543))

        pygame.draw.rect(screen,(0,0,0),self.shot24fon)
        pygame.draw.rect(screen,(self.shotfon3,self.shotfon3,self.shotfon3),self.shot24)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 4', 1, (self.shotnad3,0,0))
        screen.blit(text6, (853,578))
        screen.blit(text6, (854,578))

        pygame.draw.rect(self.screen,(0,0,0),self.shot32fon)
        pygame.draw.rect(self.screen,(self.shotfon4,self.shotfon4,self.shotfon4),self.shot32)
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render('Reduce vol. by 8', 1, (self.shotnad4,0,0))
        self.screen.blit(text6, (853,613))
        self.screen.blit(text6, (854,613))

        #----------------------------------------------------
        pygame.draw.rect(self.screen,(0,0,0),self.backfon)
        pygame.draw.rect(self.screen,(128,128,128),self.back)

        f1 = pygame.font.SysFont('calibri', 20)
        text1 = f1.render('Back to Main-Menu', 1000, (self.backnad,0,0))
        self.screen.blit(text1, (20, 665))
        self.screen.blit(text1, (19, 665))

MG=True
server=3
def main():
    TANK=pygame.image.load("img\\tank.png")

    class TankRpcClient():
        def __init__(self):
            self.connection = pika.BlockingConnection(pika.ConnectionParameters('34.254.177.17',5672,'dar-tanks',pika.PlainCredentials('dar-tanks','5orPLExUYnyVYZg48caMpX')))
            self.channel=self.connection.channel()
            queue=self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)
            self.callback_queue=queue.method.queue
            self.channel.queue_bind(exchange='X:routing.topic',queue=self.callback_queue)
            self.channel.basic_consume(queue=self.callback_queue,on_message_callback=self.on_response,auto_ack=True)
            self.response=self.corr_id=self.token=self.tank_id=self.room_id=''
            
        def on_response(self, ch, method, props, body):
            if self.corr_id == props.correlation_id:
                self.response = json.loads(body)

        def call(self,key,message={}):
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(
                exchange='X:routing.topic',routing_key=key,properties=pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.corr_id,),
                body=json.dumps(message)
            )
            while self.response is None:
                self.connection.process_data_events()
        def check_server_status(self):
            self.call('tank.request.healthcheck')
            return self.response['status']==200

        def obtain_token(self,room_id):
            message={
                'roomId': room_id
            }
            self.call('tank.request.register',message)
            self.token=self.response['token']
            self.tank_id=self.response['tankId']
            self.room_id=self.response['roomId']
        def turn_tank(self,token,direction):
            message={
                'token': token,
                'direction': direction
            }
            self.call('tank.request.turn',message)
        def fire_tank(self,token):
            message={
                'token':token
            }
            self.call('tank.request.fire',message)
    class TankConsumerClient(Thread):
        def __init__(self,room_id):
            super().__init__()
            self.connection = pika.BlockingConnection(pika.ConnectionParameters('34.254.177.17',5672,'dar-tanks',pika.PlainCredentials('dar-tanks','5orPLExUYnyVYZg48caMpX')))
            
            self.channel=self.connection.channel()
            queue=self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)
            queue_event=queue.method.queue
            self.channel.queue_bind(exchange='X:routing.topic',queue=queue_event, routing_key='event.state.'+room_id)        
            self.channel.basic_consume(queue=queue_event,on_message_callback=self.on_response,auto_ack=True)
            self.response=None
        def on_response(self, ch, method, props, body):
            self.response = json.loads(body)
        def run(self):
            self.channel.start_consuming()

    def draw_tank(x,y,direction,a,b,c,Id):
        f6 = pygame.font.SysFont('calibri', 12)
        text6 = f6.render(str(Id), 1, (a,b,c))
        screen.blit(text6, (x-5,y-17))    
        
        if direction=="UP":
            act = pygame.transform.rotate(TANK, 0)
            screen.blit(act,(x,y))
        if direction=="DOWN":
            act = pygame.transform.rotate(TANK, 180)
            screen.blit(act,(x,y))
        if direction=="RIGHT":
            act = pygame.transform.rotate(TANK, -90)
            screen.blit(act,(x,y))
        if direction=="LEFT":
            act = pygame.transform.rotate(TANK, 90)
            screen.blit(act,(x,y))



    def draw_bullet(x,y,direction,e,r,f):
        if direction=="UP" or direction=="DOWN":
            pygame.draw.rect(screen,(e,r,f),(x,y,5,15))
        else:
            pygame.draw.rect(screen,(e,r,f),(x,y,15,5))
    def stattable():
        pygame.draw.rect(screen,(255,255,255),(800,0,200,600))
        f2 = pygame.font.SysFont('calibri', 45)
        text2 = f2.render('ID', 1, (0, 0, 0))
        screen.blit(text2, (802, 1))
        screen.blit(text2, (801, 1))
        pygame.draw.rect(screen,(0,0,0),(800,42,200,3))

        pygame.draw.rect(screen,(0,0,0),(800,60,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,80,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,100,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,120,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,140,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,160,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,180,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,200,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,220,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,240,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,260,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,280,200,2))

        pygame.draw.rect(screen,(0,0,0),(0,600,800,100))
        pygame.draw.rect(screen,(255,255,255),(800,600,200,100))
        f2 = pygame.font.SysFont('calibri', 35)
        text2 = f2.render('Score', 1, (0, 0, 0))
        screen.blit(text2, (857, 7))
        screen.blit(text2, (857, 7))
        pygame.draw.rect(screen,(0,0,0),(851,0,3,292))


        f2 = pygame.font.SysFont('calibri', 40)
        text2 = f2.render('Hp', 1, (0, 0, 0))
        screen.blit(text2, (949, 5))
        screen.blit(text2, (948, 5))
        pygame.draw.rect(screen,(0,0,0),(941,0,3,292))

        pygame.draw.rect(screen,(255,0,0),(800,282,200,44))
        pygame.draw.rect(screen,(255,255,255),(802,284,196,40))
        f6 = pygame.font.SysFont('calibri', 25)
        text6 = f6.render('<--About Game-->', 1, (0,0,0))
        screen.blit(text6, (808,290))
        screen.blit(text6, (807,290))
        
        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('The Rules', 1, (138,43,226))
        screen.blit(text6, (820,335))
        screen.blit(text6, (821,335))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('This game is a multi-', 1, (0,0,255))
        screen.blit(text6, (810,357+7))
        screen.blit(text6, (811,357+7))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('player view of the game of tanks', 1, (0,0,255))
        screen.blit(text6, (805,375+10))
        screen.blit(text6, (804,375+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('You do not choose the ', 1, (165,42,42))
        screen.blit(text6, (810,400+15))
        screen.blit(text6, (811,400+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('room where you go ', 1, (165,42,42))
        screen.blit(text6, (804,418+10))
        screen.blit(text6, (805,418+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('up to 11 people can play', 1, (255,97,3))
        screen.blit(text6, (810,443+15))
        screen.blit(text6, (811,443+15))

        f6 = pygame.font.SysFont('blackadderitc', 23)
        text6 = f6.render('with you in the same room', 1, (255,97,3))
        screen.blit(text6, (804,461+10))
        screen.blit(text6, (805,461+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('You have to shoot them', 1, (127,255,0))
        screen.blit(text6, (810,481+15))
        screen.blit(text6, (811,481+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('and protect yourself', 1, (127,255,0))
        screen.blit(text6, (804,499+10))
        screen.blit(text6, (805,499+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('If you lose, the game', 1, (104,34,139))
        screen.blit(text6, (810,520+15))
        screen.blit(text6, (811,520+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('will stop', 1, (104,34,139))
        screen.blit(text6, (804,538+10))
        screen.blit(text6, (805,538+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('If you do not move for', 1, (255,20,147))
        screen.blit(text6, (810,558+15))
        screen.blit(text6, (811,558+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('30 seconds, you fly out', 1, (255,20,147))
        screen.blit(text6, (804,576+10))
        screen.blit(text6, (805,576+10))

        f6 = pygame.font.SysFont('blackadderitc', 23)
        text6 = f6.render('Both live people and bots', 1, (75,0,130))
        screen.blit(text6, (804,596+15))
        screen.blit(text6, (805,596+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('can play in one room', 1, (75,0,130))
        screen.blit(text6, (804,614+10))
        screen.blit(text6, (805,614+10))

        f6 = pygame.font.SysFont('snapitc', 60)
        text6 = f6.render('Good luck my friend!!!', 1, (128,0,0))
        screen.blit(text6, (10,615))

    def table(z,b,c,d):
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render(str(b), 1, (0,0,0))
        screen.blit(text6, (808,45+z))
        screen.blit(text6, (807,45+z))

        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render(str(c), 1, (0,0,0))
        screen.blit(text6, (898,45+z))
        screen.blit(text6, (897,45+z))

        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render(str(d), 1, (0,0,0))
        screen.blit(text6, (968,45+z))
        screen.blit(text6, (967,45+z))

    class Multimenu(object):
        def __init__(self,screen):
            self.screen=screen
            self.menufon=pygame.Rect(598,248,304,54)
            self.menu=pygame.Rect(600,250,300,50)
            self.playfon=pygame.Rect(598,348,304,54)
            self.play=pygame.Rect(600,350,300,50)
            self.x=0
            self.y=0
            self.Amir=0
        def color(self,x1,y1):
            self.mish=(x1,y1,2,2)
            if self.menu.colliderect(self.mish):
                self.x=255
            elif not self.menu.colliderect(self.mish):
                self.x=0

            if self.play.colliderect(self.mish):
                self.y=255
            elif not self.play.colliderect(self.mish):
                self.y=0
        def draw(self,ending):
            self.screen.fill((255,255,255))
            f6 = pygame.font.SysFont('snapitc', 60)
            text6 = f6.render('GAMEPLAY when you played', 1, (0,0,0))
            self.screen.blit(text6, (0,0))
            z=0
            
            for i in range(0,len(ending)-3,4):
                a=ending[i]
                b=ending[i+1]
                c=ending[i+2]
                d=ending[i+3]
                f6 = pygame.font.SysFont('Georgia', 30)
                text6 = f6.render(a+" - "+b+" , "+ c+ " - " +d, 1, (255,0,0))
                self.screen.blit(text6,(20,90+z))
                self.screen.blit(text6,(20,91+z))
                self.screen.blit(text6,(20,92+z))
                z+=40
            pygame.draw.rect(self.screen,(0,0,0),self.menufon)
            pygame.draw.rect(self.screen,(255,255,255),self.menu)


            pygame.draw.rect(self.screen,(0,0,0),self.playfon)
            pygame.draw.rect(self.screen,(255,255,255),self.play)

            f6 = pygame.font.SysFont('Georgia', 30)
            text6 = f6.render('Back to main-menu', 1, (self.x,0,0))
            self.screen.blit(text6, (610,260))
            self.screen.blit(text6, (611,260))

            f6 = pygame.font.SysFont('Georgia', 30)
            text6 = f6.render('Play multiplayer game', 1, (self.y,0,0))
            self.screen.blit(text6, (600,355))
            self.screen.blit(text6, (601,355))
        def perehod(self,x1,y1):
            self.mish=(x1,y1,2,2)
            if self.menu.colliderect(self.mish):
                self.Amir=1

            elif self.play.colliderect(self.mish):
                self.Amir=2
        
    def game():
        ending=[]
        Bitti=False
        done=True
        Time2=121
        can=True 
        global MM
        global MP
        while done:
            cnt1=[]
            cnt2=[]
            cnt3=[]
            cnttotal=[]
            cnttotalsorted=[]
            printres=[]
            listid=[]
            listhp=[]
            listscore=[]
            s=""
        
            screen.fill((0,0,0))
            z=0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    MP=False
                    MM=True
                    done=False
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_UP:
                        client.turn_tank(client.token,"UP")
                    if event.key ==pygame.K_DOWN:
                        client.turn_tank(client.token,"DOWN")
                    if event.key==pygame.K_LEFT:
                        client.turn_tank(client.token,"LEFT")
                    if event.key==pygame.K_RIGHT:
                        client.turn_tank(client.token,"RIGHT")
                    if event.key==pygame.K_SPACE:
                        client.fire_tank(client.token)
                        vistrel.play()

                if event.type == pygame.MOUSEMOTION:
                    Multi.color(event.pos[0],event.pos[1])
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Multi.perehod(event.pos[0],event.pos[1])

            Time=event_client.response['remainingTime']
            if Time>Time2:
                Bitti=True
            Time2=Time
            if Time==1:
                Bitti=True

            f6 = pygame.font.SysFont('snapitc', 45)
            text6 = f6.render('Remaining time: {}'.format(Time), 1, (255,255,255))
            screen.blit(text6, (200,0))
            tanks=event_client.response['gameField']['tanks']

            for tank in tanks:
                if tank["id"]!=client.tank_id:
                    a=255
                    b=c=0
                else:
                    a=b=255
                    c=0
                Id=tank["id"]
                draw_tank(tank['x'],tank['y'],tank['direction'],a,b,c,Id)
            
            for b in event_client.response["gameField"]["bullets"]:
                if b['owner']!=client.tank_id:
                    e=255
                    r=f=0
                else:
                    e=r=255
                    f=0
                draw_bullet(b['x'],b['y'],b['direction'],e,r,f)
            stattable()

            for b in event_client.response["gameField"]['tanks']:
                for i in range(5,len(b['id']),1):
                    s+=b['id'][i]
                listid.append(int(s))
                listhp.append(int(b['health']))
                listscore.append(int(b['score']))
                s=""
            
            cnt=0
            for i in range(len(listid)):
                for j in range(len(listid)):
                    if listid[i]>listid[j] and i!=j:
                        cnt+=1
                cnt1.append(cnt)
                cnt=0

            for i in range(len(listid)):
                for j in range(len(listid)):
                    if listhp[i]>=listhp[j] and i!=j:
                        cnt+=10
                cnt2.append(cnt)
                cnt=0

            for i in range(len(listid)):
                for j in range(len(listid)):
                    if listscore[i]>=listscore[j] and i!=j:
                        cnt+=100
                cnt3.append(cnt)
                cnt=0

            for i in range(len(listid)):
                cnttotal.append(cnt1[i]+cnt2[i]+cnt3[i])
                cnttotalsorted.append(cnt1[i]+cnt2[i]+cnt3[i])

            cnttotalsorted.sort()

            for i in range(len(listid)-1,-1,-1):
                for j in range(len(listid)):
                    if cnttotalsorted[i]==cnttotal[j]:
                        printres.append(j)
                        break
                    
            for i in printres:
                b=listid[i]
                c=listscore[i]
                d=listhp[i]

                table(z,b,c,d)
                z+=20

            mpl=""
            ll=""

            if len(event_client.response["losers"])>0:
                mpl="loser"
                ll=event_client.response["losers"]
                for j in ll:
                    if can:
                        print(j["tankId"])
                        if j["tankId"]==client.tank_id:
                            Bitti=True
                            ending.append("YOU")
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                            can=False
                        else:
                            ending.append(j["tankId"])
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                    ll.remove(j) 
            if len(event_client.response["kicked"])>0:
                mpl="kicked"
                ll=event_client.response["kicked"]
                for j in ll:
                    
                    if can:
                        print(j["tankId"])
                        if j["tankId"]==client.tank_id:
                            Bitti=True
                            ending.append("YOU")
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                            can=False
                        else:
                            ending.append(j["tankId"])
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                    ll.remove(j) 
            if len(event_client.response["winners"])>0:
                mpl="winner"
                ll=event_client.response["winners"]
                for j in ll:
                    
                    if can:
                        print(j["tankId"])
                        if j["tankId"]==client.tank_id:
                            Bitti=True
                            ending.append("YOU")
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                            can=False
                        else:
                            ending.append(j["tankId"])
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                    ll.remove(j) 
            if Bitti:
                Multi.draw(ending)
                if Multi.Amir==2:
                    global MG
                    MG=False
                    return 0
                elif Multi.Amir==1:   
                    MP=False
                    MM=True
                    return 0
            pygame.display.update()
    
    Multi=Multimenu(screen)
    client=TankRpcClient()
    client.check_server_status()
    global server
    try:
        client.obtain_token('room-'+str(server%30+1))
        event_client=TankConsumerClient('room-'+str(server%30+1))
        event_client.daemon=True
        event_client.start()
        game()
    except:
        server+=1
def mainAI():
    TANK=pygame.image.load("img\\tank.png")
    class TankRpcClient():
        def __init__(self):
            self.connection = pika.BlockingConnection(pika.ConnectionParameters('34.254.177.17',5672,'dar-tanks',pika.PlainCredentials('dar-tanks','5orPLExUYnyVYZg48caMpX')))
            self.channel=self.connection.channel()
            queue=self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)
            self.callback_queue=queue.method.queue
            self.channel.queue_bind(exchange='X:routing.topic',queue=self.callback_queue)
            self.channel.basic_consume(queue=self.callback_queue,on_message_callback=self.on_response,auto_ack=True)
            self.response=self.corr_id=self.token=self.tank_id=self.room_id=''
            
        def on_response(self, ch, method, props, body):
            if self.corr_id == props.correlation_id:
                self.response = json.loads(body)

        def call(self,key,message={}):
            self.response = None
            self.corr_id = str(uuid.uuid4())
            self.channel.basic_publish(
                exchange='X:routing.topic',routing_key=key,properties=pika.BasicProperties(reply_to=self.callback_queue,correlation_id=self.corr_id,),
                body=json.dumps(message)
            )
            while self.response is None:
                self.connection.process_data_events()
        def check_server_status(self):
            self.call('tank.request.healthcheck')
            return self.response['status']==200

        def obtain_token(self,room_id):
            message={
                'roomId': room_id
            }
            self.call('tank.request.register',message)
            self.token=self.response['token']
            self.tank_id=self.response['tankId']
            self.room_id=self.response['roomId']
        def turn_tank(self,token,direction):
            message={
                'token': token,
                'direction': direction
            }
            self.call('tank.request.turn',message)
        def fire_tank(self,token):
            message={
                'token':token
            }
            self.call('tank.request.fire',message)
    class TankConsumerClient(Thread):
        def __init__(self,room_id):
            super().__init__()
            self.connection = pika.BlockingConnection(pika.ConnectionParameters('34.254.177.17',5672,'dar-tanks',pika.PlainCredentials('dar-tanks','5orPLExUYnyVYZg48caMpX')))
            
            self.channel=self.connection.channel()
            queue=self.channel.queue_declare(queue='',auto_delete=True,exclusive=True)
            queue_event=queue.method.queue
            self.channel.queue_bind(exchange='X:routing.topic',queue=queue_event, routing_key='event.state.'+room_id)        
            self.channel.basic_consume(queue=queue_event,on_message_callback=self.on_response,auto_ack=True)
            self.response=None
        def on_response(self, ch, method, props, body):
            self.response = json.loads(body)
        def run(self):
            self.channel.start_consuming()

    def draw_tank(x,y,direction,a,b,c,Id):
        f6 = pygame.font.SysFont('calibri', 12)
        text6 = f6.render(str(Id), 1, (a,b,c))
        screen.blit(text6, (x-5,y-17))    
        
        if direction=="UP":
            act = pygame.transform.rotate(TANK, 0)
            screen.blit(act,(x,y))
        if direction=="DOWN":
            act = pygame.transform.rotate(TANK, 180)
            screen.blit(act,(x,y))
        if direction=="RIGHT":
            act = pygame.transform.rotate(TANK, -90)
            screen.blit(act,(x,y))
        if direction=="LEFT":
            act = pygame.transform.rotate(TANK, 90)
            screen.blit(act,(x,y))
    def draw_bullet(x,y,direction,e,r,f):
        if direction=="UP" or direction=="DOWN":
            pygame.draw.rect(screen,(e,r,f),(x,y,5,15))
        else:
            pygame.draw.rect(screen,(e,r,f),(x,y,15,5))
    def stattable():
        pygame.draw.rect(screen,(255,255,255),(800,0,200,600))
        f2 = pygame.font.SysFont('calibri', 45)
        text2 = f2.render('ID', 1, (0, 0, 0))
        screen.blit(text2, (802, 1))
        screen.blit(text2, (801, 1))
        pygame.draw.rect(screen,(0,0,0),(800,42,200,3))

        pygame.draw.rect(screen,(0,0,0),(800,60,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,80,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,100,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,120,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,140,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,160,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,180,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,200,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,220,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,240,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,260,200,2))
        pygame.draw.rect(screen,(0,0,0),(800,280,200,2))

        pygame.draw.rect(screen,(0,0,0),(0,600,800,100))
        pygame.draw.rect(screen,(255,255,255),(800,600,200,100))
        f2 = pygame.font.SysFont('calibri', 35)
        text2 = f2.render('Score', 1, (0, 0, 0))
        screen.blit(text2, (857, 7))
        screen.blit(text2, (857, 7))
        pygame.draw.rect(screen,(0,0,0),(851,0,3,292))


        f2 = pygame.font.SysFont('calibri', 40)
        text2 = f2.render('Hp', 1, (0, 0, 0))
        screen.blit(text2, (949, 5))
        screen.blit(text2, (948, 5))
        pygame.draw.rect(screen,(0,0,0),(941,0,3,292))

        pygame.draw.rect(screen,(255,0,0),(800,282,200,44))
        pygame.draw.rect(screen,(255,255,255),(802,284,196,40))
        f6 = pygame.font.SysFont('calibri', 25)
        text6 = f6.render('<--About Game-->', 1, (0,0,0))
        screen.blit(text6, (808,290))
        screen.blit(text6, (807,290))
        
        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('The Rules', 1, (138,43,226))
        screen.blit(text6, (820,335))
        screen.blit(text6, (821,335))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('This game is a multi-', 1, (0,0,255))
        screen.blit(text6, (810,357+7))
        screen.blit(text6, (811,357+7))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('player view of the game of tanks', 1, (0,0,255))
        screen.blit(text6, (805,375+10))
        screen.blit(text6, (804,375+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('You do not choose the ', 1, (165,42,42))
        screen.blit(text6, (810,400+15))
        screen.blit(text6, (811,400+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('room where you go ', 1, (165,42,42))
        screen.blit(text6, (804,418+10))
        screen.blit(text6, (805,418+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('up to 11 people can play', 1, (255,97,3))
        screen.blit(text6, (810,443+15))
        screen.blit(text6, (811,443+15))

        f6 = pygame.font.SysFont('blackadderitc', 23)
        text6 = f6.render('with you in the same room', 1, (255,97,3))
        screen.blit(text6, (804,461+10))
        screen.blit(text6, (805,461+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('You have to shoot them', 1, (127,255,0))
        screen.blit(text6, (810,481+15))
        screen.blit(text6, (811,481+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('and protect yourself', 1, (127,255,0))
        screen.blit(text6, (804,499+10))
        screen.blit(text6, (805,499+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('If you lose, the game', 1, (104,34,139))
        screen.blit(text6, (810,520+15))
        screen.blit(text6, (811,520+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('will stop', 1, (104,34,139))
        screen.blit(text6, (804,538+10))
        screen.blit(text6, (805,538+10))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('If you do not move for', 1, (255,20,147))
        screen.blit(text6, (810,558+15))
        screen.blit(text6, (811,558+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('30 seconds, you fly out', 1, (255,20,147))
        screen.blit(text6, (804,576+10))
        screen.blit(text6, (805,576+10))

        f6 = pygame.font.SysFont('blackadderitc', 23)
        text6 = f6.render('Both live people and bots', 1, (75,0,130))
        screen.blit(text6, (804,596+15))
        screen.blit(text6, (805,596+15))

        f6 = pygame.font.SysFont('blackadderitc', 25)
        text6 = f6.render('can play in one room', 1, (75,0,130))
        screen.blit(text6, (804,614+10))
        screen.blit(text6, (805,614+10))

        f6 = pygame.font.SysFont('snapitc', 60)
        text6 = f6.render('Good luck my friend!!!', 1, (128,0,0))
        screen.blit(text6, (10,615))

    def table(z,b,c,d):
        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render(str(b), 1, (0,0,0))
        screen.blit(text6, (808,45+z))
        screen.blit(text6, (807,45+z))

        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render(str(c), 1, (0,0,0))
        screen.blit(text6, (898,45+z))
        screen.blit(text6, (897,45+z))

        f6 = pygame.font.SysFont('calibri', 18)
        text6 = f6.render(str(d), 1, (0,0,0))
        screen.blit(text6, (968,45+z))
        screen.blit(text6, (967,45+z))

    class Multimenu(object):
        def __init__(self,screen):
            self.screen=screen
            self.menufon=pygame.Rect(598,248,304,54)
            self.menu=pygame.Rect(600,250,300,50)
            self.playfon=pygame.Rect(598,348,304,54)
            self.play=pygame.Rect(600,350,300,50)
            self.x=0
            self.y=0
            self.Amir=0
        def color(self,x1,y1):
            self.mish=(x1,y1,2,2)
            if self.menu.colliderect(self.mish):
                self.x=255
            elif not self.menu.colliderect(self.mish):
                self.x=0

            if self.play.colliderect(self.mish):
                self.y=255
            elif not self.play.colliderect(self.mish):
                self.y=0
        def draw(self,ending):
            self.screen.fill((255,255,255))
            f6 = pygame.font.SysFont('snapitc', 60)
            text6 = f6.render('GAMEPLAY when you played', 1, (0,0,0))
            self.screen.blit(text6, (0,0))
            z=0
            
            for i in range(0,len(ending)-3,4):
                a=ending[i]
                b=ending[i+1]
                c=ending[i+2]
                d=ending[i+3]
                f6 = pygame.font.SysFont('Georgia', 30)
                text6 = f6.render(a+" - "+b+" , "+ c+ " - " +d, 1, (255,0,0))
                self.screen.blit(text6,(20,90+z))
                self.screen.blit(text6,(20,91+z))
                self.screen.blit(text6,(20,92+z))
                z+=40
            pygame.draw.rect(self.screen,(0,0,0),self.menufon)
            pygame.draw.rect(self.screen,(255,255,255),self.menu)


            pygame.draw.rect(self.screen,(0,0,0),self.playfon)
            pygame.draw.rect(self.screen,(255,255,255),self.play)

            f6 = pygame.font.SysFont('Georgia', 30)
            text6 = f6.render('Back to main-menu', 1, (self.x,0,0))
            self.screen.blit(text6, (610,260))
            self.screen.blit(text6, (611,260))

            f6 = pygame.font.SysFont('Georgia', 30)
            text6 = f6.render('Play multiplayer game', 1, (self.y,0,0))
            self.screen.blit(text6, (600,355))
            self.screen.blit(text6, (601,355))
        def perehod(self,x1,y1):
            self.mish=(x1,y1,2,2)
            if self.menu.colliderect(self.mish):
                self.Amir=1

            elif self.play.colliderect(self.mish):
                self.Amir=2

    clock=pygame.time.Clock()
    def game():
        Id=x=y=0
        ending=[]
        Bitti=False
        done=True
        Time2=121
        can=True 
        global MM
        global MPAI
        while done:
            cnt1=[]
            cnt2=[]
            cnt3=[]
            cnttotal=[]
            cnttotalsorted=[]
            printres=[]
            listid=[]
            listhp=[]
            listscore=[]
            s=""
            z=0
            screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    MPAI=False
                    MM=True
                    done=False
                if event.type == pygame.MOUSEMOTION:
                    Multi.color(event.pos[0],event.pos[1])
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Multi.perehod(event.pos[0],event.pos[1])
            
            Time=event_client.response['remainingTime']
            if Time>Time2:
                Bitti=True
            Time2=Time
            if Time==1:
                Bitti=True

            f6 = pygame.font.SysFont('snapitc', 45)
            text6 = f6.render('Remaining time: {}'.format(Time), 1, (255,255,255))
            screen.blit(text6, (200,0))

            tanks=event_client.response['gameField']['tanks']

            bullets=event_client.response['gameField']['bullets']
            
            for bullet in bullets:
                if bullet['owner']!=Id:
                    if  (bullet['direction']=='UP') :
                        if bullet["x"]>x and bullet["x"]<(x+15)   :
                            if (bullet["y"]-y)<35:
                                client.turn_tank(client.token,'RIGHT')
                            else:
                                client.turn_tank(client.token,'DOWN')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'RIGHT')
                        elif bullet["x"]> (x+15) and bullet["x"]<(x+31) :
                            if (bullet["y"]-35)<y:
                                client.turn_tank(client.token,'LEFT')
                            else:
                                client.turn_tank(client.token,'DOWN')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'LEFT')
                    elif (bullet['direction']=='DOWN'):
                        if bullet["x"]> x and bullet["x"]<(x+15) :
                            if (y-bullet["y"])<35:
                                client.turn_tank(client.token,'RIGHT')
                            else:
                                client.turn_tank(client.token,'UP')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'RIGHT')
                        elif bullet["x"]> (x+15) and bullet["x"]<(x+31) :
                            if (y-bullet["y"])<35:
                                client.turn_tank(client.token,'LEFT')
                            else:
                                client.turn_tank(client.token,'UP')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'LEFT')
                    elif  (bullet['direction']=='RIGHT'):
                        if bullet["y"]> y and bullet["y"]<(y+15) : 
                            if (x-bullet["x"])<35:
                                client.turn_tank(client.token,'DOWN')
                            else:
                                client.turn_tank(client.token,'LEFT')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'DOWN')
                        elif bullet["y"]> (y+15) and bullet["y"]<(y+31) : 
                            if (x-bullet["x"])<35:
                                client.turn_tank(client.token,'UP')
                            else:
                                client.turn_tank(client.token,'LEFT')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'UP')
                    elif  (bullet['direction']=='LEFT'):
                        if bullet["y"]> y and bullet["y"]<(y+15) : 
                            if (bullet["x"]-x)<35:
                                client.turn_tank(client.token,'DOWN')
                            else:
                                client.turn_tank(client.token,'RIGHT')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'DOWN')
                        elif bullet["y"]>= y and bullet["y"]<(y+15) : 
                            if (bullet["x"]-x)<35:
                                client.turn_tank(client.token,'UP')
                            else:
                                client.turn_tank(client.token,'RIGHT')
                                client.fire_tank(client.token)
                                client.turn_tank(client.token,'UP')
                                
            for tank in tanks:
                if tank['id']!=Id:
                    if (tank['x']>x-15) and (tank['x']<x+31) and (tank['y']>y):
                        client.turn_tank(client.token,'DOWN')
                        client.fire_tank(client.token)
                        client.turn_tank(client.token,'RIGHT')

                    elif (tank['x']>x-15) and (tank['x']<x+31) and (tank['y']<y):
                        client.turn_tank(client.token,'UP')
                        client.fire_tank(client.token)
                        client.turn_tank(client.token,'LEFT')

                    elif (tank['y']>y-15) and (tank['y']<y+31) and (tank['x']>x):
                        client.turn_tank(client.token,'RIGHT')
                        client.fire_tank(client.token)
                        client.turn_tank(client.token,'UP')

                    elif (tank['y']>y-15) and (tank['y']<y+31) and (tank['x']<x):
                        client.turn_tank(client.token,'LEFT')
                        client.fire_tank(client.token)
                        client.turn_tank(client.token,'DOWN')
            for tank in tanks:
                if tank["id"]!=client.tank_id:
                    a=255
                    b=c=0
                else:
                    Id=tank['id']
                    x=tank['x']
                    y=tank['y']
                    a=b=255
                    c=0
                draw_tank(tank['x'],tank['y'],tank['direction'],a,b,c,tank["id"])
            for bullet in bullets:
                if bullet['owner']!=client.tank_id:
                    e=255
                    r=f=0
                else:
                    e=r=255
                    f=0
                draw_bullet(bullet['x'],bullet['y'],bullet['direction'],e,r,f)
            stattable()
            for b in event_client.response["gameField"]['tanks']:
                for i in range(5,len(b['id']),1):
                    s+=b['id'][i]
                listid.append(int(s))
                listhp.append(int(b['health']))
                listscore.append(int(b['score']))
                s=""
            
            cnt=0
            for i in range(len(listid)):
                for j in range(len(listid)):
                    if listid[i]>listid[j] and i!=j:
                        cnt+=1
                cnt1.append(cnt)
                cnt=0

            for i in range(len(listid)):
                for j in range(len(listid)):
                    if listhp[i]>=listhp[j] and i!=j:
                        cnt+=10
                cnt2.append(cnt)
                cnt=0

            for i in range(len(listid)):
                for j in range(len(listid)):
                    if listscore[i]>=listscore[j] and i!=j:
                        cnt+=100
                cnt3.append(cnt)
                cnt=0

            for i in range(len(listid)):
                cnttotal.append(cnt1[i]+cnt2[i]+cnt3[i])
                cnttotalsorted.append(cnt1[i]+cnt2[i]+cnt3[i])

            cnttotalsorted.sort()

            for i in range(len(listid)-1,-1,-1):
                for j in range(len(listid)):
                    if cnttotalsorted[i]==cnttotal[j]:
                        printres.append(j)
                        break
                    
            for i in printres:
                b=listid[i]
                c=listscore[i]
                d=listhp[i]

                table(z,b,c,d)
                z+=20

            mpl=""
            ll=""

            if len(event_client.response["losers"])>0:
                mpl="loser"
                ll=event_client.response["losers"]
                for j in ll:
                    if can:
                        print(j["tankId"])
                        if j["tankId"]==client.tank_id:
                            Bitti=True
                            ending.append("YOU")
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                            can=False
                        else:
                            ending.append(j["tankId"])
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                    ll.remove(j) 
            if len(event_client.response["kicked"])>0:
                mpl="kicked"
                ll=event_client.response["kicked"]
                for j in ll:
                    if can:
                        print(j["tankId"])
                        if j["tankId"]==client.tank_id:
                            Bitti=True
                            ending.append("YOU")
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                            can=False
                        else:
                            ending.append(j["tankId"])
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                    ll.remove(j) 
            if len(event_client.response["winners"])>0:
                mpl="winner"
                ll=event_client.response["winners"]
                for j in ll:
                    if can:
                        print(j["tankId"])
                        if j["tankId"]==client.tank_id:
                            Bitti=True
                            ending.append("YOU")
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                            can=False
                        else:
                            ending.append(j["tankId"])
                            ending.append(mpl)
                            ending.append("score")
                            ending.append(str(j["score"]))
                    ll.remove(j)

            if Bitti:
                Multi.draw(ending)
                if Multi.Amir==2:
                    global MGAI
                    MGAI=False
                    return 0
                elif Multi.Amir==1:   
                    MPAI=False
                    MM=True
                    return 0

            clock.tick(60)
            pygame.display.update()
    Multi=Multimenu(screen)
    client=TankRpcClient()
    client.check_server_status()
    global server
    try:
        client.obtain_token('room-'+str(server%30+1))
        event_client=TankConsumerClient('room-'+str(server%30+1))
        event_client.daemon=True
        event_client.start()
        game()
    except:
        server+=1

SPGAME=SP=MP=MPAI=OP=QU=False
MM=True
MGAI=True
direction1="up"
direction2="right"

singfon=pygame.image.load('img\\fon.png')
aifon=pygame.image.load('img\\fon.png')
multifon=pygame.image.load('img\\fon.png')
food=pygame.image.load('img\\food.png')

war=pygame.mixer.Sound('sounds\\war.wav')
vistrel=pygame.mixer.Sound('sounds\\vistrel.wav')
win=pygame.mixer.Sound('sounds\\win.wav')

bullet=Bullet(screen)
player=Tank(screen)
option=Options(screen)
Menu=MainMenu(screen)
Single=single(screen)

fon=pygame.image.load("img\\fon.png")

musicplaying=True
war.play()

x=210
y=180
z=140
Stenki=[]
st=True
start=konec=0
foodinpole=kocnulcya=False

eating1=0
vol1=vol2=vol3=1
P=random.randint(15,25)
s=0
while done:
    war.set_volume(1/(10+vol1*5))
    
    player1=pygame.Rect(player.x,player.y,40,40)
    player2=pygame.Rect(player.x1,player.y1,40,40)
    bullet1=pygame.Rect(bullet.bullet1.x,bullet.bullet1.y,10,10)
    bullet2=pygame.Rect(bullet.bullet2.x,bullet.bullet2.y,10,10)

    ms= clock.tick(FPS)
    secund+=ms/1000
    s=ms/1000
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            done = False
        if event.type == pygame.MOUSEMOTION:
            Menu.color(event.pos[0],event.pos[1])
            Single.color(event.pos[0],event.pos[1])
            option.color(event.pos[0],event.pos[1])
        if event.type == pygame.MOUSEBUTTONDOWN:
            Menu.perehod(event.pos[0],event.pos[1])
            Single.perehod(event.pos[0],event.pos[1])
            option.perehod(event.pos[0],event.pos[1])
            option.press(event.pos[0],event.pos[1],war,win,vistrel,vol2,vol3)
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction1="up"
            if event.key == pygame.K_s:
                direction1="down"
            if event.key == pygame.K_a:
                direction1="left"
            if event.key == pygame.K_d:
                direction1 = "right"

            if event.key == pygame.K_UP:
                direction2="up"
            if event.key == pygame.K_DOWN:
                direction2="down"
            if event.key == pygame.K_LEFT:
                direction2="left"
            if event.key == pygame.K_RIGHT:
                direction2 = "right"

            if event.key==pygame.K_SPACE and not bullet.shooting1:
                bullet.shoot1(direction1,player.x,player.y)
                if musicplaying:
                    vistrel.play()
                    vistrel.set_volume(1/vol3)
            if event.key==pygame.K_RETURN and not bullet.shooting2:
                bullet.shoot2(direction2,player.x1,player.y1)
                if musicplaying:
                    vistrel.play()
                    vistrel.set_volume(1/vol3)
        
    
    konec=secund
    if st:
        x_x=random.randint(2,28)
        y_y=random.randint(2,20)
        Stenki.append(pygame.Rect(x_x*32,y_y*32,30,30))
    if len(Stenki)==15:
        st=False
    if QU:
        pygame.quit()
        sys.exit()

    if SPGAME:
        screen.fill((x,y,z))
        player.direction(direction1,1)
        player.move(1,s)
        player.infinitepole(1)
        player.draw(1)
    
        bullet.move1(player.x1,player.y1,s)
        bullet.draw1()

        player.direction(direction2,2)
        player.move(2,s)
        player.infinitepole(2)
        player.draw(2)
        bullet.move2(player.x,player.y,s)
        bullet.draw2()
        if int(secund) % P==0 and not foodinpole:
            start=secund
            foodinpole=True
            x_s=random.randint(50,950)
            y_s=random.randint(50,650)
            Food=pygame.Rect(x_s,y_s,31,40)
        if konec-start>=7 and foodinpole and not kocnulcya:
            y_s=x_s=-100
            foodinpole=False
        if foodinpole and player1.colliderect(Food):
            player.double =player.first=kocnulcya=True
            eating1=pygame.time.get_ticks()
            y_s=x_s=-100
            foodinpole=False
            bullet.double =bullet.first=True
        if foodinpole and player2.colliderect(Food):
            player.double =player.second=kocnulcya=True
            eating1=pygame.time.get_ticks()
            y_s=x_s=-100
            foodinpole=False
            bullet.double =bullet.second=True
        if (konec-eating1/1000)>=5:
            player.double =player.first=player.second=bullet.double =bullet.first=bullet.second=False
        
        hp1=player.HP1()
        hp2=player.HP2()
        if hp1==0:
            screen.fill((0,0,0))
            f1 = pygame.font.SysFont('blackadderitc', 80)
            text1 = f1.render('Winner - RedTank', 10, (250, 0, 0))
            screen.blit(text1, (180,250))
            pygame.display.flip()
            war.stop()
            win.play()
            win.set_volume((1/vol2)*30)
            time.sleep(3)
            SPGAME=foodinpole=kocnulcya=False
            MM=st=True
            Stenki.clear()
            war.play(-1,0,0)
            player.restart(1)
            player.restart(2)
        if hp2==0:
            screen.fill((255,255,255))
            f1 = pygame.font.SysFont('blackadderitc', 80)
            text1 = f1.render('Winner - BlackTank', 10, (0, 0, 0))
            screen.blit(text1, (180,250))
            
            pygame.display.flip()
            war.stop()
            win.play()
            win.set_volume((1/vol2)*30)
            time.sleep(3)
            SPGAME=foodinpole=kocnulcya=False
            MM=st=True
            Stenki.clear()
            war.play(-1,0,0)
            player.restart(1)
            player.restart(2)
       
        
        for stenko in Stenki[:]:
            if stenko.colliderect(player1):
                Stenki.remove(stenko)
                player.Hp1-=1
            elif stenko.colliderect(player2):
                Stenki.remove(stenko)
                player.Hp2-=1
            elif stenko.colliderect(bullet1):
                Stenki.remove(stenko)
                bullet.shooting1=False
                bullet.bullet1.x=bullet.bullet1.y=-100
            elif stenko.colliderect(bullet2):
                Stenki.remove(stenko)
                bullet.shooting2=False
                bullet.bullet2.x=bullet.bullet2.y=-100
            pygame.draw.rect(screen,(138,54,15),stenko)
        if foodinpole:
            screen.blit(food,Food)
        f1 = pygame.font.Font(None, 25)
        text1 = f1.render('HP(black): {0:.1f}'.format(hp1), 10, (250, 0, 0))
        screen.blit(text1, (1,1))
        
        f2 = pygame.font.SysFont(None,25)
        text2 = f2.render('HP(red): {0:.1f}'.format(hp2), 10, (0, 0, 0))
        screen.blit(text2, (882, 1))
    pygame.display.set_caption("YOU ARE PLAYING           "+ str("%.2f" % secund))
    if MM or Single.Back:
        screen.blit(fon,(-97,0))
        Menu.draw()
    if SP and not Single.Back:
        Single.draw(singfon)
    if OP:
        option.draw()
        vol1,vol2,vol3=option.pressreturn()
        x,y,z=option.pressreturn2()
    if MP:
        main()
        if not MG:
            server+=random.randint(1,30)
            main()
    if MPAI:
        mainAI()
        if not MGAI:
            server+=random.randint(1,30)
            mainAI()
    pygame.display.flip()