class Quaternion:
    def __init__(self):
        pass

    def __init__(self,r,i,j,k):
       self.q = ['w':r, 'i':i, 'j':j, 'k':k)
       
    def __init__(self,q):
        w = q[0]
        i = q[1]
        j = q[2]
        k = q[3]
        self.q = ['w':w, 'i':i, 'j':j, 'k':k)

    def __init__(self,angle,axis):
        if len(axis) != 3:
            # error
            return 
        r = math.cos(angle/2.0)
        i = axis[0] * sin(angle/2.0)
        j = axis[1] * sin(angle/2.0)
        k = axis[2] * sin(angle/2)
        self.q = ['w':r, 'i':i, 'j':j, 'k':k)

    def __add__(self, q):
        pass

    def __sub__(self, q):
        pass

    def __mul__(self,q):
        a = self.q['w'] 
        b = self.q['i'] 
        c = self.q['j'] 
        d = self.q['k'] 
    
        e = q['w']
        f = q['i']
        g = q['j']
        h = q['k']
    
        r = a*e - b*f - c*g - d*h
        i = b*e + a*f + c*h - d*g
        j = a*g - b*h + c*e + d*f
        k = a*h + b*g - c*f + d*e
        return ['w':r, 'i':i, 'j':j, 'k':k] 

    def rotate(self,point):
        p = ['w':0.0, 'i':point

