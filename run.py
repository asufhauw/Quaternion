#/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from display import Display
from quaternion import *
def deg2rad(deg):
    return 2.0*math.pi/360.0 * deg

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
        q_1 = input('enter your quaternion(default 1,0,0,0): ')
        q_1 = tuple(float(q_1.strip()) for q_1 in q_1.split(','))
        print(axis)
        print('{},{},{},{}'.format(q_1[0],q_1[1],q_1[2],q_1[3]))
        x = quat(deg2rad(angle),axis)
        x = mul(q_1,x)
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
        while not screen.WaitInput:
            screen.paint()
        exit = input('wanna exit (y/n)?: ')
        screen.WaitInput = False
    
