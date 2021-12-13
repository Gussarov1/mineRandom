import keyboard
import mouse
import random

min = 6
max = 9
mode_on = True


def event_mouse(event):
    global mode_on
    if mode_on:
        if isinstance(event, mouse.ButtonEvent):
            if event.button == 'right':
                random_number = str(random.randint(min, max))
                print(random_number)
                keyboard.press(random_number)


def event_keyboard():
    global mode_on
    if keyboard.is_pressed('x'):
        mode_on = True
        print("ON")
    elif keyboard.is_pressed('c'):
        mode_on = False
        print("OFF")


mouse.hook(event_mouse)
keyboard.hook(event_keyboard)
keyboard.wait("z")
