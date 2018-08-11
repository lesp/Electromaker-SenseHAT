from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()



while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
    if pitch > 254:
        pitch = 254
    if pitch < 1:
        pitch = 0
    if roll > 254:
        roll = 254
    if roll < 1:
        roll = 0
    if yaw > 254:
        yaw = 254
    if yaw < 1:
        yaw = 0
    sense.clear(int(pitch),int(roll),int(yaw))
    sleep(0.1)
