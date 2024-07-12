from mcpi import minecraft
import time
import math
import pygame

# some deffinitions
GLOWSTONE = 89
WOOL = 35
BRICK = 45
SSANDSTONE = 24,2
OBSIDIAN = 15

lHeight = 3
length = 50
lean = 10

halfNote = .5
tinyNote = .2

BLACK = 15
WHITE = 0

# Initialize pygame mixer
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load('/home/beiopi/Documents/lmms/projects/9min(3).mp3')

#create connection to minecraft
mc = minecraft.Minecraft.create()

class Vector:
    def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

def line(linePos1,linePos2,Block,Id,resolution):
    if ((linePos1.x - linePos2.x) != 0):
    
        #find the line of y=mx+b
        y_slope = ((linePos1.y - 1) - (linePos2.y - 1)) / (linePos1.x - linePos2.x)
        y_b = (linePos1.y - 1) - (linePos1.x * y_slope)

        #find the line of z=mx+b
        z_slope = (linePos1.z - linePos2.z) / (linePos1.x - linePos2.x)
        z_b = linePos1.z - (linePos1.x * z_slope)
    else:
       #pretend to find the line of y=mx+b
        y_slope = ((linePos1.y - 1) - (linePos2.y - 1)) / (0.001)
        y_b = (linePos1.y - 1) - (linePos1.x * y_slope)
        print("help me")
        #pretend to find the line of z=mx+b
        z_slope = (linePos1.z - linePos2.z) / (0.001)
        z_b = linePos1.z - (linePos1.x * z_slope) 
    
    #point the line in the right direction
    if linePos2.x > linePos1.x:
        m = 1
    elif linePos2.x < linePos1.x:
        m = -1
    else:
        m = 0
        print("fill command used")
        mc.setBlocks(linePos1.x,linePos1.y,linePos1.z,linePos2.x,linePos2.y,linePos2.z,Block, Id)

    if m != 0:
        #start line at deh begining
        x = linePos1.x

        #continue drawing line till you reach dah end
        while round(x,1) != round(linePos2.x):
            mc.setBlock(x, x * y_slope + y_b, x * z_slope + z_b, Block, Id)
            x += (m / resolution)
            #print(x,linePos2.x)

def startSong():
    global clock_start, wait_time_old, wait_time
    pygame.mixer.music.play()
    clock_start = time.clock_gettime(6) - 0
    wait_time_old = 0.0

def WAIT(t):
    global clock_start, wait_time_old, wait_time
    wait_time = wait_time_old + ((t) * (60/135))
    while (time.clock_gettime(6) < (clock_start + wait_time)):
        time.sleep(0.01)
    #print(wait_time)
    wait_time_old = wait_time

def buildSpeaker():
    # Right Speaker
    
    mc.setBlocks(-19, 11, -15, -21, 3, -18, 35, 15)
    mc.setBlocks(-18, 11, -18, -20, 3, -20, 35, 15)
    mc.setBlocks(-21, 11, -19, -23, 3, -21, 35, 15)
    mc.setBlocks(-22, 11, -16, -24, 3, -18, 35, 15)


    mc.setBlocks(-18, 10, -19, -19, 4, -16, 49)
    mc.setBlocks(-18, 4, -17, -18, 10, -16, 0)



    mc.setBlock(-19, 9, -17, SSANDSTONE)
    mc.setBlock(-18, 9, -18, SSANDSTONE)

    mc.setBlocks(-19, 6, -17, -19, 5, -17, BRICK)
    mc.setBlocks(-18, 6, -18, -18, 5, -18, BRICK)


    mc.setBlock(-19, 7, -17, SSANDSTONE)
    mc.setBlock(-18, 7, -18, SSANDSTONE)
    mc.setBlocks(-18, 6, -19, -18, 5, -19, SSANDSTONE)
    mc.setBlocks(-19, 5, -16, -19, 6, -16, SSANDSTONE)
    mc.setBlock(-19, 4, -17, SSANDSTONE)
    mc.setBlock(-18, 4, -18, SSANDSTONE)

    # Left Speaker
    

    mc.setBlocks(-19, 11, 14, -21, 3, 17, 35, 15)
    mc.setBlocks(-22, 11, 15, -24, 3, 17,35, 15)
    mc.setBlocks(-21, 11, 18, -23, 3, 20, 35, 15)
    mc.setBlocks(-18, 11, 17, -20, 3, 19, 35, 15)
    mc.setBlocks(-19, 4, 15, -19, 10, 16, 49)
    mc.setBlocks(-18, 4, 17, -18, 10, 18, 49)

    mc.setBlock(-18, 9, 17, SSANDSTONE)
    mc.setBlock(-19, 9, 16, SSANDSTONE)

    mc.setBlock(-18, 7, 17, SSANDSTONE)
    mc.setBlock(-19, 7, 16, SSANDSTONE)

    mc.setBlock(-18, 6, 17, BRICK)
    mc.setBlock(-19, 6, 16, BRICK)
    mc.setBlock(-18, 5, 17, BRICK)
    mc.setBlock(-19, 5, 16, BRICK)

    mc.setBlock(-18, 4, 17, SSANDSTONE)
    mc.setBlock(-19, 4, 16, SSANDSTONE)

    mc.setBlock(-18, 6, 18, SSANDSTONE)
    mc.setBlock(-18, 5, 18, SSANDSTONE)
    mc.setBlock(-19, 6, 15, SSANDSTONE)
    mc.setBlock(-19, 5, 15, SSANDSTONE)

def tweeters(what):
    mc.setBlock(-18, 9, 17, what)
    mc.setBlock(-19, 9, 16, what)
    mc.setBlock(-19, 9, -17, what)
    mc.setBlock(-18, 9, -18, what)

def drivers(what):
    # Rigth 
    mc.setBlock(-19, 7, -17, what)
    mc.setBlock(-18, 7, -18, what)
    mc.setBlocks(-18, 6, -19, -18, 5, -19, what)
    mc.setBlocks(-19, 5, -16, -19, 6, -16, what)
    mc.setBlock(-19, 4, -17, what)
    mc.setBlock(-18, 4, -18, what)

    # left
    mc.setBlock(-18, 7, 17, what)
    mc.setBlock(-19, 7, 16, what)
    mc.setBlock(-18, 4, 17, what)
    mc.setBlock(-19, 4, 16, what)
    mc.setBlock(-18, 6, 18, what)
    mc.setBlock(-18, 5, 18, what)
    mc.setBlock(-19, 6, 15, what)
    mc.setBlock(-19, 5, 15, what)

def sin(t):
    return math.sin(math.radians(t))

def cos(t):
    return math.cos(math.radians(t))

def lazer(n,block,iD):
    if ((lean > 45) and (lean < 135)):
        resolution = 5
    else:
        resolution = 1
    if (n <= 4):
        line(Vector(-20, 13, -11),Vector(
            -20 + length * cos(lean),
            13 + length * sin(lean) * sin(144 - (18 * n)),
            -11 + length * cos(144 - (18 * n)))
            , block, iD , resolution)
        
        mc.setBlocks(-20, 12, -11 - 1,-20, 12, -11 + 1, 20)
    else:
        line(Vector(-20, 12, 10),Vector(
            -20 + length * cos(lean),
            13 + length * sin(lean) * sin(180 - (18 * n)),
            -11 + length * cos(180 - (18 * n)))
            , block, iD , resolution)
        mc.setBlocks(-20, 12, 10 - 1,-20, 12, 10 + 1, 20)

    print(resolution)
    print(lean)

def pad(n, iD, d):
    if n == 1:
        mc.setBlocks(-16, -2, -8, -14, -2, -6,iD,d)
        mc.setBlocks(-16, -1, -12, -14, 1, -12,iD,d)
    if n == 2:
        mc.setBlocks(-12, -2, -8, -10, -2, -6,iD,d)
        mc.setBlocks(-12, -1, -12, -10, 1, -12,iD,d)
    if n == 3:
        mc.setBlocks(-8, -2, -8, -6, -2, -6,iD,d)
        mc.setBlocks(-8, -1, -12, -6, 1, -12,iD,d)
    if n == 4:
        mc.setBlocks(-4, -2, -8, -2, -2, -6,iD,d)
        mc.setBlocks(-4, -1, -12, -2, 1, -12,iD,d)
    if n == 5:
        mc.setBlocks(-16, -2, 8, -14, -2, 6,iD,d)
        mc.setBlocks(-16, 1, 12, -14, -1, 12,iD,d)
    if n == 6:
        mc.setBlocks(-12, -2, 6, -10, -2, 8,iD,d)
        mc.setBlocks(-12, 1, 12, -10, -1, 12,iD,d)
    if n == 7:
        mc.setBlocks(-8, -2, 8, -6, -2, 6,iD,d)
        mc.setBlocks(-8, 1, 12, -6, -1, 12,iD,d)
    if n == 8:
        mc.setBlocks(-4, 1, 12, -2, -1, 12,iD,d)
        mc.setBlocks(-4, -2, 8, -2, -2, 6,iD,d)
    if n == 9:
        mc.setBlocks(-16, -3, -1, -13, -3, -4,iD,d)
    if n == 10:
        mc.setBlocks(-12, -3, -1, -9, -3, -4,iD,d)
    if n == 11:
        mc.setBlocks(-8, -3, -1, -5, -3, -4,iD,d)
    if n == 12:
        mc.setBlocks(-1, -3, -4, -4, -3, -1,iD,d)
    if n == 13:
        mc.setBlocks(-13, -3, 4, -16, -3, 1,iD,d)
    if n == 14:
        mc.setBlocks(-9, -3, 4,-12, -3, 1,iD, d)
    if n == 15:
        mc.setBlocks(-5, -3, 4, -8, -3, 1,iD,d)
    if n == 16:
        mc.setBlocks(-1, -3, 4, -4, -3, 1,iD,d)

mc.setBlocks(-18, 11, -15, -24, 3, -21, 0) #R
mc.setBlocks(-18, 11, 20,-24, 3, 14,0) #L

mc.setBlocks(-20,11,-12,-20, -1, 11, WOOL, BLACK) #border
mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, WHITE)
mc.setBlocks(-21,12,-10,-21, 12 + lHeight, 10, 0) # clear lazers (sholud replacew this with some form of clear everything)

mc.setBlocks(-1 - 3,-1,-1,1 - 3,-1,1,1) #platform
mc.player.setPos(-3,0,0) # tp player to platform

# startup questionare
mc.setBlock(-1 - 4,0,0,WOOL, 5)
mc.postToChat("break the green wool to start fire")
while (mc.getBlock(-1 - 4,0,0) == WOOL):
    time.sleep(0.25) #distract the cpu



startSong()

# i dont understand functions enough so here is mess:
for k in range(2):
    if True:
        for j in range(4):
            for i in range(16):
                mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
                WAIT(halfNote)
                print(j)
    i = 0
    k = 9
    buildSpeaker()
    for j in range(16):

        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)

        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)

        i += 1
        k += 1
        print(j)

    lean = 80
    for j in range(4):

        #1
        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        lazer(5,GLOWSTONE,5)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)

        #2
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #3
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #4
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)

        #5
        i += 1
        k += 1
        print(j)
        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        lazer(5,WOOL,5)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)

        #6
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #7
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        lazer(5,GLOWSTONE,5)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #8
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        lazer(5,WOOL,5)
        WAIT(halfNote)
        
        #9
        i += 1
        k += 1
        print(j)
        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        lazer(4,GLOWSTONE,5)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)

        #10
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #11
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #12
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        lazer(4,WOOL,5)
        lazer(3,GLOWSTONE,5)
        WAIT(halfNote)

        #13
        i += 1
        k += 1
        print(j)
        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)
        
        #14
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #15
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #16
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)

        #17
        i += 1
        k += 1
        print(j)

        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)

        #18
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #19
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #20
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)

        #21
        i += 1
        k += 1
        print(j)
        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)

        #22
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #23
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #24
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #25
        i += 1
        k += 1
        print(j)
        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)

        #26
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #27
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #28
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)

        #29
        i += 1
        k += 1
        print(j)
        tweeters((GLOWSTONE,15))
        if i == 16: i = 0
        if k > 16: k = 9
        pad(k,WOOL, 0)
        if k == 9:
            pad(16,WOOL,1)
        else:
            pad(k - 1,WOOL,5)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(tinyNote)
        tweeters((SSANDSTONE))
        WAIT(halfNote - tinyNote)
        
        #30
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 2)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        
        #31
        drivers((GLOWSTONE,15))
        i += 1
        k += 1
        pad(k,WOOL, 0)
        pad(k - 1,WOOL, 3)
        WAIT(tinyNote)
        drivers((SSANDSTONE))
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote - tinyNote)

        #32
        i += 1
        k += 1
        pad(k,WOOL,0)
        pad(k - 1,WOOL, 4)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)

        #
        i += 1
        k += 1
        print(j)

    for j in range(24):
        i = 0
        print(j)
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, )
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, GLOWSTONE, i)
        WAIT(halfNote)
        i += 1
        mc.setBlocks(-20,10,-11,-20, 0, 10, WOOL, i)
        WAIT(halfNote)
    startSong()

