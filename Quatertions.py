#/usr/bin/python2.7
import math

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def Quaternions2Euler(q):
    w,x,y,z = q
    roll = math.atan2(2*(w*x+y*z),1-2*(x*x+y*y))*360.0/(2*math.pi)
    pitch = math.asin(2*(w*y-z*x))*360.0/(2*math.pi)
    yaw = math.atan2(2*(w*z+x*y),1-2*(y*y+z*z))*360/(2*math.pi)
    print('euler rotation: ({},{},{})'.format(roll,pitch,yaw))
    return roll,pitch,yaw

def GetOtherQuaternion(q):
    r,i,j,k = q
    r = r*-1
    i = i*-1
    j = j*-1
    k = k*-1
    print('{0}+{1}i+{2}j+{3}k'.format(r,i,j,k))
    return r,i,j,k

def Calc_Quaternions((i,j,k),rot):
    '''
        calculate the Quaternions,
        set the rot in angles
        i, j and k is what axis you want to rotate in
    '''
    a = rot*math.pi*2/360 # convert rot to radians
    r = math.cos(a/2)
    i = i*math.sin(a/2)
    j = j*math.sin(a/2)
    k = k*math.sin(a/2)
    check = r**2 + i**2 + j**2 + k**2
    assert(isclose(check,1.0))
    print('q = {0} + {1}i + {2}j + {3}k'.format(r,i,j,k))
    return r,i,j,k

def Conj_Q(q):
    r,i,j,k = q
    i = i*-1
    j = j*-1
    k = k*-1
    return r,i,j,k

def normalize(q):
    r,i,j,k = q
    magnitude = math.sqrt(r**2 + i**2 + j**2 + k**2)
    a = r/magnitude
    b = i/magnitude
    c = j/magnitude
    d = k/magnitude
    return a,b,c,d
    

def Mul_Quaternions((r1,i1,j1,k1),(r2,i2,j2,k2)):
    '''
	
        Multiply two quaternions,

        real = r1*r2 - i1*i2 - j1*j2 - k1*k2
        i    = i1*r2 + j1*k2 - k1*j2 + r1*i2
        j    = r1*j2 + k1*i2 - i1*k2 + j1*r2 
        k    = r1*k2 + i1*j2 - j1*i2 + k1*r2
    '''
    real = r1*r2 - i1*i2 - j1*j2 - k1*k2
    i    = i1*r2 + j1*k2 - k1*j2 + r1*i2
    j    = r1*j2 + k1*i2 - i1*k2 + j1*r2
    k    = r1*k2 + i1*j2 - j1*i2 + k1*r2
    check = real**2 + i**2 + j**2 + k**2
 #   print('{}'.format(check))
#    assert(isclose(check,1.0))
    print('{0} + {1}i + {2}j + {3}k'.format(real,i,j,k))
    return real,i,j,k

def Pout(q,pin):
    '''
	NEW POINT

        Multiply two quaternions,

        real = r1*r2 - i1*i2 - j1*j2 - k1*k2
        i    = i1*r2 + j1*k2 - k1*j2 + r1*i2
        j    = r1*j2 + k1*i2 - i1*k2 + j1*r2 
        k    = r1*k2 + i1*j2 - j1*i2 + k1*r2
    '''
    r1,i1,j1,k1 = q
    i2,j2,k2 = pin
    print('Pin: {}x + {}y + {}z'.format(i2,j2,k2))
    assert(isclose(r1**2+i1**2+j1**2+k1**2,1))
    conj_q = Conj_Q((r1,i1,j1,k1))
    check = conj_q[0]**2+conj_q[1]**2+conj_q[2]**2+conj_q[3]**2
    assert(isclose(check,1))
    real = (-1)*i1*i2 - j1*j2 - k1*k2
    i    = j1*k2 - k1*j2 + r1*i2
    j    = r1*j2 + k1*i2 - i1*k2 
    k    = r1*k2 + i1*j2 - j1*i2
    print('q*pin = {} + {}i + {}j + {}k'.format(real,i,j,k))
    real,i,j,k = Mul_Quaternions((real,i,j,k),conj_q)
    print('Pout: {0} + {1}i + {2}j + {3}k'.format(real,i,j,k))
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

DoTest=False
if __name__ == '__main__':
    if DoTest: Test()
    q = (-1,0,0,0)#Calc_Quaternions((0,1,0),140)
  '''  
    Quaternions2Euler(q)
    pout = Pout(q,(2,3,0)) 
    print('{}'.format(pout))
    q1 = ()
    q2 = ()
    Mul_Quaternions(q,Calc_Quaternions((1,0,0),90))
    while(1):
        print('Enter a quaterion, using following format: ({i},{j},{k}),{rot}')
        in_val = input()
	
        #q1 = Calc_Quaternions(in_val[0],in_val[1])

        print('Enter new quaterion, using following format: ({i},{j},{k}),{rot}')
        #in_val = input()
        #q2 = Calc_Quaternions(in_val[0],in_val[1])
        
        print('Multiplying the two quaterions we get the following:')
        #Mul_Quaternions(q1,q2)

'''