from communication.server.server import MountainServer
from communication.server.mountain.easy_mountain import EasyMountain
s = MountainServer(EasyMountain(1,10),(14000,14000),50,191.234.202.2,8080)
s.start()