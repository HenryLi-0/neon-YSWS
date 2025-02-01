import time
import random
import board
import displayio
import framebufferio
import rgbmatrix
import terminalio
import math
from adafruit_display_text import label

displayio.release_displays()

def getTime():
    return time.strftime("%I:%M %p", time.localtime(time.time()))

# matrix setup woo
matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1)

display = framebufferio.FramebufferDisplay(matrix, auto_refresh=False)
b1 = displayio.Bitmap(display.width, display.height, 2)
g1 = displayio.Group(scale=1)

# imagery bitmap
bitmap1 = displayio.OnDiskBitmap("sky.bmp")
bitmap2 = displayio.OnDiskBitmap("water.bmp")
bitmap3 = displayio.OnDiskBitmap("beach.bmp")

# tilegrid
tilegrid1 = displayio.TileGrid(bitmap1, pixel_shader=bitmap1.pixel_shader)
tilegrid1.x = 0
tilegrid1.y = 0
tilegrid2 = displayio.TileGrid(bitmap2, pixel_shader=bitmap2.pixel_shader)
tilegrid2.x = 0
tilegrid2.y = 14
tilegrid3 = displayio.TileGrid(bitmap3, pixel_shader=bitmap3.pixel_shader)
tilegrid3.x = 0
tilegrid3.y = 19

g1.append(tilegrid1)
g1.append(tilegrid2)
g1.append(tilegrid3)

text_group = displayio.Group(scale=1)
text = label.Label(terminalio.FONT, text=getTime(), color=0xFFFFFF)
text.x = 2
text.y = 5
text_group.append(text)
g1.append(text_group)

display.root_group = g1
print("done")
while True:
    text.text = getTime()
    display.auto_refresh = True
    display.refresh()
    tilegrid2.y = round(math.sin(time.time())*1.5 + 14)
    time.sleep(0.1)