import curses
from time import sleep
#import sfx
from curses import*;from random import*
import threading
#
#
class P3:
  '''fight the final boss'''
  bhell_my_timer = 60  # timer for part 2
  data_start_timer = False
  data_current_stage_timer = False  # in stage 2, where timer applies
  bhell_out_of_time = False

  def countdown():
    P3.bhell_my_timer = 15
    P3.bhell_out_of_time = False
    for i in range(15):
            P3.bhell_my_timer = P3.bhell_my_timer - 1
            sleep(1)
    P3.bhell_out_of_time = True

  def bhell():
    class A:             # ~~ASTEROID BELT~~
      w=0;a=4;t=2          # By u/Bombadil44
      def m(_):     # github.com/bombadil444
        _.x+=_.z;_.w+=1  # WASD=move P=shoot
        try:      # Don't Panic! Have Fun :D
          for i in 0,1: p(_.x,_.w+i,"O"*4)
        except: o.remove(_)
      def __init__(_): _.x=r(t);_.z=r(-1,2)
    class Z: #                       OOOO 0
      def __init__(_): _.x=x+3;_.y=y#OOOO
      def m(_): #                        AA
        _.y-=1;p(_.x,_.y,"0") #    OOOO <==>
        if _.y<=0: global m;m=0 #  OOOO  **
    z=curses.initscr();r=randrange;q,t=z.getmaxyx()
    l=["","<YOU>"," "];d=a=m=n=0;y=q-9
    def p(h,e,w):
      z.addstr(e,h,w)
    def k(e=100,w=1,l=0):
      if e in u: global d;global a;d=w;a=l
    z.keypad(1);z.nodelay(1);o=u=[];x=10
    while 48 not in u and P3.bhell_out_of_time == False:
      u=[];U=0;r(7)<5 and o.append(A())
      while U!=-1:
        U=z.getch();u+=U,
      m=(m,Z())[112 in u];k();k(97,-1)
      k(115,0,1);k(119,0,-1);z.clear()
      x+=d;y+=a;y-=(0,a)[y<0 or y+3>q]
      x-=(0,d)[x<=0 or x+7>t];m and m.m()
      for i in 0,1,2:
        p(x,y+i,l[i])
      for e in o:
        v=e.x;g=e.w;e.m();(v+e.a>x+3>=v
        and g+e.t>y+2>=g and u.append(48))
        if (m and v<=m.x<v+e.a and g<=m.y< g+e.t):
          o.remove(e);m=0;n+=1000
      p(10,0,"%s"%(n));curses.napms(50)
    curses.endwin()
    curses.napms(5000);z.keypad(0);curses.endwin()
    if 48 in u:
        print('You died')
    elif P3.bhell_out_of_time == True:
        print('You survived')
    sleep(2)



  def fight_boss():
    input('Do you want to die?')
    countdown_thread = threading.Thread(target=P3.countdown)
    countdown_thread.start()
    P3.bhell()
    sleep(2)

# write if name equals main
if __name__ == '__main__':
  P3.fight_boss()
