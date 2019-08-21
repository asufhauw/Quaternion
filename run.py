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
    while exit != 'y':

        angle = input('enter angle in degrees: ')
        angle = float(angle)
        axis = input('enter axis (e.g 0,0,1 to rotate in Z: ')
        axis = tuple(float(axis.strip()) for axis in axis.split(',')) 
        print(axis)
        r = 2.0*math.pi/360.0 * angle

        x = get_quaternion(r,axis)
        print('q = {}'.format(x))
        point = rotate(x,(1,0,0))
        point = (point[1],point[2],point[3])
        screen.X_Axis = point
        point = rotate(x,(0,1,0))
        point = (point[1],point[2],point[3])
        screen.Y_Axis = point
        point = rotate(x,(0,0,1))
        point = (point[1],point[2],point[3])
        screen.Z_Axis = point 
        print('x: {}'.format(screen.X_Axis))
        print('y: {}'.format(screen.Y_Axis))
        print('z: {}'.format(screen.Z_Axis))
        
        screen.paint()
        
        exit = input('wanna exit (y/n)?: ')
    
