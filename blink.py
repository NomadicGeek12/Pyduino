from pyfirmata import Arduino, util
import time

board = Arduino('COM3')
while True:
    board.digital[13].write(0)
    time.sleep(1)
    board.digital[13].write(1)
    time.sleep(1)
board.exit()
