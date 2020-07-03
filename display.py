
import numpy as np
import sys
import pygame
import OpenGL
from OpenGL.GL import *
import OpenGL.GL.shaders
from OpenGL.GLU import *
#from quaternion import *
import glm
import array as arr
import quaternion as Quat
import math
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Display():
    points = [glm.vec4(1.0,0.0,0.0,0),glm.vec4(0.0,1.0,0.0,0),glm.vec4(0.0,0.0,1.0,0)]

    def __init__(self, W, H):
        pygame.init()
        self.size = W,H
        self.screen = pygame.display.set_mode(self.size, 
                pygame.DOUBLEBUF|pygame.OPENGL)
        gluPerspective(45,self.size[0]/self.size[1],0.1,50.0)

        gluLookAt(-10,-10,5,0,0,1,0,0,1.0)

    def paint(self):
         # get event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                quat = self.wait_input() 
                self.rotate_axis(quat)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) 
        self.draw_axis()
        pygame.display.flip()
        pygame.time.wait(10)
    point = (1,1,1)

    def wait_input(self):
        cmd = input('waiting for command')
        if cmd == 'd':
            #check what diff between quat
            q_1 = input('enter your quaternion(default 1,0,0,0):')
            q_2 = input('enter second quaternion:')
            q_1 = tuple(float(q_1.strip()) for q_1 in q_1.split(','))
            q_2 = tuple(float(q_2.strip()) for q_2 in q_2.split(','))
            q_diff = Quat.diff(q_1,q_2)
            print('Diff q = {}'.format(q_diff))
            return q_diff
        if cmd == 'e':
            q = input('enter your quat:')
            q = tuple(float(q.strip()) for q in q.split(','))
            euler = Quat.quat2Euler(q)
            print('Euler == {}'.format(euler))
            return q
        else:
            angle = input('enter angle in degrees: ')
            angle = float(angle)
            axis = input('enter axis (e.g 0,0,1 to rotate in Z: ')
            axis = tuple(float(axis.strip()) for axis in axis.split(','))
            q_1 = input('enter your quaternion(default 1,0,0,0): ')
            q_1 = tuple(float(q_1.strip()) for q_1 in q_1.split(','))
            print(axis)
            print('{},{},{},{}'.format(q_1[0],q_1[1],q_1[2],q_1[3]))
            r = 2.0*math.pi/360.0 * angle
            x = Quat.quat(r,axis)
            x = Quat.mul(q_1,x)
            print('q = {}'.format(x))
            return x
    
    def rotate_axis(self, q):
        self.X_Axis = (1,0.0,0.0)
        self.Y_Axis = (0.0,1.0,0.0)
        self.Z_Axis = (0.0,0.0,1.0)
       
        a = Quat.rotate(q,self.X_Axis)
        self.points[0] = glm.vec4(a[1],a[2],a[3],0)
        a = Quat.rotate(q,self.Y_Axis)
        self.points[1] = glm.vec4(a[1],a[2],a[3],0)
        a = Quat.rotate(q,self.Z_Axis)
        self.points[2] = glm.vec4(a[1],a[2],a[3],0)

        print('x: {}'.format(self.points[0]))
        print('y: {}'.format(self.points[1]))
        print('z: {}'.format(self.points[2]))
        
        self.paint()
        
    def draw_axis(self):
        glBegin(GL_LINES)
        # x-axis red color
        glColor3f(RED[0],RED[1],RED[2])
        glVertex3f(0,0,0)
        glVertex3f(self.points[0].x,self.points[0].y,self.points[0].z)
        # y-axis green color
        glColor3f(GREEN[0],GREEN[1],GREEN[2])
        glVertex3f(0,0,0)
        glVertex3f(self.points[1].x,self.points[1].y,self.points[1].z)
        # z-axis blue color
        glColor3f(BLUE[0],BLUE[1],BLUE[2])
        glVertex3f(0,0,0)
        glVertex3f(self.points[2].x,self.points[2].y,self.points[2].z)
        glEnd()

        glBegin(GL_LINES)
        zero = (0,0,2)
        glColor3f(RED[0],RED[1],RED[2])
        glVertex3f(zero[0],zero[1],zero[2])
        glVertex3f(zero[0]+1,zero[1],zero[2])
        glColor3f(GREEN[0],GREEN[1],GREEN[2])
        glVertex3f(zero[0],zero[1],zero[2])
        glVertex3f(zero[0],zero[1]+1,zero[2])
        glColor3f(BLUE[0],BLUE[1],BLUE[2])
        glVertex3f(zero[0],zero[1],zero[2])
        glVertex3f(zero[0],zero[1],zero[2]+1)
        glEnd()



