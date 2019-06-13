#/usr/bin/python3
import math
import pygame
def Calc_Quaternions(ijk,rot):
    '''
        calculate the Quaternions,
        set the rot in angles
        i, j and k is what axis you want to rotate in
    '''
    a = rot*math.pi*2/360 # convert rot to radians
    i,j,k=ijk
    r = math.cos(a/2)
    i = i*math.sin(a/2)
    j = j*math.sin(a/2)
    k = k*math.sin(a/2)
    assert(r**2+i**2+j**2+k**2 == 1.0)
    print('{0} + {1}i + {2}j + {3}k'.format(r,i,j,k))
    return r,i,j,k

def Mul_Quaternions(q1,q2):
    '''
        Multiply two quaternions,

        real = r1*r2 - i1*i2 - j1*j2 - k1*k2
        i    = i1*r2 + j1*k2 - k1*j2 + r1*i2
        j    = r1*j2 + k1*i2 - i1*k2 + j1*r2 
        k    = r1*k2 + i1*j2 - j1*i2 + k1*r2
    '''
    r1,i1,j1,k1=q1
    r2,i2,j2,k2=q2
    real = r1*r2 - i1*i2 - j1*j2 - k1*k2
    i    = i1*r2 + j1*k2 - k1*j2 + r1*i2
    j    = r1*j2 + k1*i2 - i1*k2 + j1*r2
    k    = r1*k2 + i1*j2 - j1*i2 + k1*r2
    assert(real**2+i**2+j**2+k**2 == 1.0)
    print('{0} + {1}i + {2}j + {3}k'.format(real,i,j,k))
    return real,i,j,k

def Test():
    check = (1,0,0,0)
    assert(Calc_Quaternions((0,0,0),0)==check)
    assert(Calc_Quaternions((0,1,0),0)==check)
    assert(Calc_Quaternions((0,0,1),0)==check)
    check = (0.7071067811865476, 0.7071067811865475, 0.0, 0.0)
    assert(Calc_Quaternions((1,0,0),90)==check)
    check = (0.7071067811865476, 0.0, 0.7071067811865475, 0.0)
    assert(Calc_Quaternions((0,1,0),90)==check)
    check = (0.7071067811865476, 0.0, 0.0, 0.7071067811865475)
    assert(Calc_Quaternions((0,0,1),90)==check)

    check = (0.5000000000000001, 0.5, 0.5, 0.4999999999999999)
    assert(Mul_Quaternions(Calc_Quaternions((1,0,0),90),Calc_Quaternions((0,1,0),90)) == check)
    return
DoTest=True
if __name__ == '__main__':
    if DoTest: Test()
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

