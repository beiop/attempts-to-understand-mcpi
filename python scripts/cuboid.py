from mcpi import minecraft
from mcpi import block

#create connection to minecraft
mc = minecraft.Minecraft.create()

#determine the position of player
playerTilePos1 = mc.player.getTilePos()

#determine the type of block below the player at that positon
Block = mc.getBlockWithData(playerTilePos1.x, playerTilePos1.y - 1, playerTilePos1.z)

input("pos one recoreded, press entre when at pos 2")

#determine the position of player again for the second position
playerTilePos2 = mc.player.getTilePos()


#fill that space in. I was about to write a huge for loop but then i found
mc.setBlocks(playerTilePos1,playerTilePos2,Block)