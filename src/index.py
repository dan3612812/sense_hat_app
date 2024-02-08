#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from time import *
from os.path import abspath, dirname
import subprocess

from sense_hat import SenseHat
from color import *
from Trace import Trace

# base env
dir = dirname(abspath(__file__))
entryPoint = "%s/../entry" % dir

# global variable
interruptMsg = None


def up(event) -> None:
    if event.action == "released":
        trace.up()


def down(event) -> None:
    if event.action == "released":
        trace.down()


def left(event) -> None:
    if event.action == "released":
        trace.pop()


def right(event) -> None:
    if event.action == "released":
        trace.append()


def middle(event) -> None:
    global interruptMsg
    if event.action == "released":
        if trace.peek().type == 2:
            target = "%s/%s" % (trace.peek().parentPath, trace.peek().name)
            result = subprocess.run(
                [target], stdout=subprocess.PIPE).stdout.decode('utf-8')
            result = "EMPTY" if result == '' else result
            if interruptMsg == None:
                if result == '':
                    interruptMsg = "None"
                else:
                    interruptMsg = result


def mappingTextColor(filetype: int):
    if filetype == 0:
        return folderColor
    elif filetype == 1:
        return fileColor
    elif filetype == 2:
        return execFileColor
    else:
        return yellow


if __name__ == "__main__":
    sense = SenseHat()
    trace = Trace(rootFolder=entryPoint)

    # bind joystick
    sense.stick.direction_up = up
    sense.stick.direction_down = down
    sense.stick.direction_left = left
    sense.stick.direction_right = right
    sense.stick.direction_middle = middle

    try:
        while True:
            if interruptMsg == None:
                name = trace.peek().name
                # trace.peek().print()
                textColor = mappingTextColor(trace.peek().type)
                sense.show_message(name, scroll_speed=0.05,
                                   text_colour=textColor)
            else:
                sense.show_message(
                    interruptMsg, scroll_speed=0.05, text_colour=resultColor)
                interruptMsg = None
            sleep(0.01)
    except KeyboardInterrupt:
        sense.clear()
        print("keyboard interrupt")
