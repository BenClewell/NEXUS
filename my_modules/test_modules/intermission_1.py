import curses
from time import sleep

# REALLY COOL IDEA FROM bombadil444
# super illegible though because of the business card idea, haha
# change things in this and make a similar minigame?

class A:             # ~~ASTEROID BELT~~
  w=0;a=4;t=2          # By u/Bombadil44
  def m(_):     # github.com/bombadil444
    _.x+=_.z;_.w+=1  # WASD=move P=shoot
    try:      # Don't Panic! Have Fun :D])
      for i in 1,2: p(_.x,_.w+i,"O"*4)
    except: o.remove(_)
  def __init__(_): _.x=r(t);_.z=r(-1,2)
class Z: #                       OOOO 0
  def __init__(_): _.x=x+3;_.y=y#OOOO
  def m(_): #                        AA
    _.y-=1;p(_.x,_.y,"0") #    OOOO <==>
    if _.y<=0: global m;m=0 #  OOOO  **
from curses import*;from random import*
z=curses.initscr();r=randrange;q,t=z.getmaxyx()
l=["","<YOU>",""];d=a=m=n=0;y=q-9
def p(h,e,w):
    z.addstr(e,h,w)
    #print("POSITION: {} + {} + {}".format(e,h,w))
    #print(position)
    #if position.inch(8,t-20):
    #    curses.napms(0);z.keypad(0);curses.endwin()
def k(e=100,w=1,l=0):
  if e in u: global d;global a;d=w;a=l
z.keypad(1);z.nodelay(1);o=u=[];x=10
# addscr text in top-right of screen
found_the_node = False
while 48 not in u and found_the_node == False:
    goalpost = z.addstr(20,t-100,"HERE")
    # if player touches (8,t-20) then end the game
    u=[];U=0;r(7)<5 and o.append(A())
    while U!=-1: U=z.getch();u+=U,
    m=(m,Z())[112 in u];k();k(97,-1)
    k(115,0,1);k(119,0,-1);z.erase()
    x+=d;y+=a;y-=(0,a)[y<0 or y+3>q]
    x-=(0,d)[x<=0 or x+7>t];m and m.m()
    print(str(x)+"X + Y"+str(y) )
    print('t-100 = {}'.format(t-100))
    if (y == 17 or y == 17) and (x == (t-98 ) or x == (t-99) or x == (t-100) or x == (t-101) or x == (t-102)):
        curses.napms(0);z.keypad(0);curses.endwin()
        print('COOL')
        found_the_node = True

    for i in 0,1,2:
        player_position = p(x,y+i,l[i])
        # check to see if player_position's inch is (8,t-20)


    for e in o:
        v=e.x;g=e.w;e.m();(v+e.a>x+3>=v
        and g+e.t>y+2>=g and u.append(48))
        if (m and v<=m.x<v+e.a and g<=m.y<
        g+e.t): o.remove(e);m=0;n+=1000
    p(10,0,"%s"%(n));curses.napms(50)
curses.napms(0);z.keypad(0);curses.endwin()

if found_the_node == True:
    print('YOU FOUND THE NODE!')
else:
    print('YOU DID NOT FIND THE NODE!')
sleep(25)
