from mcpi import minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


import time
import math
BRICK = 45
SSANDSTONE = 24,2
GLOWSTONE = 89
WOOL = 35
BRICK = 45
SSANDSTONE = 24,2
OBSIDIAN = 15

print(str(pos.x) + ", " + str(pos.y - 1) + ", " + str(pos.z))
for i in range(5):
    mc.postToChat(i)
    time.sleep(1)
pos = mc.player.getTilePos()
print(str(pos.x) + ", " + str(pos.y - 1) + ", " + str(pos.z))
mc.setBlocks(-20, 12, -11 - 1,-20, 12, -11 + 1, 20)
mc.setBlocks(-20, 12, 10 - 1,-20, 12, 10 + 1, 20)
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


#mc.setBlocks(-100, -50, -100, 100, 50 , 100, 0)  # clear everything
def sin(t):
    return math.sin(math.radians(t))
def cos(t):
    return math.cos(math.radians(t))


length = 50
lean = 10

def lazer(n, iD):
    if ((lean > 45) and (lean < 135)):
        resolution = 5
    else:
        resolution = 1
    if (n <= 4):
        line(Vector(-20, 13, -11),Vector(
            -20 + length * cos(lean),
            13 + length * sin(lean) * sin(144 - (18 * n)),
            -11 + length * cos(144 - (18 * n)))
            , WOOL, iD + 1 , resolution)
        
        mc.setBlocks(-20, 12, -11 - 1,-20, 12, -11 + 1, 20)
    else:
        line(Vector(-20, 12, 10),Vector(
            -20 + length * cos(lean),
            13 + length * sin(lean) * sin(180 - (18 * n)),
            -11 + length * cos(180 - (18 * n)))
            , WOOL, iD + 1 , resolution)
        mc.setBlocks(-20, 12, 10 - 1,-20, 12, 10 + 1, 20)

    print(resolution)
    print(lean)

def pad(n, iD):
    if n == 1:
        mc.setblocks(-16, -2, -8, -14, -2, -6,iD)
        mc.setblocks(-16, -1, -12, -14, 1, -12,iD)
    if n == 2:
        mc.setblocks(-12, -2, -8, -10, -2, -6,iD)
        mc.setblocks(-12, -1, -12, -10, 1, -12,iD)
    if n == 3:
        mc.setblocks(-8, -2, -8, -6, -2, -6,iD)
        mc.setblocks(-8, -1, -12, -6, 1, -12,iD)
    if n == 4:
        mc.setblocks(-4, -2, -8, -2, -2, -6,iD)
        mc.setblocks(-4, -1, -12, -2, 1, -12,iD)
    if n == 5:
        mc.setblocks(-16, -2, 8, -14, -2, 6,iD)
        mc.setblocks(-16, 1, 12, -14, -1, 12,iD)
    if n == 6:
        mc.setblocks(-12, -2, 6, -10, -2, 8,iD)
        mc.setblocks(-12, 1, 12, -10, -1, 12,iD)
    if n == 7:
        mc.setblocks(-8, -2, 8, -6, -2, 6,iD)
        mc.setblocks(-8, 1, 12, -6, -1, 12,iD)
    if n == 8:
        mc.setblocks(-4, 1, 12, -2, -1, 12,iD)
        mc.setblocks(-4, -2, 8, -2, -2, 6,iD)
    if n == 9:
        mc.setblocks(-16, -3, -1, -13, -3, -4,iD)
    if n == 10:
        mc.setblocks(-12, -3, -1, -9, -3, -4,iD)
    if n == 11:
        mc.setblocks(-8, -3, -1, -5, -3, -4,iD)
    if n == 12:
        mc.setblocks(-1, -3, -4, -4, -3, -1,iD)
    if n == 13:
        mc.setblocks(-13, -3, 4, -16, -3, 1,iD)
    if n == 14:
        mc.setblocks(-9, -3, 4,-12, -3, 1,iD)
    if n == 15:
        mc.setblocks(-5, -3, 4, -8, -3, 1,iD)
    if n == 16:
        mc.setblocks(-1, -3, 4, -4, -3, 1,iD)


#for i in range(10):
#    lazer(0, i)
