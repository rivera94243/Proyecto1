from graphics import*
from itertools import*
def Location():
    
    Array=[]
    nums = permutations(['6','5','4'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    nums = permutations(['7','8','9'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    nums = permutations(['3','2','1'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    nums = permutations(['1','4','7'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    nums = permutations(['3','6','9'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    nums = permutations(['2','5','8'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    nums = permutations(['1','5','9'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    nums = permutations(['3','5','7'])
    for i in list(nums):
        tt=''.join(i)
        Array.append(tt)
    return Array

def check(value, comb):
    Array2=[]
    combinations = permutations(value, 3)
    
    for i in list(combinations):
        tt=''.join(i)
        Array2.append(tt)
       
    for i in Array2:
        if(i in comb):
            return True
    
def main():
    x=10
    y=10
    square = 1
    arr1 = []
    arr2 =[]
    
    #title of the GUI
    comb = Location()
    win = GraphWin('Tic-Tac-Toe', 300, 400)
    p1=[' ']
    pl="X"
    p2=[' ']
    #vertical
    vertical = Line(Point(105,15),Point(105, 285))
    vertical.draw(win)
    vertical =Line(Point(195,15),Point(195,285))
    vertical.draw(win)
    
    #horizontal lines
    horizontal=Line(Point(15,105),Point(285,105))
    horizontal.draw(win)
    horizontal = Line(Point(15,195),Point(285,195))
    horizontal.draw(win)
    i=0
    j=8
   
    while j >= 0:
            arr1.append(Point(x,y))
            arr2.append(Point(x + 90,y + 90))
            x=x + 90
            j= j - 1
            i= i + 1
            if (i == 3):       
                x = 10
                y = y + 90
                i = 0

    t1=Text(Point(1,1),p1)
    t2=Text(Point(1,1),p1)
    clk=True
    
    finres=False
    Box=False
    mid=Point(0,0)    

    
    while square < 10:
        ch= win.getMouse()
        num =""
        
        if (ch.x >arr1[0].x  and ch.x <arr2[0].x and ch.y >arr1[0].y  and ch.y<arr2[0].y):
            num="1"
            mid=Point(arr1[0].x +50,arr1[0].y+50)
            Box=True
            
        if (ch.x >arr1[1].x  and ch.x <arr2[1].x and ch.y >arr1[1].y  and ch.y<arr2[1].y):
            num="2"
            mid=Point(arr1[1].x + 50,arr1[1].y+50)
            Box=True
            
        if (ch.x >arr1[2].x  and ch.x <arr2[2].x and ch.y >arr1[2].y  and ch.y<arr2[2].y):
            num="3"
            mid=Point(arr1[2].x +50,arr1[2].y+50)
            Box=True
            
        if (ch.x >arr1[3].x  and ch.x <arr2[3].x and ch.y >arr1[3].y  and ch.y<arr2[3].y):
            num="4"
            mid=Point(arr1[3].x +50,arr1[3].y+50)
            Box=True
            
        if (ch.x >arr1[4].x  and ch.x <arr2[4].x and ch.y >arr1[4].y  and ch.y<arr2[4].y):
            num="5"
            mid=Point(arr1[4].x +50,arr1[4].y+50)
            Box=True
            
        if (ch.x >arr1[5].x  and ch.x <arr2[5].x and ch.y >arr1[5].y  and ch.y<arr2[5].y):
            num="6"
            mid=Point(arr1[5].x +50,arr1[5].y+50)
            Box=True
            
        if (ch.x >arr1[6].x  and ch.x <arr2[6].x and ch.y >arr1[6].y  and ch.y<arr2[6].y):
            num="7"
            mid=Point(arr1[6].x +50,arr1[6].y+50)
            Box=True
            
        if (ch.x >arr1[7].x  and ch.x <arr2[7].x and ch.y >arr1[7].y  and ch.y<arr2[7].y):
            num="8"
            mid=Point(arr1[7].x +50,arr1[7].y+50)
            Box=True
            
        if (ch.x >arr1[8].x  and ch.x <arr2[8].x and ch.y >arr1[8].y  and ch.y<arr2[8].y):
            num="9"
            mid=Point(arr1[8].x +50,arr1[8].y+50)
            Box=True
            
       
        if Box:
            text=Text(mid,pl)
            text.setSize(24)   
            text.draw(win)
            Box = False
            square=square + 1


        cn = 0
        if pl=="X":
            p1.append(num)
            if len(p1)>=3:
                finres=check(p1,comb)
            if finres:
                text = Text(Point(win.getWidth()/2,320),"The player one wins")
                text.setSize(15)
                text.setTextColor("blue")
                text.draw(win)
                clk=False
                break
            pl="O"
        
        else:
            cn+= 1
            p2.append(num)
            if len(p2)>=3:
                finres=check(p2,comb)
            if finres:
                text=Text(Point(win.getWidth()/2,320),"The player two wins")
                text.setSize(20)
                text.setTextColor("blue")
                text.draw(win)
                clk=False
                break
            pl="X"
             
    if clk:
        text=Text(Point(win.getWidth()/2,320),"The Game is aDraw\n maybe next time")
        text.setSize(15)
        text.setTextColor("red")
        text.draw(win)

        repeat = eval(input("Do you want to play again (y/n) ? "))
        if repeat.lower() == 'y':
            return True
        if repeat.lower() == 'n':
            return False
        
    
            
main()
