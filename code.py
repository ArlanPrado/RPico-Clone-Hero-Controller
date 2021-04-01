# Raspberry Pi Pico Keyboard Controller for Clone Hero
# Using CircuitPython 6.2.0-beta.4
# Using Adafruit USB_HID Library

"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio
import usb_hid

from adafruit_hid.gamepad import Gamepad

# checks if the pico is connected, could be removed later

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

for x in range(0, 5):
    led.value = False
    time.sleep(0.1)
    led.value = True
    time.sleep(0.1)

gamepad = Gamepad(usb_hid.devices)

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

# maybe use an list of buttons instead of this jumbled if-else mess
while True:
    #Fret Buttons,
    if btn_green.value:
        gamepad.press_buttons(1)
    if btn_green.value is False:
        gamepad.release_buttons(1)
    if btn_red.value:
        gamepad.press_buttons(2)
    if btn_red.value is False:
        gamepad.release_buttons(2)
    if btn_yellow.value:
        gamepad.press_buttons(3)
    if btn_yellow.value is False:
        gamepad.release_buttons(3)
    if btn_blue.value:
        gamepad.press_buttons(4)
    if btn_blue.value is False:
        gamepad.release_buttons(4)
    if btn_orange.value:
        gamepad.press_buttons(5)
    if btn_orange.value is False:
        gamepad.release_buttons(5)
    #Strum Bar
    #consider using time.sleep
    if btn_up.value:
        gamepad.press_buttons(6)
    if btn_up.value is False:
        gamepad.release_buttons(6)
    if btn_dn.value:
        gamepad.press_buttons(7)
    if btn_dn.value is False:
        gamepad.release_buttons(7)
