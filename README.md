# SENSE HAT APP
Run your custom scripts by the joystick to choose which one.And show the information on the LED matrix.It be design like to Linux file system that show color of filename like the Ubuntu.

## How to run
1. install python3
2. install sense hat library
3. create `entry/` folder reference [Use example entry](#1-use-example-entry)
4. run it `python src/index.py`

## Operation method
The LED matrix show now foucs(filename).
Use the joystick to change your foucs.

The direction table:
| direction | action                                  |
| :-------: | :-------------------------------------- |
|   right   | entry the folder                        |
|   left    | leave the folder                        |
|    up     | choose the previous file in same folder |
|   down    | choose the next file in same folder     |
|  middle   | execute the script                      |


## LED matrix color means
The focus show different color by filetype.
Your can change it at `src/color.py`.

The default color:
| color  | description            |
| :----: | :--------------------- |
|  blue  | folder                 |
| green  | execute file           |
| white  | normal file            |
| purple | result of execute file |

## Entry folder
I show you two methods create your tree of scripts.The root folder of scripts named `entry`.

### 1. Use example Entry
Run the command `ln -s ./example/entry ./entry` at project directory.
The `entry/` folder be create(link to `./example/entry` folder) at project directory.

### 2. Custom your Entry
Create the `entry/` folder at project directory.
Put your scripts or folder in here.

## Scripts
The show the script stdout on LED Matrix.

## Linux boot automatically

### 1. systemd
Reference `example/systemd/senseHat.service`

## PR
Welcome~

## AUTHOR
BYS(dan3612812@gmail.com)
