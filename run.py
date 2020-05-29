#/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from display import Display
from quaternion import *

# Test.. Todo: Add unit test
W, H = 640, 480
DoTest=False
if __name__ == '__main__':
    if DoTest: Test()
    exit = ''
    screen = Display(W,H) 
    while(1):
        screen.paint()
