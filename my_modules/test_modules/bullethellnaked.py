import curses
from time import sleep
stdscr = curses.initscr()
class A:             # ~~ASTEROID BELT~~
  w=0
  a=4
  t=2          # By u/Bombadil44
  def m(_):     # github.com/bombadil444
    _.x+=_.z;_.w+=1  # WASD=move P=shoot
    try:      # Don't Panic! Have Fun :D
      for i in 0,1: p(_.x,_.w+i,"O"*4)
    except: o.remove(_)
  def __init__(_): _.x=r_range(x_boundary);_.z=r_range(-1,2)
class Z: #                       OOOO 0
  def __init__(_): _.x=x+3;_.y=player_position#OOOO
  def m(_): #                        AA
    _.y-=1;p(_.x,_.y,"0") #    OOOO <==>
    if _.y<=0: global m;m=0 #  OOOO  **
from curses import napms, endwin, initscr; from random import randrange
r_range=randrange
y_boundary,x_boundary=stdscr.getmaxyx()
player_shape=[" AA","<==>"," **"]
d=a=m=player_score=0
player_position =y_boundary-9
def p(h,e,w):
  stdscr.addstr(e,h,w)
def k(e=100,w=1,l=0):
  if e in stored_user_input: global d
  global a
  d=w
  a=l
stdscr.keypad(1)
stdscr.nodelay(1)
o=stored_user_input=[]
x=10
while 48 not in stored_user_input:
  stored_user_input=[]
  U=0
  r_range(7)<5 and o.append(A())
  while U!=-1:
    U=stdscr.getch()
  stored_user_input += U,
  m = (m,Z())[112 in stored_user_input]
  k()
  k(97,-1)
  k(115,0,1)
  k(119,0,-1)
  stdscr.erase()
  x+=d
  player_position+=a
  player_position-=(0,a)[player_position<0 or player_position+3>y_boundary]
  x-=(0,d)[x<=0 or x+7>x_boundary]
  m and m.m()
  for i in 0,1,2:
    p(x,player_position+i,player_shape[i])
  for e in o:
    # the below controls the falling data
    v=e.x
    g=e.w
    e.m()
    (v+e.a>x+3>=v and g+e.t>player_position+2>=g and stored_user_input.append(48))
    if (m and v<=m.x<v+e.a and g<=m.y<g+e.t):
      o.remove(e);m=0;player_score+=1000
    # end the part of controlling falling data
  p(10,0,"%s"%(player_score))
  napms(50)
endwin()
napms(5000)
stdscr.keypad(0)
endwin()