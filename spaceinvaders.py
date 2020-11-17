import pyxel
import math
bulleth= 5
bulletw= 1
move=0
playerspeed=3
bulletspeed= 3
rockets = []
enemiesx= []
enemypos= []
upr = 113
 

 
class Game:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.load('space1.pyxres')
        self.x= 80
        self.pos= 80
        self.bullets = []
        pyxel.run(self.update, self.draw)
    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.x +=  playerspeed
        if pyxel.btn(pyxel.KEY_Q):
            self.x-= playerspeed
        if pyxel.btnp(pyxel.KEY_E):
            self.bullets.append(Bullet(self.x + (13 - bulletw) / 2))
        if self.x <= 0:
            self.x= 159
        if self.x >= 160:
            self.x= 0
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_W):
            self.pos= self.x

        for b in self.bullets:
            b.update()     

               
    def enemy(enemiesx, enemiesy):
        
       for i in range(5):
           for j in range(2):
             pyxel.rect(enemiesx[i], enemiesy[j], 3, 3, 10)

    def draw(self):
    
     for testx in range(1,119):
      if testx%19==0:
        enemiesx.append(testx +15)

     enemiesy= enemiesx.copy()
     enemiesy = [x - 30 for x in enemiesy]

     pyxel.cls(0)
     pyxel.blt(self.x, 112, 0, 1, 0, 14,8)

     for b in self.bullets:
            pyxel.rect(b.x, b.y, 1, 4, 9)     
        
     for i in range(6):
       enemypos.append(enemiesx[i], enemiesy[0])
       enemypos.append(enemiesx[i], enemiesy[1])
       enemypos.append(enemiesx[i], enemiesy[2])
      

     for i in range(6):
         pyxel.rect(enemiesx[i], enemiesy[0], 3, 3, 10)
         pyxel.rect(enemiesx[i], enemiesy[1], 3, 3, 10)
         pyxel.rect(enemiesx[i], enemiesy[2], 3, 3, 10)
    
        
  #      for e in enemypos:
   #
    #              if  e.x + e.w == b.x and b.x + b.w == e.x and b.y + b.h == e.y :
    
     #              b.alive = False


class Enemy:
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.w = 5
        self.h = 5
    def draw(self):
        pyxel.rect(self.x, self.y, 3, 3, 10)

       
class Bullet:
    def __init__(self, x):
        self.x = x
        self.y = 112
        self.w = bulletw
        self.h = bulleth
        self.alive = True
        rockets.append(self)

    def detectar_colisao(self,x1, y1, r1, x2, y2, r2):
        distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if distancia <= r1 + r2:
            return True
        else:
            return False
    
    def update(self):
        for testx in range(1,119):
         if testx%19==0:
          enemiesx.append(testx +15)
        
        enemiesy= enemiesx.copy()
        enemiesy = [x - 30 for x in enemiesy]
        for j in range(15):
         self.colidiu = self.detectar_colisao(self.x, self.y, self.w, enemypos[j], enemypos[j], 5)
        self.y -= bulletspeed

        if self.y + self.h - 1 < 0:
            self.alive = False

        if self.colidiu:
            del enemiesx[0] 
            del enemiesy[0]    

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 5)
        
     
Game()

#import pyxel
#class App:
#    def __init__(self):
 #       pyxel.init(160, 120)
  #      self.x = 0
  #      pyxel.run(self.update, self.draw)

   # def update(self):
    #    self.x = (self.x + 1) % pyxel.width

  #  def draw(self):
   #     pyxel.cls(0)
    #    pyxel.rect(self.x, 0, 8, 8, 9)
