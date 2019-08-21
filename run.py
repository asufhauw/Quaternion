#/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
from display import Display
from quaternion_v2 import *

# Test.. Todo: Add unit test
W, H = 640, 480
DoTest=False
if __name__ == '__main__':
    if DoTest: Test()
    x = get_quaternion(math.pi/2.0,(0,0,1))
    screen = Display(W,H)
    print(x)
    point = rotate(x,(1,0,0))
    point = (point[1],point[2],point[2])
    screen.X_Axis = point
    point = rotate(x,(0,1,0))
    point = (point[1],point[2],point[2])
    screen.Y_Axis = point
    point = rotate(x,(0,0,1))
    point = (point[1],point[2],point[2])
    screen.Z_Axis = (0,0,1) 
    print(screen.X_Axis)
    print(screen.Y_Axis)
    print(screen.Z_Axis)
    while 1:
        screen.paint()
        
    '''
    q1 = ()
    q2 = ()
    while(0):
        print('Enter a quaterion, using following format: ({i},{j},{k}),{rot}')
        in_val = input()
        q1 = Calc_Quaternions(in_val[0],in_val[1])

        print('Enter new quaterion, using following format: ({i},{j},{k}),{rot}')
        in_val = input()
        q2 = Calc_Quaternions(in_val[0],in_val[1])
        
        print('Multiplying the two quaterions we get the following:')
        Mul_Quaternions(q1,q2)
    '''
