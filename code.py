# Raspberry Pi Pico Keyboard Controller for Clone Hero
# Using CircuitPython 6.2.0-beta.4
# Using Adafruit USB_HID Library

# import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

#frets
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

#strum bar
btn_up = digitalio.DigitalInOut(board.GP14)
btn_up.direction = digitalio.Direction.INPUT
btn_up.pull = digitalio.Pull.DOWN

btn_dn = digitalio.DigitalInOut(board.GP15)
btn_dn.direction = digitalio.Direction.INPUT
btn_dn.pull = digitalio.Pull.DOWN

#checks if the pico is connected, could be removed later
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

while True:
    #Fret Buttons,
    if btn_green.value:
        keyboard.press(Keycode.ONE)
    if btn_green.value is False:
        keyboard.release(Keycode.ONE)
    if btn_red.value:
        keyboard.press(Keycode.TWO)
    if btn_red.value is False:
        keyboard.release(Keycode.TWO)
    if btn_yellow.value:
        keyboard.press(Keycode.THREE)
    if btn_yellow.value is False:
        keyboard.release(Keycode.THREE)
    if btn_blue.value:
        keyboard.press(Keycode.FOUR)
    if btn_blue.value is False:
        keyboard.release(Keycode.FOUR)
    if btn_orange.value:
        keyboard.press(Keycode.FIVE)
    if btn_orange.value is False:
        keyboard.release(Keycode.FIVE)
    #Strum Bar
    #consider using time.sleep
    if btn_up.value:
        keyboard.press(Keycode.UP_ARROW)
    if btn_up.value is False:
        keyboard.release(Keycode.UP_ARROW)
    if btn_dn.value:
        keyboard.press(Keycode.UP_ARROW)
    if btn_dn.value is False:
        keyboard.release(Keycode.UP_ARROW)



