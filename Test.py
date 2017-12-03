try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges.")

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN) ## make sure this is # on pinout diagram
GPIO.setup(18, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(18, GPIO.IN)

## set default inputs to 0
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

## check default inputs
if GPIO.input(17):
    print("Pin 11 is starting HIGH") // run this animation
else:
    print("Pin 11 is starting LOW") // run that animation

if GPIO.input(17):
    print("Pin 11 is starting  HIGH") // run this animation
else:
    print("Pin 11 is starting  LOW") // run that animation

if GPIO.input(17):
    print("Pin 11 is starting HIGH") // run this animation
else:
    print("Pin 11 is starting LOW") // run that animation

if GPIO.input(17):
    print("Pin 11 is starting HIGH") // run this animation
else:
    print("Pin 11 is starting LOW") // run that animation

## Check for change in values that should be 0 --> 1

GPIO.wait_for_edge(##, GPIO.RISING)

print("Pin ## and pin ## both went high!")

GPIO.wait_for_edge(##, GPIO.RISING)

print("Pin ## and pin ## both went high!")

## pull values back down & check
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

## check newer inputs
if GPIO.input(17):
    print("Pin 11 is now HIGH") // run this animation
else:
    print("Pin 11 is now LOW") // run that animation

if GPIO.input(17):
    print("Pin 11 is now HIGH") // run this animation
else:
    print("Pin 11 is LOW") // run that animation

if GPIO.input(17):
    print("Pin 11 is now HIGH") // run this animation
else:
    print("Pin 11 is now LOW") // run that animation

if GPIO.input(17):
    print("Pin 11 is now HIGH") // run this animation
else:
    print("Pin 11 is now LOW") // run that animation

