import time

#--------------------------------------
#Start of main scripts
#--------------------------------------
def playerOnStairs():
    p1,p2 = g.Point(0, 0),g.Point(70, 100)
    if p1.getX() < P.hitbox.getCenter().getX() < p2.getX():
        if p1.getY() < P.hitbox.getCenter().getY() < p2.getY():
            return True
        else:
            return False

global lvl
lvl = 1
gameWon = False

print ('Game Loading...')

time.sleep(3)

if lvl == 1:
    #initialization for level 1
    P = refPlayer('win',0,0)
    M2 = maze(lvl)
    P = Player(M2.w, 500, 550)
    H = Health(M2.w, 0, 590)
    monster1 = Monster(25,373,M2.w,'explore')
    monster2 = Monster(200,25,M2.w,'explore',g.Point(300,300))

    #control loop level 1
    key = None
    while key != 'q':
        key = M2.w.checkKey()
        P.control(key)
        click = M2.w.checkMouse()
        P.fire(click)

        if playerOnStairs():
            M2.w.close()
            lvl = 2
            break
        if H.playerDead:
            break
    M2.w.close()

if lvl == 2:
    #initialization for level 2
    M2 = maze(lvl)
    P = Player(M2.w, 575, 600)
    H = Health(M2.w, 0, 690)
    monster1 = Monster(25,373,M2.w,'explore')
    monster2 = Monster(725,373,M2.w,'wait',g.Point(300,300))
    monster3 = Monster(475,25,M2.w,'patrol',g.Point(475,226))
    #control loop level 2
    key = None
    while key != 'q':
        key = M2.w.checkKey()
        P.control(key)
        click = M2.w.checkMouse()
        P.fire(click)

        if playerOnStairs():
            M2.w.close()
            lvl = 3
            break
        if H.playerDead:
            break
    M2.w.close()

if lvl == 3:
    #initialization for level 2
    M2 = maze(lvl)
    P = Player(M2.w, 775, 600)
    H = Health(M2.w, 0, 690)
    monster1 = Monster(25,423,M2.w,'wait')
    monster2 = Monster(925,423,M2.w,'chase')
    monster3 = Monster(575,25,M2.w,'explore')
    monster4 = Monster(75,100,M2.w,'patrol',g.Point(301,100))
    #control loop level 3
    key = None
    while key != 'q':
        key = M2.w.checkKey()
        P.control(key)
        click = M2.w.checkMouse()
        P.fire(click)

        if playerOnStairs():
            M2.w.close()
            gameWon = True
            break

        if H.playerDead:
            break
    M2.w.close()

if gameWon:
    print ('Congratulations! You won!')
    time.sleep(1)
else:
    print ('Better luck next time!')
    time.sleep(1)
