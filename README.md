# Auto Car Racing
Online Convex Optimisation on Car Racing
## Install
```
git clone https://github.com/harsharora21/OCO-Car-Racing.git
cd OCO-Car-Racing
chmod +x install.sh run.sh
./install.sh
```
### Running
```
./run.sh
```
## How To Play
Hold the M key, now use WASD to move (while holding M key). This will train the Model.
For running the Model just take hands off the keyboard.

If Model goes haywire you can intervene by holding the M key and guiding it.

## Controls
W - Forward

S - Back

A - Left

D - Right

Q - Quit

M (Hold) - Train

X - Get a plot of what model is seeing

R - Reset the game (Does not reset the model)

## How does it Work?
Uses Online Convex Optimisation. 

## An Image
![Alt text](GameImage.png?raw=true "Game Image" )

## Notes
1. This game captures keyboard even when not in focus.

2. The install script was tested on Mac. It should work fine on Linux.

3. For some reason sometimes install does not work. The error is something related to Gym Box2D. In that case delete the gamevenv folder and run install.sh again.

## TODO
Expand Docs

Fix keyboard code
