import math
def get_quaternion(angle, axis):
    '''
        angle : rotation angle in radians
        axis : (x,y,z) rotation axis
    '''
    if len(axis) != 3:
        # error
        return 
    r = math.cos(angle/2.0)
    i = axis[0] * math.sin(angle/2.0)
    j = axis[1] * math.sin(angle/2.0)
    k = axis[2] * math.sin(angle/2)
    return (r, i, j, k)

def rotate(q, point):
    '''
        Pout = q * Pin * conj(q)
    '''
    if len(q) != 4 or len(point) != 3:
        # ERROR return 
        return
    p1 = (0, point[0], point[1], point[2])
    
    q1 = mul(q,p1)
    p2 = mul(q1,conj(q))
    return p2

def conj(q):
    return (q[0], -1*q[1], -1*q[2], -1*q[3])

def length(q):
    return math.sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3])

def normalise(q):
    l = length(q)
    return (q[0]/l, q[1]/l, q[2]/l, q[3]/l)

def mul(q1, q2):
    a = q1[0]
    b = q1[1]
    c = q1[2]
    d = q1[3]

    e = q2[0]
    f = q2[1]
    g = q2[2]
    h = q2[3]

    r = a*e - b*f - c*g - d*h
    i = b*e + a*f + c*h - d*g
    j = a*g - b*h + c*e + d*f
    k = a*h + b*g - c*f + d*e
    return (r, i, j, k)

def add(q1, q2):
    return (q1[0]+q2[0],q1[1]+q2[1],q1[2]+q2[2])

def diff(q1, q2):
    return (q1[0]-q2[0],q1[1]-q2[1],q1[2]-q2[2])


def reflect():
    pass

