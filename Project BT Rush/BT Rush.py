
 #TanShoo
#BT Rush
#Jing Wei 
#The game consist of a charcter whuch is a girl that is late to a concert.
#Your job is to control the girl and go through different obstacals.
#You have to help her get to that concert on time.
#https://cooltext.com/Logo-Design-White?Font=1320 <--- for the text that was createdd 

from gamelib import*
game = Game(800,600,"BT Rush",180)
bk1 = Image("beeed.jpg",game)
bk1.resizeTo(800,600)
bk2 = Image("cross.jpg",game)
bk2.resizeTo(800,600)
bk3 = Image("street1.jpg",game)
bk3.resizeTo(800,600)
bk4 = Image("park.jpg",game)
bk4.resizeTo(800,600)
girl = Animation("girl.png",30,game,843/5,978/6,2)
#girl2 = Animation("girl4.png",5,game,843/5,181)
#girl2.visible = False
coke = Image("oof.png",game)
coke.resizeBy(-96)
bk5 = Image("build3.png",game)
bk5.resizeTo(800,600)
bk6 = Image("end.png",game)
bk6.resizeTo(800,600)
bk6.visible = False

#sound
traf = Sound("traf.wav",1)
wing = Sound("wing.wav",2)
#stamp = Sound("stamp.wav",3)
piano = Sound("piano.wav",3)

#text
START = Image("START.png",game)
START.y +=50
GP = Image("GP.png",game)
GP.y+=150
LOGO = Image("LOGO.png",game)
LOGO.y -=100
LOGO.resizeBy(30)
htp = Image("htp1.png",game)
htp.resizeTo(800,600)
htp.visible = False
git = Image("git.png",game)
git.resizeBy(-20)
git.y +=270
git.visible = False
story = Image("Capture.png",game)
story.resizeTo(800,600)
lg = Image("lg.png",game)
lg.y +=140
lg.visible = False
go = Image("go.png",game)
go.y-=60
go.visible = False

#For second lvl
dog = Animation("rundog.png",12,game,1057/3,1057/4)
dog.resizeBy(-28)
dog.moveTo(700,550)
dog.setSpeed(8,90)
corgi = Animation("corgi.png",21,game,1057/7,348/3)
corgi.resizeBy(20)
corgi.moveTo(650,500)
corgi.setSpeed(5,90)
potato = Animation("potato.png",18,game,1057/9,185/2)
potato.moveTo(950,525)
potato.setSpeed(4,90)
'''army = Animation("army.png",48,game,1059/3,1155/16)
army.moveTo(1050,510)
army.setSpeed(7,94)'''

#For third lvl
lp = Animation("lp1.png",6,game,999/3,685/2,3)
lp.resizeBy(-60)
lp.setSpeed(4,30)
lp1 = Animation("lp1.png",6,game,999/3,685/2,3)
lp1.moveTo(258,100)
lp1.resizeBy(-60)
lp1.setSpeed(4,30)
rp = Animation("rp1.png",6,game,999/3,685/2,2)
rp.moveTo(400,200)
rp.resizeBy(-60)
rp.setSpeed(6,60)
rp1 = Animation("rp1.png",6,game,999/3,685/2,2)
rp1.moveTo(600,200)
rp1.resizeBy(-60)
rp1.setSpeed(6,60)

#jumping
jumping = False
land = False
factor = 1
count = 0
floor = False

#building
person = Image("sec3.png",game)
person.resizeBy(-80)
cokes = Image("cokes1.png",game)
tree = Image("tre.png",game)
tree.resizeBy(-40)
tree.moveTo(180,350)
tre = Image("tre.png",game)
tre.resizeBy(-40)
tre.moveTo(600,350)
fou = Image("fou.png",game)
fou.moveTo(90,400)
fou.resizeBy(-46)
sad = Image("sad.png",game)
sad.y+=100
sad.x+=240

con = Image("concert1.jpg",game)
con.resizeTo(800,600)
win = Image("win.png",game)
win.y-=80
win.resizeBy(-30)
enjoy = Image("enjoy.png",game)
enjoy.y+=50



#start room
while not game.over:
    game.processInput()
    bk1.draw()
    START.draw()
    LOGO.draw()
    GP.draw()
    htp.draw()
    git.draw()
    piano.play()
    if START.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
    
    if mouse.collidedWith(GP,"rectangle") and mouse.LeftClick:
        htp.visible = True
        git.visible = True
        START.visible = False
        GP.visible = False
        LOGO.visible = False
        
    if git.collidedWith(mouse) and mouse.LeftClick:
        htp.visible = False
        git.visible = False
        START.visible = True
        GP.visible = True
        LOGO.visible = True
        

    game.update(30)
game.over = False

#story
coke.moveTo(780,580)
coke.resizeBy(50)
girl.moveTo(100,500)
while not game.over:
    game.processInput()
    story.draw()
    lg.draw()
    coke.draw()
    girl.draw()
    piano.play()
    if girl.collidedWith(coke):
        coke.visible = False
        lg.visible = True 
    if lg.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    if keys.Pressed[K_a]:
        girl.x-=5
    if keys.Pressed[K_d]:
        girl.x+=5

    game.update(30)
game.over = False


font = Font(black,30,black,"Lobster")

#first: cross
girl.resizeBy(20)
#girl2.resizeBy(20)
girl.moveTo(200,450)

cars = []
for index in range(28):
    cars.append(Image("room2.png",game))
    cars.append(Image("room3.png",game))
    cars.append(Image("taxi.png",game))
for index in range(len(cars)):
    x = randint(320,500)
    y = -randint(100,9000)
    cars[index].moveTo(x,y)
    s = randint(2,9)
    cars[index].setSpeed(s,180)
    cars[index].resizeBy(30)
coke.moveTo(688,600)
while not game.over:
    game.processInput()
    bk2.draw()
    girl.draw()
    #girl2.draw()
    #girl2.moveTo(girl.x,girl.y)
    coke.draw()
    traf.play()
    if girl.collidedWith(coke):
        game.over = True
    for index in range(len(cars)):
        cars[index].move()
        if girl.collidedWith(cars[index]):
            girl.moveTo(200,450)
    game.displayTime(20,0,font)
    
    '''if keys.Pressed[K_LEFT]:
        girl.visible = False
        girl2.visible = True
    if keys.Pressed[K_RIGHT]:
        girl.visible = True
        girl2.visible = False
    if mouse.LeftClick:
        game.over = True'''
    

    if keys.Pressed[K_w]:
       girl.y-=5
    if keys.Pressed[K_a]:
        girl.x-=5
    if keys.Pressed[K_d]:
        girl.x+=5
    if keys.Pressed[K_s]:
        girl.y+=5
    game.update(30)
game.over = False

#second: jump
game.setBackground(bk3)
girl.moveTo(180,490)
coke.moveTo(780,580)
while not game.over:
    game.processInput()
    bk3.draw()
    game.scrollBackground("left",2)
    #stamp.play()
    girl.draw()
    dog.move()
    corgi.move()
    potato.move()
    #army.move()
    coke.draw()
    bk6.draw()
    go.draw()
    if corgi.isOffScreen("left"):
        corgi.moveTo(950,500)
    if dog.isOffScreen("left"):
        dog.moveTo(950,550)
    if potato.isOffScreen("left"):
        potato.moveTo(950,525)
    '''if army.isOffScreen("left"):
        army.moveTo(950,510)'''
    if girl.collidedWith(corgi) or girl.collidedWith(dog) or girl.collidedWith(potato):
        bk6.visible = True
        go.visible = True
        game.time = False
        girl.visible = False
        
    if girl.collidedWith(coke):
        game.over = True
    
    if girl.y< 500:
        landed = False
    else:
        landed = True
    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True
    if jumping:
        girl.y -=30*factor
        
        factor*=.95
        landed = False
        floor = False
        if factor < .18:
            jumping = False
            factor = 1
    if not landed:
        girl.y +=8

    game.displayTime(20,0,font)
        
    if keys.Pressed[K_w]:
       girl.y-=5
    if keys.Pressed[K_a]:
        girl.x-=5
    if keys.Pressed[K_d]:
        girl.x+=5
    if keys.Pressed[K_s]:
        girl.y+=5

    game.update(30)
game.over = False

 #third: park
game.setBackground(bk4)
girl.resizeBy(10)
girl.moveTo(180,490)
coke.resizeBy(20)
coke.moveTo(790,596)
while not game.over:
    game.processInput()
    bk4.draw()
    game.scrollBackground("left",2)
    girl.draw()
    rp.move(True)
    lp.move(True)
    rp1.move(True)
    lp1.move(True)
    coke.draw()
    bk6.draw()
    wing.play()
    if girl.collidedWith(rp) or girl.collidedWith(rp1) or girl.collidedWith(lp) or girl.collidedWith(lp1) :
        bk6.visbile = True
        game.time = False
        go.visible = True
        girl.visible = False
        

    if mouse.LeftClick:
        game.over = True
    if girl.collidedWith(coke):
        game.over = True
    game.displayTime(20,0,font)
    
    if girl.y< 500:
        landed = False
    else:
        landed = True
    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping = True
    if jumping:
        girl.y -=20*factor
        factor*=.95
        landed = False
        floor = False
        if factor < .18:
            jumping = False
            factor = 1
    if not landed:
        girl.y +=8

    if keys.Pressed[K_w]:
       girl.y-=5
    if keys.Pressed[K_a]:
        girl.x-=5
    if keys.Pressed[K_d]:
        girl.x+=5
    if keys.Pressed[K_s]:
        girl.y+=5

    game.update(30)
game.over = False

#building
girl.resizeBy(-20)
girl.moveTo(180,490)
coke.resizeBy(-80)
coke.moveTo(410,390)
person.moveTo(300,360)
while not game.over:
    game.processInput()
    bk5.draw()
    coke.draw()
    person.draw()
    tree.draw()
    tre.draw()
    fou.draw()
    girl.draw()
    piano.play()
    game.drawText("Open",305,380)
    if girl.collidedWith(coke):
        game.over = True

    if keys.Pressed[K_w]:
       girl.y-=5
    if keys.Pressed[K_a]:
        girl.x-=5
    if keys.Pressed[K_d]:
        girl.x+=5
    if keys.Pressed[K_s]:
        girl.y+=5

    game.update(30)

game.over = False

#win
while not game.over:
    game.processInput()
    con.draw()
    win.draw()
    enjoy.draw()

    game.update(30)
game.over = False

game.quit()
