from mcpi.minecraft import Minecraft
import time, random
mc = Minecraft.create()

while True:
	x=random.randint(-1000, 1000)
	y=random.randint(0, 200)
	z=random.randint(-1000, 1000)
	
	time.sleep(3)
	mc.player.setTilePos(x, y, z)
	mc.setBlock(x, y-1, z, 46)
	
	
	
