# Raspberry Pi Pico Keyboard Controller for Clone Hero
# Using CircuitPython 6.2.0-rc.0
# Using Adafruit USB_HID Library

import time
import board
import digitalio
import usb_hid

from adafruit_hid.gamepad import Gamepad
from analogio import AnalogIn
# checks if the pico is connected, could be removed later

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

for x in range(0, 3):
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
    led.value = True

gamepad = Gamepad(usb_hid.devices)

# frets
btn_green = digitalio.DigitalInOut(board.GP2)
btn_green.direction = digitalio.Direction.INPUT
btn_green.pull = digitalio.Pull.DOWN

btn_red = digitalio.DigitalInOut(board.GP3)
btn_red.direction = digitalio.Direction.INPUT
btn_red.pull = digitalio.Pull.DOWN

btn_yellow = digitalio.DigitalInOut(board.GP4)
btn_yellow.direction = digitalio.Direction.INPUT
btn_yellow.pull = digitalio.Pull.DOWN

btn_blue = digitalio.DigitalInOut(board.GP5)
btn_blue.direction = digitalio.Direction.INPUT
btn_blue.pull = digitalio.Pull.DOWN

btn_orange = digitalio.DigitalInOut(board.GP6)
btn_orange.direction = digitalio.Direction.INPUT
btn_orange.pull = digitalio.Pull.DOWN

# strum bar
btn_up = digitalio.DigitalInOut(board.GP7)
btn_up.direction = digitalio.Direction.INPUT
btn_up.pull = digitalio.Pull.DOWN

btn_down = digitalio.DigitalInOut(board.GP8)
btn_down.direction = digitalio.Direction.INPUT
btn_down.pull = digitalio.Pull.DOWN

# misc. buttons
btn_star = digitalio.DigitalInOut(board.GP9)
btn_star.direction = digitalio.Direction.INPUT
btn_star.pull = digitalio.Pull.DOWN

btn_plus = digitalio.DigitalInOut(board.GP10)
btn_plus.direction = digitalio.Direction.INPUT
btn_plus.pull = digitalio.Pull.DOWN

btn_minus = digitalio.DigitalInOut(board.GP11)
btn_minus.direction = digitalio.Direction.INPUT
btn_minus.pull = digitalio.Pull.DOWN

# whammy
ana_whammy = AnalogIn(board.GP26)

# joystick
ana_joy_x = AnalogIn(board.GP28)
ana_joy_y = AnalogIn(board.GP27)

# button dictionary to the gamepad buttons
# current problem: want btn_plus and btn_minus to be the same button press. not possible
#   on dictionary

# cannot put btn as key, must be simple immutable datatype
buttons = {5 : btn_green, 2 : btn_red, 6 : btn_yellow, 1 : btn_blue,
9 : btn_orange, 3 : btn_star, 4 : btn_plus, 7 : btn_minus, 13 : btn_up, 14 : btn_down}

# sets the range from -127 to 127
def setToJoyStickRange(stickVal):
    return int(stickVal * 127 * 2 -127)

# sets a dead zone for the whammy bar
# if the whammy value is below the specified whammy value, then return the specified whammy value
def whammyDeadZone(whammyVal):
    whammyDeadZoneVal = -90
    whammyVal = setToJoyStickRange(whammyVal)
    if(whammyVal < whammyDeadZoneVal):
        return whammyDeadZoneVal
    else:
        return whammyVal

# rounds down the joystick value to the value specified
def roundStickVal(stickVal):
    roundDownVal = 20
    return int(stickVal / roundDownVal) * roundDownVal
while True:
    for gamenum, button in buttons.items():
        if button.value:
            gamepad.press_buttons(gamenum)
        else:
            gamepad.release_buttons(gamenum)

    # the limit on each analog stick is by the first value
    # make limit -127 to 127
    # adjust your joystick until limits are -127 to 127

    gamepad.move_joysticks(
        setToJoyStickRange(ana_joy_x.value/64000),
        setToJoyStickRange(ana_joy_y.value/65000),
        roundStickVal(whammyDeadZone((ana_whammy.value-30000)/25000)),
        None)

    #time.sleep(0.1)
    #print(roundStickVal(whammyDeadZone((ana_whammy.value-30000)/25000)))

