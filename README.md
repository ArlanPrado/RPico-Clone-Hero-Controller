# Raspberry Pico Guitar Hero Controller
 Clone/Guitar Hero guitar controller made with using Raspberry Pi Pico and CircuitPython. Make anything a Guitar Hero controller!

CircuitPython v6.2.0-rc.0 + adafruit_hid library


## Instructions

1. Connect your Raspberry Pico to your pc and load into it CircuitPython.

2. Have code.py and adafruit_hid library downloaded. Load code.py into circuitpy and adafruit_hid into the "lib" folder.

[If you don't care about configuring the whammy and joystick skip this step]

3. Make sure the Pico has the Male Pin Header Connectors to connect your analog sticks and buttons. Open up the Guitar Hero guitar and check your values of the joystick and the whammy bar. For maximum usage of the whammy and joystick, modify the gamepad.move_joysticks values set in the while loop to your liking. Here's an example of how to modify the joysticks:

Enter statement "print(ana_whammy.value)" and "time.sleep(0.1)"
If the "zero" value of whammy bar is 31,000 then go down to at least 30,000 in the next operation.
Next "print(ana_whammy.value-30,000)"
If the maximum value of the whammy bar is around 24,000 go to at most 25,000.
You should have (ana_whammy.value-30000)/25000. Replace the previous value with this operation.

**NOTE: The gamepad.move_joysticks values must be between -127 to 127, the code will not run if the values are outside this range. If you are getting this error, comment out the line and configure your joysticks as said in step 3**

Make sure to save the code! The pico should light up if it works.

4. Connect your Pico with the controller buttons and analog sticks you want to use (pico diagram is included). Basic circuitry knowledge is recommended. Use a soldering iron, solder wick (in case of mistakes), wire (26AWG<), dupont jumper wires (male to female), super glue/hot glue, and switches. I used Kailh Choc Reds for frets and BOX Navies for the strumbar, but keeping the original ALPS switches should be fine too!

5. To test out the controller search "Set Up USB game controllers" on Windows and select CircuitPython HID. You should be able to see all the buttons you connected working.

6. Set up controller in Clone Hero and enjoy!

## Resources

### Library and Driver

[CircuitPython for Pico Download](https://circuitpython.org/board/raspberry_pi_pico/)

[Adafruit CircuitPython HID Library](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases)

### Helpful Resources

[How to Replace Fret Pads with Mechanical Keyswitches!](https://www.youtube.com/watch?v=wVMz653ncTs)

[How to use CircuitPython with Raspberry Pi Pico](https://dronebotworkshop.com/pi-pico-circuitpython/)

[Guitar Hero USB Controller w/Arduino and Java](https://www.instructables.com/Guitar-Hero-USB-Controller-With-Arduino/)
