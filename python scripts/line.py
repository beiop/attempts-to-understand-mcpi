from mcpi import minecraft
from mcpi import block
#attempt to remove holes in the line by useing brute force
resolution = 10

#create connection to minecraft
mc = minecraft.Minecraft.create()

#determine the position of player
playerTilePos1 = mc.player.getTilePos()

#determine the type of block below the player at that positon
Block = mc.getBlockWithData(playerTilePos1.x, playerTilePos1.y - 1, playerTilePos1.z)

input("pos one recoreded, press entre when at pos 2")

#determine the position of player again for the second position
playerTilePos2 = mc.player.getTilePos()

#find the line of y=mx+b
y_slope = (playerTilePos1.y - playerTilePos2.y) / (playerTilePos1.x - playerTilePos2.x)
y_b = playerTilePos1.y - (playerTilePos1.x * y_slope)

#find the line of z=mx+b
z_slope = (playerTilePos1.z - playerTilePos2.z) / (playerTilePos1.x - playerTilePos2.x)
z_b = playerTilePos1.z - (playerTilePos1.x * z_slope)

#point the line in the right direction
if playerTilePos2.x > playerTilePos1.x:
    m = 1
elif playerTilePos2.x < playerTilePos1.x:
    m = -1
else:
    print("sorry, drawing straight lines on the x axis currently isn't supported.")

#start line at deh begining
x = playerTilePos1.x

#continue drawing line till you reach dah end
while round(x,1) != playerTilePos2.x:
    mc.setBlock(x, x * y_slope + y_b, x * z_slope + z_b, Block)
    x += (m / resolution)