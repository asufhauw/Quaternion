import math
import glm
def quat(angle, axis):
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

def norm(q):
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

def quat2Euler(q):
    norm_q = normalize(q)
    
    pass
def quat2Mat4(q):
    """1 - 2*qy2 - 2*qz2  2*qx*qy - 2*qz*qw   2*qx*qz + 2*qy*qw
    2*qx*qy + 2*qz*qw   1 - 2*qx2 - 2*qz2   2*qy*qz - 2*qx*qw
    2*qx*qz - 2*qy*qw   2*qy*qz + 2*qx*qw   1 - 2*qx2 - 2*qy2"""
    import math
    rows, cols = (4,4)
    arr = [[0.0 for i in range(cols)] for j in range(rows)] 
    qw = q[0]
    qw2 = math.pow(qw,2)#qw**2
    qx = q[1]
    qx2 = math.pow(qx,2)#qx**2
    qy = q[2]
    qy2 = math.pow(qy,2)#qy**2
    qz = q[3]
    qz2 = math.pow(qz,2)#qz**2
    arr[0][0] = 1 - 2*(qy2 + qz2)
    arr[0][1] = 2*(qx*qy - qz*qw)
    arr[0][2] = 2*(qx*qz + qy*qw)
    arr[0][3] = 0
    arr[1][0] = 2*(qx*qy + qz*qw)
    arr[1][1] =  1 - 2*qx2 - 2*qz2
    arr[1][2] = 2*qy*qz - 2*qx*qw 
    arr[1][3] = 0
    arr[2][0] = 2*qx*qz - 2*qy*qw 
    arr[2][1] =  2*qy*qz + 2*qx*qw 
    arr[2][2] =  1 - 2*qx2 - 2*qy2
    arr[2][3] = 0
    arr[3][0] = 0
    arr[3][1] = 0
    arr[3][2] = 0
    arr[3][3] = 1
    return arr

def reflect():
    pass

if __name__ == '__main__':
    assert(quat2Mat4((1,0,0,0))           == [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    assert(quat2Mat4((-1,0,0,0))          == [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    assert(quat2Mat4((0.7071,0,0.7071,0)) == [[0,0,1,0],[0,1,0,0],[-1,0,0,0],[0,0,0,1]])
    assert(quat2Mat4((0.7071,0.7071,0,0)) == [[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]])
